"""Interactive simulators for EVO lesson 1.2 - Statistical Inference.

The lesson explains sampling, testing and regression in prose and tables. These
simulators let the same ideas be handled: move a slider and watch the interval
narrow, re-roll and watch five intervals in a hundred miss the truth, drag an
outlier and watch the least-squares line follow it.

Every section states the point it is making underneath the chart, so a screenshot
is still worth something on its own.

Colours come from the validated categorical palette (slots 1-3) and the fixed
status palette. Aqua sits below 3:1 on a light surface, so every chart that uses
it also carries direct labels or a table - the relief rule.
"""

import altair as alt
import mistune
import numpy as np
import pandas as pd
import streamlit as st
from scipy import stats

# Categorical slots 1-3 - validated all-pairs in both modes.
C_BLUE = "#2a78d6"
C_ORANGE = "#eb6834"
C_AQUA = "#1baf7a"
# Status palette - fixed, never themed. Always paired with a label.
S_GOOD = "#0ca30c"
S_CRITICAL = "#d03b3b"
S_WARNING = "#fab219"
INK_MUTED = "#52514e"

CHART_H = 260

# Opening draws. Each is an ordinary draw, not a filtered one; the re-roll button
# shows how much the picture moves, which is itself part of the lesson.
_SEEDS = {"a2": 7, "b3": 1, "drill": 7}


def _chart_base(df):
    return alt.Chart(df).properties(height=CHART_H)


# The table plugin is on because some callouts lay their arithmetic out as a small
# table; without it mistune emits the pipe characters as literal text.
_MD = mistune.create_markdown(plugins=["table"])


def _callout(msg, colour=C_BLUE, tint="rgba(42,120,214,0.06)"):
    """A coloured callout whose body is real markdown.

    Streamlit does not process markdown inside a raw HTML block, so the text is
    rendered to HTML here first - otherwise **bold** reaches the page as asterisks.
    """
    body = _MD(msg)
    # A table produced by the markdown plugin arrives with no styling of its own,
    # so it is given borders and padding inline - a stylesheet would not reach
    # inside this block.
    if "<table>" in body:
        body = body.replace(
            "<table>",
            '<table style="border-collapse:collapse;margin:0.5rem 0;font-size:0.92em;">',
        ).replace(
            "<td>", '<td style="padding:0.22rem 0.75rem 0.22rem 0;'
                    'border-bottom:1px solid rgba(0,0,0,0.08);">'
        ).replace(
            "<th>", '<th style="padding:0.22rem 0.75rem 0.22rem 0;text-align:left;'
                    'border-bottom:1px solid rgba(0,0,0,0.22);">'
        )
    st.markdown(
        f'<div style="border-left:3px solid {colour};padding:0.55rem 0.95rem;'
        f'margin:0.4rem 0 1.2rem 0;background:{tint};">{body}</div>',
        unsafe_allow_html=True,
    )


def _point(msg):
    """The teaching line under a chart."""
    _callout(msg)


def _seed_control(key, label="Re-roll the random draw"):
    state_key = f"vl_seed_{key}"
    if state_key not in st.session_state:
        st.session_state[state_key] = _SEEDS.get(key, 7)
    if st.button(f"🎲 {label}", key=f"vl_btn_{key}"):
        st.session_state[state_key] += 1
    return st.session_state[state_key]


# --------------------------------------------------------------------------
# A. Sampling and uncertainty
# --------------------------------------------------------------------------

@st.cache_data(show_spinner=False)
def _population(shape, size=200_000, seed=0):
    rng = np.random.default_rng(seed)
    if shape == "Normal":
        return rng.normal(742, 210, size)
    if shape == "Right-skewed (order values)":
        return 300 + rng.lognormal(mean=5.9, sigma=0.75, size=size)
    if shape == "Bimodal (two customer types)":
        pick = rng.random(size) < 0.62
        return np.where(pick, rng.normal(520, 120, size), rng.normal(1180, 190, size))
    return rng.uniform(200, 1300, size)


@st.cache_data(show_spinner=False)
def _sample_means(shape, n, reps, seed):
    pop = _population(shape)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, pop.size, size=(reps, n))
    return pop[idx].mean(axis=1)


def _sampling_distribution():
    st.markdown("#### 1 · Utvalgsfordelingen og √n")
    st.caption(
        "Populasjonen kan ha hvilken som helst form. Gjennomsnittene av utvalg fra den "
        "blir likevel tilnærmet normalfordelte — og sprer seg mindre jo større n er."
    )
    c1, c2 = st.columns([1, 1])
    with c1:
        shape = st.selectbox(
            "Populasjonens form",
            ["Right-skewed (order values)", "Normal", "Bimodal (two customer types)", "Uniform"],
            key="vl_a1_shape",
        )
    with c2:
        n = st.select_slider("Utvalgsstørrelse n", [5, 10, 25, 50, 100, 200, 400], value=25, key="vl_a1_n")

    pop = _population(shape)
    means = _sample_means(shape, n, 4000, 11)
    mu, sigma = pop.mean(), pop.std(ddof=0)
    se_theory = sigma / np.sqrt(n)

    lo, hi = np.percentile(pop, 0.2), np.percentile(pop, 99.8)
    # Bin in numpy rather than in Vega: 200k rows would blow Altair's row limit,
    # and the browser has no use for the raw values.
    edges = np.linspace(lo, hi, 46)

    def _binned(values):
        counts, _ = np.histogram(np.clip(values, lo, hi), bins=edges)
        return pd.DataFrame({"verdi": (edges[:-1] + edges[1:]) / 2, "andel": counts / counts.sum()})

    pop_df, mean_df = _binned(pop), _binned(means)
    width = float(edges[1] - edges[0])

    left = (
        _chart_base(pop_df)
        .mark_bar(color=C_BLUE, cornerRadiusTopLeft=3, cornerRadiusTopRight=3, size=max(3, 520 / 46))
        .encode(
            x=alt.X("verdi:Q", scale=alt.Scale(domain=[lo, hi]), title="Populasjonen"),
            y=alt.Y("andel:Q", title="Andel", axis=alt.Axis(format="%", grid=True)),
            tooltip=[alt.Tooltip("verdi:Q", format=",.0f", title="Verdi"),
                     alt.Tooltip("andel:Q", format=".2%", title="Andel")],
        )
        .properties(title="Populasjonen — hele fordelingen")
    )
    right = (
        _chart_base(mean_df)
        .mark_bar(color=C_ORANGE, cornerRadiusTopLeft=3, cornerRadiusTopRight=3, size=max(3, 520 / 46))
        .encode(
            x=alt.X("verdi:Q", scale=alt.Scale(domain=[lo, hi]),
                    title=f"Gjennomsnitt av utvalg på n = {n}"),
            y=alt.Y("andel:Q", title="Andel", axis=alt.Axis(format="%", grid=True)),
            tooltip=[alt.Tooltip("verdi:Q", format=",.0f", title="Gjennomsnitt"),
                     alt.Tooltip("andel:Q", format=".2%", title="Andel")],
        )
        .properties(title="Utvalgsfordelingen — 4 000 utvalgsgjennomsnitt")
    )
    rule = alt.Chart(pd.DataFrame({"x": [mu]})).mark_rule(color=INK_MUTED, strokeDash=[4, 3], size=2).encode(x="x:Q")
    st.altair_chart((left + rule) | (right + rule), use_container_width=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Populasjonens μ", f"{mu:,.0f}")
    m2.metric("Populasjonens σ", f"{sigma:,.0f}")
    m3.metric("SE = σ/√n", f"{se_theory:,.1f}")
    m4.metric("Faktisk spredning", f"{means.std(ddof=1):,.1f}")

    halved = sigma / np.sqrt(n * 2)
    _point(
        f"**Begge histogrammene har samme x-akse.** Populasjonen er bred; gjennomsnittene klumper seg. "
        f"Det er dette som gjør inferens mulig.\n\n"
        f"**Og legg merke til √n:** dobler du n fra {n} til {n*2}, faller SE fra {se_theory:,.1f} til "
        f"{halved:,.1f} — en forbedring på **{(1 - halved/se_theory)*100:.0f} %**, ikke 50 %. "
        f"Å halvere usikkerheten koster fire ganger utvalget."
    )


@st.cache_data(show_spinner=False)
def _coverage_runs(shape, n, level, runs, seed):
    pop = _population(shape)
    mu = pop.mean()
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, pop.size, size=(runs, n))
    draws = pop[idx]
    xbar = draws.mean(axis=1)
    s = draws.std(axis=1, ddof=1)
    tcrit = stats.t.ppf(1 - (1 - level) / 2, n - 1)
    half = tcrit * s / np.sqrt(n)
    return mu, xbar, xbar - half, xbar + half


@st.cache_data(show_spinner=False)
def _true_coverage(shape, n, level, runs=20_000):
    """Actual coverage of the t-interval, measured rather than assumed.

    On a skewed population the sample mean is not yet normal at small n, so the
    interval covers less often than its label claims. That gap is worth showing.
    """
    pop = _population(shape)
    mu = pop.mean()
    rng = np.random.default_rng(99)
    idx = rng.integers(0, pop.size, size=(runs, n))
    draws = pop[idx]
    xbar = draws.mean(axis=1)
    s = draws.std(axis=1, ddof=1)
    half = stats.t.ppf(1 - (1 - level) / 2, n - 1) * s / np.sqrt(n)
    return float(((xbar - half <= mu) & (xbar + half >= mu)).mean())


def _coverage():
    st.markdown("#### 2 · Hva 95 % faktisk betyr")
    st.caption(
        "Hvert vannrett strek er ett intervall fra ett utvalg. Den stiplede linja er den sanne "
        "populasjonsverdien — som du i virkeligheten aldri ser."
    )
    c1, c2, c3, c4 = st.columns([1.2, 1, 1, 1])
    with c1:
        shape = st.selectbox("Populasjonens form",
                             ["Normal", "Right-skewed (order values)", "Bimodal (two customer types)"],
                             key="vl_a2_shape")
    with c2:
        n = st.select_slider("Utvalgsstørrelse n", [10, 20, 40, 80, 160], value=40, key="vl_a2_n")
    with c3:
        level = st.select_slider("Konfidensnivå", [0.80, 0.90, 0.95, 0.99], value=0.95,
                                 format_func=lambda v: f"{v:.0%}", key="vl_a2_lvl")
    with c4:
        st.write("")
        seed = _seed_control("a2", "Trekk 100 nye utvalg")

    mu, xbar, lo, hi = _coverage_runs(shape, n, level, 100, seed)
    hit = (lo <= mu) & (hi >= mu)
    df = pd.DataFrame({
        "kjøring": np.arange(1, 101), "lav": lo, "høy": hi, "snitt": xbar,
        "treff": np.where(hit, "Fanger sannheten", "Bommer"),
    })

    bars = (
        alt.Chart(df).mark_rule(size=3, strokeCap="round")
        .encode(
            y=alt.Y("kjøring:O", axis=None),
            x=alt.X("lav:Q", title="Estimert gjennomsnitt", scale=alt.Scale(zero=False)),
            x2="høy:Q",
            color=alt.Color("treff:N",
                            scale=alt.Scale(domain=["Fanger sannheten", "Bommer"], range=[C_BLUE, S_CRITICAL]),
                            legend=alt.Legend(title=None, orient="top")),
            tooltip=[alt.Tooltip("kjøring:O", title="Kjøring"),
                     alt.Tooltip("lav:Q", title="Nedre", format=",.0f"),
                     alt.Tooltip("høy:Q", title="Øvre", format=",.0f"),
                     alt.Tooltip("treff:N", title="Utfall")],
        ).properties(height=420)
    )
    dots = alt.Chart(df).mark_point(size=14, filled=True, opacity=0.85).encode(
        y=alt.Y("kjøring:O", axis=None), x="snitt:Q",
        color=alt.Color("treff:N", scale=alt.Scale(domain=["Fanger sannheten", "Bommer"],
                                                   range=[C_BLUE, S_CRITICAL]), legend=None),
    )
    truth = alt.Chart(pd.DataFrame({"x": [mu]})).mark_rule(
        color=INK_MUTED, strokeDash=[5, 4], size=2).encode(x="x:Q")
    st.altair_chart(bars + dots + truth, use_container_width=True)

    misses = int((~hit).sum())
    true_cov = _true_coverage(shape, n, level)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Bommer", f"{misses} av 100")
    m2.metric("Lovet", f"{(1-level)*100:.0f} av 100")
    m3.metric("Faktisk over 20 000 kjøringer", f"{(1-true_cov)*100:.1f} av 100")
    m4.metric("Snittbredde", f"{np.mean(hi - lo):,.0f}")
    _point(
        f"**De {level:.0%} beskriver prosedyren, ikke det enkelte intervallet.** "
        f"Her bommet {misses} av 100. Trykk «Trekk 100 nye utvalg» noen ganger: tallet svinger en god del "
        f"rundt {(1-level)*100:.0f} — hundre kjøringer er i seg selv et lite utvalg.\n\n"
        f"**Prøv 99 %:** færre bommer, og hvert intervall blir bredere. Du kan ikke kjøpe sikkerhet "
        f"uten å betale i presisjon. Og et enkelt intervall inneholder sannheten eller ikke — "
        f"du får aldri vite hvilket."
    )

    shortfall = (1 - level) - (1 - true_cov)
    if abs(shortfall) > 0.008:
        _callout(
            f"**Og her er noe verdt å oppdage: løftet holdes ikke helt.** Over 20 000 kjøringer fanger "
            f"disse intervallene sannheten **{true_cov:.1%}** av gangene, ikke {level:.0%}.\n\n"
            f"Det er ikke en feil i simulatoren. t-intervallet forutsetter at *utvalgsgjennomsnittet* er "
            f"tilnærmet normalfordelt, og på en skjev populasjon tar det større n før det blir sant. "
            f"Med n = {n} her er det ikke sant nok ennå.\n\n"
            f"**Skru n oppover og se dekningen krype mot {level:.0%}.** Dette er sentralgrenseteoremet "
            f"observert i praksis — og en påminnelse om at «95 %» er en *forutsetning som må holde*, "
            f"ikke en garanti som følger med formelen.",
            S_WARNING, "rgba(250,178,25,0.10)")


def _bias_vs_noise():
    st.markdown("#### 3 · Skjevhet mot støy — det smale og feilaktige intervallet")
    st.caption(
        "Skru opp utvalget og se intervallet smalne. Skru så på skjevheten og se at det fortsatt "
        "smalner — rundt feil verdi."
    )
    c1, c2 = st.columns(2)
    with c1:
        bias = st.slider("Skjevhet i utvalget (i standardavvik)", 0.0, 1.0, 0.35, 0.05, key="vl_a3_bias",
                         help="F.eks. bare kunder som kontaktet support svarte")
    with c2:
        max_n = st.select_slider("Hvor stort utvalg tar vi til slutt?", [100, 400, 1600, 6400],
                                 value=1600, key="vl_a3_n")

    mu, sigma = 742.0, 210.0
    ns = np.unique(np.round(np.geomspace(20, max_n, 22)).astype(int))
    se = sigma / np.sqrt(ns)
    centre = mu + bias * sigma
    df = pd.DataFrame({"n": ns, "senter": centre, "lav": centre - 1.96 * se, "høy": centre + 1.96 * se})
    df["fanger"] = np.where((df["lav"] <= mu) & (df["høy"] >= mu), "Fanger sannheten", "Bommer")

    band = alt.Chart(df).mark_area(opacity=0.22, color=C_BLUE).encode(
        x=alt.X("n:Q", scale=alt.Scale(type="log"), title="Utvalgsstørrelse (log-skala)"),
        y=alt.Y("lav:Q", title="Estimert gjennomsnitt", scale=alt.Scale(zero=False)), y2="høy:Q",
    )
    line = alt.Chart(df).mark_line(size=2, color=C_BLUE).encode(x="n:Q", y="senter:Q")
    pts = alt.Chart(df).mark_point(size=55, filled=True).encode(
        x="n:Q", y="senter:Q",
        color=alt.Color("fanger:N", scale=alt.Scale(domain=["Fanger sannheten", "Bommer"],
                                                    range=[C_BLUE, S_CRITICAL]),
                        legend=alt.Legend(title=None, orient="top")),
        tooltip=[alt.Tooltip("n:Q", title="n"), alt.Tooltip("lav:Q", format=",.0f", title="Nedre"),
                 alt.Tooltip("høy:Q", format=",.0f", title="Øvre"), alt.Tooltip("fanger:N", title="Utfall")],
    )
    truth = alt.Chart(pd.DataFrame({"y": [mu], "etikett": ["Sann verdi 742"]})).mark_rule(
        color=INK_MUTED, strokeDash=[5, 4], size=2).encode(y="y:Q")
    tlabel = alt.Chart(pd.DataFrame({"y": [mu], "t": ["Sann verdi = 742"]})).mark_text(
        align="left", dx=6, dy=-8, color=INK_MUTED, fontSize=11).encode(y="y:Q", text="t:N")
    st.altair_chart((band + line + pts + truth + tlabel).properties(height=320), use_container_width=True)

    first_miss = df.loc[df["fanger"] == "Bommer", "n"]
    m1, m2 = st.columns(2)
    m1.metric("Skjevhet i kroner", f"{bias*sigma:,.0f}")
    m2.metric("Bommer fra og med n =", f"{int(first_miss.iloc[0]):,}" if len(first_miss) else "bommer aldri")
    if bias == 0:
        _point("**Uten skjevhet:** intervallet smalner rundt sannheten, og fanger den nesten alltid. "
               "Dette er den situasjonen all formelverket forutsetter. Dra nå i skjevhets-slideren.")
    else:
        _point(
            f"**Intervallet blir smalere og mer selvsikkert — og beveger seg aldri mot sannheten.** "
            f"Skjevheten på {bias*sigma:,.0f} kr forsvinner ikke med mer data; den blir bare målt mer presist. "
            f"\n\nDet er dette som menes med at et konfidensintervall måler **presisjon, ikke nøyaktighet**. "
            f"Store utvalg gjør et skjevt estimat *farligere*, ikke tryggere, fordi rapporten ser mer overbevisende ut."
        )


# --------------------------------------------------------------------------
# B. Testing and effect size
# --------------------------------------------------------------------------

def _p_vs_d():
    st.markdown("#### 4 · p-verdi mot effektstørrelse")
    st.caption("Samme forskjell kan gi en knusende p-verdi eller ingen, avhengig av n. Effektstørrelsen bryr seg ikke om n.")
    c1, c2, c3 = st.columns(3)
    with c1:
        diff = st.slider("Forskjell mellom gruppene (kr)", 0, 200, 49, 1, key="vl_b1_diff")
    with c2:
        sd = st.slider("Standardavvik", 50, 400, 217, 1, key="vl_b1_sd")
    with c3:
        n = st.select_slider("n per gruppe", [10, 25, 50, 100, 178, 400, 1000, 4000], value=178, key="vl_b1_n")

    se = sd * np.sqrt(2 / n)
    t = diff / se if se else 0.0
    dfree = 2 * n - 2
    p = float(2 * stats.t.sf(abs(t), dfree))
    d = diff / sd

    x = np.linspace(-3.6 * sd, 3.6 * sd, 400)
    curves = pd.concat([
        pd.DataFrame({"x": x, "tetthet": stats.norm.pdf(x, 0, sd), "gruppe": "Kontroll"}),
        pd.DataFrame({"x": x, "tetthet": stats.norm.pdf(x, diff, sd), "gruppe": "Ny variant"}),
    ])
    chart = (
        alt.Chart(curves).mark_area(opacity=0.45, line={"size": 2})
        .encode(
            x=alt.X("x:Q", title="Ordreverdi (avvik fra kontrollgjennomsnittet)"),
            y=alt.Y("tetthet:Q", title="Tetthet", axis=alt.Axis(labels=False, grid=False)),
            color=alt.Color("gruppe:N", scale=alt.Scale(domain=["Kontroll", "Ny variant"],
                                                        range=[C_BLUE, C_ORANGE]),
                            legend=alt.Legend(title=None, orient="top")),
            tooltip=[alt.Tooltip("gruppe:N", title="Gruppe"), alt.Tooltip("x:Q", format=",.0f", title="Verdi")],
        ).properties(height=240)
    )
    st.altair_chart(chart, use_container_width=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("t", f"{t:,.2f}")
    m2.metric("p (tosidig)", f"{p:.4f}")
    m3.metric("Cohen's d", f"{d:.3f}")
    label = "under liten" if abs(d) < 0.2 else "liten" if abs(d) < 0.5 else "middels" if abs(d) < 0.8 else "stor"
    m4.metric("Effektstørrelse", label)

    sig = p < 0.05
    big = abs(d) >= 0.5
    cells = {
        (True, True): ("✅ Signifikant + stor effekt", "Det rene tilfellet. Handle, og oppgi størrelsen.", S_GOOD),
        (True, False): ("⚠️ Signifikant + liten effekt", "Ekte, men marginal. Avgjør på kost/nytte. Svært vanlig ved store utvalg.", S_WARNING),
        (False, False): ("➖ Ikke signifikant + liten effekt", "Genuint uinformativt. Kan være ingen effekt, kan være for lite utvalg.", INK_MUTED),
        (False, True): ("🚨 Ikke signifikant + STOR effekt", "Den farlige cella. Nesten alltid for lite utvalg — ikke rapporter dette som «ingen effekt».", S_CRITICAL),
    }
    title, body, colour = cells[(sig, big)]
    _callout(f"**{title}**\n\n{body}", colour, "rgba(0,0,0,0.03)")

    n_needed = None
    if 0 < abs(d) < 3:
        n_needed = int(np.ceil(2 * ((1.96 + 0.842) / d) ** 2))
    _point(
        "**Sett n til 4 000 og la forskjellen stå.** p stuper mot null; d rører seg ikke. "
        "Det er hele poenget: p svarer *er den målbar*, d svarer *hvor stor er den*. "
        + (f"\n\nFor å oppdage denne effekten med 80 % styrke trenger du omtrent "
           f"**{n_needed:,} per gruppe**." if n_needed else "")
    )


def _power():
    st.markdown("#### 5 · Type I, Type II og styrke")
    st.caption("Den blå kurven er verden der ingenting skjer. Den oransje er verden der effekten finnes. Terskelen deler begge.")
    c1, c2, c3 = st.columns(3)
    with c1:
        true_d = st.slider("Sann effektstørrelse (d)", 0.0, 1.2, 0.35, 0.05, key="vl_b2_d")
    with c2:
        n = st.select_slider("n per gruppe", [10, 25, 50, 100, 200, 400, 1000], value=100, key="vl_b2_n")
    with c3:
        alpha = st.select_slider("α", [0.01, 0.05, 0.10], value=0.05, format_func=lambda v: f"{v:.2f}", key="vl_b2_a")

    ncp = true_d * np.sqrt(n / 2)
    crit = stats.norm.ppf(1 - alpha / 2)
    power = float(stats.norm.sf(crit - ncp) + stats.norm.cdf(-crit - ncp))
    x = np.linspace(-4.2, max(4.2, ncp + 4.2), 500)
    curves = pd.concat([
        pd.DataFrame({"x": x, "tetthet": stats.norm.pdf(x), "verden": "H₀ er sann"}),
        pd.DataFrame({"x": x, "tetthet": stats.norm.pdf(x, ncp), "verden": "Effekten finnes"}),
    ])
    base = alt.Chart(curves).mark_area(opacity=0.4, line={"size": 2}).encode(
        x=alt.X("x:Q", title="Teststatistikk"),
        y=alt.Y("tetthet:Q", title="Tetthet", axis=alt.Axis(labels=False, grid=False)),
        color=alt.Color("verden:N", scale=alt.Scale(domain=["H₀ er sann", "Effekten finnes"],
                                                    range=[C_BLUE, C_ORANGE]),
                        legend=alt.Legend(title=None, orient="top")),
    )
    thr = alt.Chart(pd.DataFrame({"x": [crit, -crit]})).mark_rule(
        color=S_CRITICAL, size=2, strokeDash=[4, 3]).encode(x="x:Q")
    thr_lab = alt.Chart(pd.DataFrame({"x": [crit], "t": [f"Terskel ±{crit:.2f}"]})).mark_text(
        align="left", dx=6, dy=-100, color=S_CRITICAL, fontSize=11).encode(x="x:Q", text="t:N")
    st.altair_chart((base + thr + thr_lab).properties(height=260), use_container_width=True)

    m1, m2, m3 = st.columns(3)
    m1.metric("Styrke (1 − β)", f"{power:.0%}")
    m2.metric("Type II-risiko (β)", f"{1-power:.0%}")
    m3.metric("Type I-risiko (α)", f"{alpha:.0%}")
    verdict = ("god" if power >= 0.8 else "for lav — studien vil sannsynligvis bomme på en ekte effekt")
    _point(
        f"**Styrken er {power:.0%}, altså {verdict}.** Med denne effekten og dette utvalget vil "
        f"{1-power:.0%} av studiene ikke oppdage en effekt som faktisk finnes.\n\n"
        f"**Skru α ned til 0,01:** falske alarmer blir sjeldnere og styrken faller. De to feiltypene "
        f"byttes mot hverandre, og hvilken som koster mest er et forretningsspørsmål, ikke et statistisk."
    )


@st.cache_data(show_spinner=False)
def _multi_tests(k, n, seed):
    rng = np.random.default_rng(seed)
    a = rng.normal(0, 1, size=(k, n))
    b = rng.normal(0, 1, size=(k, n))
    t, p = stats.ttest_ind(a, b, axis=1)
    return p


def _multiple_comparisons():
    st.markdown("#### 6 · Multippel testing — funnet ingen gjorde")
    st.caption(
        "Her er det **ingen** forskjell mellom gruppene i noen av testene. Alle data er ren støy. "
        "Se hvor mange som likevel blir «signifikante»."
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        k = st.select_slider("Antall KPI-er du sammenligner", [5, 10, 20, 40, 100], value=20, key="vl_b3_k")
    with c2:
        alpha = st.select_slider("α", [0.01, 0.05, 0.10], value=0.05, format_func=lambda v: f"{v:.2f}", key="vl_b3_a")
    with c3:
        st.write("")
        seed = _seed_control("b3", "Kjør kvartalsgjennomgangen på nytt")

    p = _multi_tests(k, 60, seed)
    bonf = alpha / k
    df = pd.DataFrame({
        "kpi": [f"KPI {i+1}" for i in range(k)], "p": p,
        "utfall": np.where(p < bonf, "Overlever korreksjon",
                           np.where(p < alpha, "«Signifikant» — men ren støy", "Ikke signifikant")),
    })
    dom = ["Ikke signifikant", "«Signifikant» — men ren støy", "Overlever korreksjon"]
    chart = (
        alt.Chart(df).mark_circle(size=140, opacity=0.9)
        .encode(
            x=alt.X("p:Q", title="p-verdi", scale=alt.Scale(domain=[0, 1])),
            y=alt.Y("kpi:N", sort=alt.EncodingSortField("p"), title=None),
            color=alt.Color("utfall:N", scale=alt.Scale(domain=dom, range=[C_BLUE, S_CRITICAL, S_WARNING]),
                            legend=alt.Legend(title=None, orient="top", columns=1)),
            tooltip=[alt.Tooltip("kpi:N", title="KPI"), alt.Tooltip("p:Q", format=".4f", title="p"),
                     alt.Tooltip("utfall:N", title="Utfall")],
        ).properties(height=max(200, 18 * k))
    )
    lines = alt.Chart(pd.DataFrame({"x": [alpha, bonf], "hva": [f"α = {alpha}", f"Bonferroni = {bonf:.4f}"]})).mark_rule(
        size=2, strokeDash=[4, 3], color=INK_MUTED).encode(
        x="x:Q", tooltip=[alt.Tooltip("hva:N", title="Terskel")])
    st.altair_chart(chart + lines, use_container_width=True)

    n_sig = int((p < alpha).sum())
    n_bonf = int((p < bonf).sum())
    m1, m2, m3 = st.columns(3)
    m1.metric("«Signifikante» funn", n_sig)
    m2.metric("Forventet fra støy", f"{k*alpha:.1f}")
    m3.metric("Overlever Bonferroni", n_bonf)
    _point(
        f"**Ingenting skjedde, og gjennomgangen fant {n_sig} funn.** Ved α = {alpha} slår omtrent "
        f"{k*alpha:.0f} av {k} tester ut på ren støy. Dette er mekanismen bak en kvartalsgjennomgang "
        f"som alltid finner noe.\n\n"
        f"**Bonferroni** deler α på antall tester: {alpha} / {k} = {bonf:.4f}. "
        f"{'Ingen av funnene overlever den terskelen.' if n_bonf == 0 else f'{n_bonf} overlever.'} "
        f"Alternativet er å bestemme på forhånd hvilken ene sammenligning du faktisk tester."
    )


# --------------------------------------------------------------------------
# C. Regression and residuals
# --------------------------------------------------------------------------

@st.cache_data(show_spinner=False)
def _reg_base(seed=3, n=40):
    rng = np.random.default_rng(seed)
    x = rng.uniform(20, 120, n)
    y = 180 + 5.1 * x + rng.normal(0, 60, n)
    return x, y


def _leverage():
    st.markdown("#### 7 · Én uteligger, hele linja")
    st.caption("Flytt det røde punktet. Den blå linja er tilpasset alle punktene; den stiplede er uten uteliggeren.")
    c1, c2 = st.columns(2)
    with c1:
        ox = st.slider("Uteliggerens x (annonsebudsjett, kNOK)", 20, 240, 200, 5, key="vl_c1_x")
    with c2:
        oy = st.slider("Uteliggerens y (omsetning, kNOK)", 0, 1800, 260, 20, key="vl_c1_y")

    x, y = _reg_base()
    ax, ay = np.append(x, ox), np.append(y, oy)
    b_all = np.polyfit(ax, ay, 1)
    b_wo = np.polyfit(x, y, 1)

    pts = pd.DataFrame({"x": x, "y": y, "rolle": "Vanlige observasjoner"})
    out = pd.DataFrame({"x": [ox], "y": [oy], "rolle": ["Uteliggeren du flytter"]})
    xs = np.array([15, 245])
    lines = pd.concat([
        pd.DataFrame({"x": xs, "y": np.polyval(b_all, xs), "linje": "Med uteliggeren"}),
        pd.DataFrame({"x": xs, "y": np.polyval(b_wo, xs), "linje": "Uten uteliggeren"}),
    ])
    sc = alt.Chart(pts).mark_circle(size=80, opacity=0.7, color=C_BLUE).encode(
        x=alt.X("x:Q", title="Annonsebudsjett (kNOK)", scale=alt.Scale(domain=[15, 245])),
        y=alt.Y("y:Q", title="Omsetning (kNOK)", scale=alt.Scale(domain=[0, 1800])),
        tooltip=[alt.Tooltip("x:Q", format=".0f"), alt.Tooltip("y:Q", format=".0f")])
    oc = alt.Chart(out).mark_point(size=280, filled=True, color=S_CRITICAL, shape="diamond").encode(
        x="x:Q", y="y:Q", tooltip=[alt.Tooltip("x:Q", format=".0f"), alt.Tooltip("y:Q", format=".0f")])
    ln = alt.Chart(lines).mark_line(size=2.5).encode(
        x="x:Q", y="y:Q",
        strokeDash=alt.StrokeDash("linje:N", legend=alt.Legend(title=None, orient="top")),
        color=alt.Color("linje:N", scale=alt.Scale(domain=["Med uteliggeren", "Uten uteliggeren"],
                                                   range=[C_BLUE, INK_MUTED]),
                        legend=alt.Legend(title=None, orient="top")))
    st.altair_chart((sc + ln + oc).properties(height=340), use_container_width=True)

    change = (b_all[0] - b_wo[0]) / b_wo[0] * 100
    m1, m2, m3 = st.columns(3)
    m1.metric("Stigningstall med", f"{b_all[0]:.2f}")
    m2.metric("Stigningstall uten", f"{b_wo[0]:.2f}")
    m3.metric("Endring", f"{change:+.1f} %")
    _point(
        f"**Ett punkt av 41 flytter stigningstallet {abs(change):.0f} %.** Det skjer fordi minste kvadraters "
        f"metode minimerer *kvadrerte* residualer: et avvik på 10 teller hundre ganger et avvik på 1, "
        f"så linja bøyer seg mot ekstreme punkter.\n\n"
        f"**Dra uteliggeren langt ut på x-aksen.** Innflytelsen vokser med avstanden fra snittet i x — "
        f"det er derfor et punkt kan være uskyldig i midten og dominerende i kanten. "
        f"Og merk: du ser dette bare hvis du ser på residualene."
    )


@st.cache_data(show_spinner=False)
def _resid_data(pattern, seed=5, n=90):
    rng = np.random.default_rng(seed)
    x = np.sort(rng.uniform(10, 100, n))
    if pattern == "I orden — formløs sky":
        y = 50 + 3 * x + rng.normal(0, 28, n)
    elif pattern == "Kurve — sammenhengen er ikke lineær":
        y = 40 + 7.5 * x - 0.045 * x**2 + rng.normal(0, 18, n)
    elif pattern == "Vifte — heteroskedastisitet":
        y = 50 + 3 * x + rng.normal(0, 1, n) * (4 + 0.75 * x)
    else:
        y = 50 + 3 * x + 45 * np.sin(x / 6.0) + rng.normal(0, 14, n)
    return x, y


def _residuals():
    st.markdown("#### 8 · Å lese residualplottet")
    st.caption("Venstre: dataene med linja lagt gjennom. Høyre: residualene. Struktur til høyre betyr at modellformen er feil.")
    pattern = st.selectbox(
        "Mønster",
        ["I orden — formløs sky", "Kurve — sammenhengen er ikke lineær",
         "Vifte — heteroskedastisitet", "Bølge — sesong modellen ikke kjenner"],
        key="vl_c2_pat")
    x, y = _resid_data(pattern)
    b = np.polyfit(x, y, 1)
    fit = np.polyval(b, x)
    res = y - fit
    std_res = res / res.std(ddof=2)
    df = pd.DataFrame({"x": x, "y": y, "tilpasset": fit, "residual": res, "std": std_res})
    df["flagg"] = np.where(np.abs(df["std"]) > 2, "Utenfor ±2", "Innenfor")

    left = alt.Chart(df).mark_circle(size=70, opacity=0.65, color=C_BLUE).encode(
        x=alt.X("x:Q", title="Prediktor"), y=alt.Y("y:Q", title="Utfall"),
        tooltip=[alt.Tooltip("x:Q", format=".1f"), alt.Tooltip("y:Q", format=".1f")])
    line = alt.Chart(df).mark_line(size=2.5, color=C_ORANGE).encode(x="x:Q", y="tilpasset:Q")
    right = alt.Chart(df).mark_circle(size=70, opacity=0.75).encode(
        x=alt.X("tilpasset:Q", title="Tilpasset verdi"),
        y=alt.Y("residual:Q", title="Residual"),
        color=alt.Color("flagg:N", scale=alt.Scale(domain=["Innenfor", "Utenfor ±2"],
                                                   range=[C_BLUE, S_CRITICAL]),
                        legend=alt.Legend(title=None, orient="top")),
        tooltip=[alt.Tooltip("residual:Q", format=".1f", title="Residual"),
                 alt.Tooltip("std:Q", format=".2f", title="Standardisert")])
    zero = alt.Chart(pd.DataFrame({"y": [0]})).mark_rule(color=INK_MUTED, strokeDash=[4, 3], size=2).encode(y="y:Q")
    st.altair_chart(
        ((left + line).properties(title="Data og tilpasset linje", height=280)
         | (right + zero).properties(title="Residualer mot tilpasset verdi", height=280)),
        use_container_width=True)

    reading = {
        "I orden — formløs sky": (
            "**Dette er målet.** Ingen struktur til høyre: residualene ligger som en formløs sky rundt null, "
            "med noenlunde jevn bredde. Modellformen er dekkende. At noen få punkter er flagget utenfor ±2 "
            "er helt normalt — omtrent 5 % skal ligge der selv i en perfekt modell. Det er *mønsteret* du "
            "ser etter, ikke enkeltpunkter.", S_GOOD),
        "Kurve — sammenhengen er ikke lineær": (
            "**En bue i residualene betyr at en rett linje ble lagt gjennom en krum sammenheng.** "
            "Modellen underestimerer i midten og overestimerer i endene, systematisk. "
            "Løsning: legg til et kvadratledd, transformer variabelen, eller bytt modell.", S_CRITICAL),
        "Vifte — heteroskedastisitet": (
            "**Vifta betyr at feilen vokser med prediksjonens størrelse.** Det viktige er hva som brytes: "
            "koeffisientene er fortsatt brukbare, men standardfeilene er feil — og dermed **hver eneste "
            "p-verdi og hvert intervall i tabellen**. Løsning: robuste standardfeil, eller log-transformer utfallet.", S_WARNING),
        "Bølge — sesong modellen ikke kjenner": (
            "**Bølgen er et tidsmønster modellen ikke inneholder.** Dette er Black Friday-residualen i "
            "generell form: avviket forteller ikke at dataene er skitne, men at modellen mangler en variabel. "
            "Løsning: legg til et sesong- eller trendledd — ikke slett punktene.", S_WARNING),
    }
    msg, colour = reading[pattern]
    _callout(msg, colour, "rgba(0,0,0,0.03)")
    st.caption(
        f"Merk at R² er {np.corrcoef(x, y)[0,1]**2:.2f} her. "
        "Et høyt R² utelukker ikke noe av dette — derfor er residualplottet ikke valgfritt."
    )


def _omitted_variable():
    st.markdown("#### 9 · Koeffisienten som endrer seg når du legger til en variabel")
    st.caption(
        "Annonsebudsjett og rabattdybde henger sammen: tunge kampanjer kjørte også dypere rabatter. "
        "Dra i sliderne og se hva det gjør med annonseringens koeffisient."
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        corr = st.slider("Samvariasjon mellom prediktorene", 0.0, 0.95, 0.70, 0.05, key="vl_c3_corr",
                         help="Kjørte tunge kampanjer også dypere rabatter?")
    with c2:
        true_b2 = st.slider("Rabattdybdens sanne effekt (b₂)", 0.0, 40.0, 21.4, 0.5, key="vl_c3_b2")
    with c3:
        sd_disc = st.slider("Hvor mye varierer rabattdybden?", 1.0, 12.0, 6.0, 0.5, key="vl_c3_sd")

    rng = np.random.default_rng(4)
    n, sd_ad, b1_true = 200, 42.0, 5.1
    z = rng.normal(size=n)
    ad = 100 + sd_ad * z
    disc = 8 + sd_disc * (corr * z + np.sqrt(max(1 - corr**2, 1e-9)) * rng.normal(size=n))
    rev = 3000 + b1_true * ad + true_b2 * disc + rng.normal(0, 150, n)

    b_simple = np.polyfit(ad, rev, 1)[0]
    X = np.column_stack([np.ones(n), ad, disc])
    coef, *_ = np.linalg.lstsq(X, rev, rcond=None)
    b_multi = coef[1]

    def r2(pred):
        return 1 - ((rev - pred) ** 2).sum() / ((rev - rev.mean()) ** 2).sum()
    r2_s = r2(np.polyval(np.polyfit(ad, rev, 1), ad))
    r2_m = r2(X @ coef)
    adj = lambda r, k: 1 - (1 - r) * (n - 1) / (n - k - 1)

    df = pd.DataFrame({
        "modell": ["Enkel: bare annonsering", "Multippel: + rabattdybde"],
        "koeffisient": [b_simple, b_multi],
    })
    bars = (
        alt.Chart(df).mark_bar(cornerRadiusEnd=4, size=48)
        .encode(
            x=alt.X("koeffisient:Q", title="Annonseringens koeffisient"),
            y=alt.Y("modell:N", title=None, sort=None),
            color=alt.Color("modell:N", scale=alt.Scale(
                domain=["Enkel: bare annonsering", "Multippel: + rabattdybde"], range=[C_ORANGE, C_BLUE]),
                legend=None),
            tooltip=[alt.Tooltip("modell:N", title="Modell"), alt.Tooltip("koeffisient:Q", format=".2f")],
        ).properties(height=150)
    )
    labels = alt.Chart(df).mark_text(align="left", dx=8, fontSize=13, color=INK_MUTED).encode(
        x="koeffisient:Q", y=alt.Y("modell:N", sort=None), text=alt.Text("koeffisient:Q", format=".2f"))
    st.altair_chart(bars + labels, use_container_width=True)

    drop = (b_simple - b_multi) / b_simple * 100 if b_simple else 0
    bias_theory = true_b2 * corr * sd_disc / sd_ad
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Enkel modell", f"{b_simple:.2f}")
    m2.metric("Multippel modell", f"{b_multi:.2f}", help=f"Den sanne verdien er {b1_true}")
    m3.metric("Endring", f"{-drop:+.0f} %")
    m4.metric("Justert R²", f"{adj(r2_s,1):.2f} → {adj(r2_m,2):.2f}")
    st.caption(
        f"Skjevheten er ikke tilfeldig — den har en formel: "
        f"**b₂ × samvariasjon × (σ_rabatt / σ_annonse)** = "
        f"{true_b2:.1f} × {corr:.2f} × ({sd_disc:.1f} / {sd_ad:.0f}) = **{bias_theory:.2f}**. "
        f"Legg den til den sanne verdien {b1_true} og du får omtrent det den enkle modellen rapporterer."
    )
    _point(
        f"**Ingenting med annonsering endret seg — spørsmålet endret seg.** "
        f"Den enkle koeffisienten på {b_simple:.1f} svarer «hvor mye mer omsetning følger en ekstra kNOK "
        f"annonsering», og inkluderer stilltiende at tunge kampanjer også kjørte dypere rabatter. "
        f"Den multiple på {b_multi:.1f} svarer «hvor mye mer, blant måneder med *samme* rabattdybde». "
        f"Bare den siste er i nærheten av den sanne verdien {b1_true}.\n\n"
        f"**Sett samvariasjonen til 0:** de to koeffisientene faller sammen. Utelatt-variabel-effekten "
        f"finnes bare når prediktorene henger sammen — og det gjør de nesten alltid i virkelige data.\n\n"
        f"**En ærlig merknad om tallene:** leksjonens egen tabell viser 8,2 → 5,1. Med rabattdybdens "
        f"spredning der (3,1 mot annonseringens 42) er det største mulige avviket 1,6, så det spranget "
        f"krever en større rabattvariasjon enn tabellen oppgir. Mekanismen er den samme; skalaen i "
        f"leksjonen henger ikke helt sammen. Dra i «hvor mye varierer rabattdybden» og se hvorfor."
    )


# --------------------------------------------------------------------------
# D. Exam drill
# --------------------------------------------------------------------------

def _fmt(v, dec=3):
    return f"{v:,.{dec}f}"


def _check(label, user, truth, tol, unit="", formula="", why=""):
    """Render one drill step with per-step feedback."""
    ok = user is not None and abs(user - truth) <= tol
    if user is None or user == 0.0:
        st.caption(f"↳ {formula}")
        return False
    if ok:
        st.success(f"✅ Riktig — {label} = {_fmt(truth)}{unit}. {why}")
    else:
        st.error(f"❌ Ikke helt. {label} = **{_fmt(truth)}{unit}**.  \nFormel: `{formula}`  \n{why}")
    return ok


@st.cache_data(show_spinner=False)
def _drill_case(kind, seed):
    rng = np.random.default_rng(seed)
    if kind == "Test en påstand (ett utvalg)":
        return {
            "claim": round(float(rng.uniform(4.2, 4.7)), 1),
            "n": int(rng.choice([80, 100, 120, 150, 200])),
            "mean": round(float(rng.uniform(4.05, 4.55)), 2),
            "sd": round(float(rng.uniform(0.6, 1.0)), 2),
        }
    if kind == "Sammenlign to grupper":
        return {
            "n1": int(rng.choice([120, 150, 176, 200])), "m1": round(float(rng.uniform(760, 820)), 0),
            "s1": round(float(rng.uniform(180, 240)), 0),
            "n2": int(rng.choice([120, 150, 180, 210])), "m2": round(float(rng.uniform(700, 760)), 0),
            "s2": round(float(rng.uniform(180, 240)), 0),
        }
    return {
        "p": round(float(rng.uniform(0.42, 0.66)), 2),
        "n": int(rng.choice([400, 600, 900, 1200, 2400])),
    }


def _drill():
    st.markdown("#### 10 · Eksamensdrill med tilbakemelding per steg")
    st.caption(
        "Oppgavetypene fra aktivitet 1.2.1 og 1.2.2, med nye tall hver gang. "
        "Skriv inn svaret på hvert steg — du får formelen og forklaringen med én gang, ikke bare fasit til slutt."
    )
    c1, c2 = st.columns([2, 1])
    with c1:
        kind = st.selectbox("Oppgavetype",
                            ["Test en påstand (ett utvalg)", "Sammenlign to grupper",
                             "Konfidensintervall for en andel"], key="vl_d_kind")
    with c2:
        st.write("")
        seed = _seed_control("drill", "Nye tall")

    case = _drill_case(kind, seed)
    st.divider()

    if kind == "Test en påstand (ett utvalg)":
        claim, n, mean, sd = case["claim"], case["n"], case["mean"], case["sd"]
        st.markdown(
            f"> En kjede hevder at kundene gir den **minst {claim} av 5**. "
            f"Et tilfeldig utvalg på **n = {n}** gir gjennomsnitt **{mean}** med standardavvik **{sd}**. "
            f"Holder påstanden ved α = 0,05?")
        st.markdown("**Steg 1 — hypotesene.** Hvor hører påstanden hjemme?")
        h = st.radio("Velg oppsett", [
            "H₀: μ ≥ {c} · Hₐ: μ < {c} — ensidig".format(c=claim),
            "H₀: μ < {c} · Hₐ: μ ≥ {c} — ensidig".format(c=claim),
            "H₀: μ = {c} · Hₐ: μ ≠ {c} — tosidig".format(c=claim),
        ], index=None, key="vl_d1_h")
        if h:
            if h.startswith(f"H₀: μ ≥ {claim}"):
                st.success("✅ Riktig. Påstanden er standardantakelsen som må motbevises, så den ligger i H₀, "
                           "og du tester om snittet er *lavere*. Ensidig, fordi bare den ene retningen truer påstanden.")
            elif h.startswith(f"H₀: μ < {claim}"):
                st.error("❌ Dette snur bevisbyrden. Du aksepterer aldri en nullhypotese, så med dette oppsettet "
                         "kan du aldri *bekrefte* påstanden — du kan bare unnlate å forkaste at den er feil.")
            else:
                st.warning("⚠️ Ikke feil, men svakere. Tosidig tester om snittet avviker i *begge* retninger. "
                           "Her truer bare den ene retningen påstanden, så ensidig er riktig — og må erklæres før dataene ses.")
        se = sd / np.sqrt(n)
        dfree = n - 1
        t = (mean - claim) / se
        p = float(stats.t.cdf(t, dfree))
        tc = float(stats.t.ppf(0.975, dfree))
        lo, hi = mean - tc * se, mean + tc * se
        d = (claim - mean) / sd

        st.markdown("**Steg 2 — standardfeilen.**")
        u = st.number_input("SE =", value=0.0, format="%.4f", step=0.001, key="vl_d1_se")
        _check("SE", u or None, se, 0.002, formula="SE = s / √n", why="Standardfeilen er hvor mye gjennomsnittet ville flyttet seg fra utvalg til utvalg.")
        st.markdown("**Steg 3 — teststatistikken.**")
        u = st.number_input("t =", value=0.0, format="%.3f", step=0.01, key="vl_d1_t")
        _check("t", u or None, t, 0.05, formula="t = (x̄ − μ₀) / SE", why=f"Med {dfree} frihetsgrader.")
        st.markdown("**Steg 4 — p-verdien (ensidig).**")
        u = st.number_input("p =", value=0.0, format="%.4f", step=0.001, key="vl_d1_p")
        _check("p", u or None, p, 0.006, formula="=T.DIST(t; df; SANN)", why="Sannsynligheten for data minst så ekstreme *gitt at* H₀ er sann.")
        st.markdown("**Steg 5 — effektstørrelsen.**")
        u = st.number_input("Cohen's d =", value=0.0, format="%.3f", step=0.01, key="vl_d1_d")
        _check("d", u or None, d, 0.02, formula="d = (μ₀ − x̄) / s", why="Avviket målt i standardavvik — uavhengig av n.")

        with st.expander("📋 Fasit og modellsvaret", expanded=False):
            lab = "under liten" if abs(d) < 0.2 else "liten" if abs(d) < 0.5 else "middels" if abs(d) < 0.8 else "stor"
            st.markdown(
                f"| Steg | Verdi |\n|---|---|\n"
                f"| SE | {se:.4f} |\n| t | {t:.3f} på {dfree} fg |\n| p (ensidig) | {p:.4f} |\n"
                f"| 95 % KI | [{lo:.3f}, {hi:.3f}] |\n| Cohen's d | {d:.3f} ({lab}) |\n\n"
                f"**{'Forkast H₀' if p < 0.05 else 'Ikke grunnlag for å forkaste H₀'}** ved α = 0,05.\n\n"
                f"**Slik ville jeg skrevet det:** «Gjennomsnittsvurderingen er {mean} "
                f"(95 % KI [{lo:.2f}, {hi:.2f}], n = {n}). "
                + (f"Ensidig t-test mot påstanden på {claim} gir t = {t:.2f}, p = {p:.3f}, så påstanden er "
                   f"ikke holdbar som formulert. Avviket er {claim-mean:.2f} poeng, d = {d:.2f} ({lab}), "
                   f"altså statistisk etablert og praktisk beskjedent — en etterlevelsessak snarere enn en kundekrise.»"
                   if p < 0.05 else
                   f"Ensidig t-test mot {claim} gir t = {t:.2f}, p = {p:.3f}. Beviset er ikke sterkt nok til å "
                   f"forkaste påstanden, hvilket ikke er det samme som å ha bekreftet den.»")
            )

    elif kind == "Sammenlign to grupper":
        n1, m1_, s1 = case["n1"], case["m1"], case["s1"]
        n2, m2_, s2 = case["n2"], case["m2"], case["s2"]
        st.markdown(
            f"> Ny variant: **n = {n1}**, snitt **{m1_:,.0f} kr**, standardavvik **{s1:,.0f}**. "
            f"Gammel: **n = {n2}**, snitt **{m2_:,.0f} kr**, standardavvik **{s2:,.0f}**. "
            f"Er forskjellen reell, og er den stor nok til å bry seg om?")
        sp = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))
        se = sp * np.sqrt(1/n1 + 1/n2)
        diff = m1_ - m2_
        t = diff / se
        dfree = n1 + n2 - 2
        p = float(2 * stats.t.sf(abs(t), dfree))
        d = diff / sp
        tc = float(stats.t.ppf(0.975, dfree))

        st.markdown("**Steg 1 — samlet standardavvik.**")
        u = st.number_input("s_pooled =", value=0.0, format="%.2f", step=0.1, key="vl_d2_sp")
        _check("s_pooled", u or None, sp, 0.6, formula="√( ((n₁−1)s₁² + (n₂−1)s₂²) / (n₁+n₂−2) )",
               why="Vektet sammenslåing av begge gruppenes spredning.")
        st.markdown("**Steg 2 — standardfeilen for forskjellen.**")
        u = st.number_input("SE =", value=0.0, format="%.2f", step=0.1, key="vl_d2_se")
        _check("SE", u or None, se, 0.4, formula="SE = s_pooled × √(1/n₁ + 1/n₂)")
        st.markdown("**Steg 3 — t.**")
        u = st.number_input("t =", value=0.0, format="%.3f", step=0.01, key="vl_d2_t")
        _check("t", u or None, t, 0.05, formula="t = (x̄₁ − x̄₂) / SE", why=f"{dfree} frihetsgrader.")
        st.markdown("**Steg 4 — Cohen's d.**")
        u = st.number_input("d =", value=0.0, format="%.3f", step=0.01, key="vl_d2_d")
        _check("d", u or None, d, 0.02, formula="d = (x̄₁ − x̄₂) / s_pooled",
               why="Legg merke til at n ikke står i denne formelen.")

        with st.expander("📋 Fasit og modellsvaret", expanded=False):
            lo, hi = diff - tc*se, diff + tc*se
            lab = "under liten" if abs(d) < 0.2 else "liten" if abs(d) < 0.5 else "middels" if abs(d) < 0.8 else "stor"
            st.markdown(
                f"| Steg | Verdi |\n|---|---|\n| Forskjell | {diff:,.0f} kr |\n| s_pooled | {sp:,.2f} |\n"
                f"| SE | {se:,.2f} |\n| t | {t:.3f} på {dfree} fg |\n| p (tosidig) | {p:.4f} |\n"
                f"| 95 % KI | [{lo:,.2f}, {hi:,.2f}] |\n| Cohen's d | {d:.3f} ({lab}) |\n\n"
                f"**Les p og d sammen.** {'Signifikant' if p < 0.05 else 'Ikke signifikant'} "
                f"med en {lab} effekt. "
                + ("Det er den farlige kombinasjonen: en stor observert effekt som ikke nådde terskelen "
                   "betyr nesten alltid for lite utvalg — ikke «ingen effekt»."
                   if p >= 0.05 and abs(d) >= 0.5 else
                   "Intervallet er det som avgjør beslutningen: regn det om til kroner i året og "
                   "hold det mot kostnaden, i begge ender.")
            )

    else:
        p_hat, n = case["p"], case["n"]
        st.markdown(
            f"> En måling gir **{p_hat:.0%}** oppslutning i et tilfeldig utvalg på **n = {n:,}**. "
            f"Hva er 95 %-intervallet, og hva kan du og kan du ikke si?")
        me = 1.96 * np.sqrt(p_hat * (1 - p_hat) / n)
        lo, hi = p_hat - me, p_hat + me
        n_for_2 = int(np.ceil(1.96**2 * p_hat * (1 - p_hat) / 0.02**2))

        st.markdown("**Steg 1 — feilmarginen, i prosentpoeng.**")
        u = st.number_input("Margin (pp) =", value=0.0, format="%.2f", step=0.1, key="vl_d3_me")
        _check("Marginen", u or None, me*100, 0.15, unit=" pp",
               formula="z × √( p(1−p) / n )   med z = 1,96",
               why="Merk at den er størst når p er nær 50 % — det er det konservative verste tilfellet.")
        st.markdown("**Steg 2 — nedre grense, i prosent.**")
        u = st.number_input("Nedre grense (%) =", value=0.0, format="%.2f", step=0.1, key="vl_d3_lo")
        _check("Nedre grense", u or None, lo*100, 0.2, unit=" %", formula="p − margin",
               why="Det er denne grensen en beslutningstaker som bærer nedsiden trenger.")
        st.markdown("**Steg 3 — hvor stort utvalg for ±2 prosentpoeng?**")
        u = st.number_input("n =", value=0.0, format="%.0f", step=10.0, key="vl_d3_n")
        _check("Nødvendig n", u or None, n_for_2, max(25, n_for_2*0.02), formula="n = z² × p(1−p) / margin²",
               why="Legg merke til at marginen står i **andre** — å halvere den koster fire ganger utvalget.")

        with st.expander("📋 Fasit og modellsvaret", expanded=False):
            majority = "hele intervallet ligger over 50 %" if lo > 0.505 else (
                "hele intervallet ligger under 50 %" if hi < 0.495 else
                "intervallet berører 50 % — flertall er **ikke** etablert")
            st.markdown(
                f"| Steg | Verdi |\n|---|---|\n| Margin | ±{me*100:.2f} pp |\n"
                f"| 95 % KI | [{lo:.1%}, {hi:.1%}] |\n| n for ±2 pp | {n_for_2:,} |\n\n"
                f"**Tolkning:** {majority}.\n\n"
                f"**Og det marginen ikke dekker:** frafall, dekning, spørsmålsformulering, "
                f"feilrapportert intensjon og oppmøte. Marginen kvantifiserer **bare** tilfeldig utvalgsfeil. "
                f"Et stramt intervall på et skjevt utvalg er et presist galt svar."
            )


# --------------------------------------------------------------------------
# Page
# --------------------------------------------------------------------------


def _zscore():
    st.markdown("#### 11 · Z-score, begge veier")
    st.caption("Z = (x − μ) ÷ σ. Framover beskriver den én observasjon; bakover setter den en terskel.")
    c1, c2, c3 = st.columns(3)
    with c1:
        mu = st.slider("Gjennomsnitt μ", 100, 2000, 742, 10, key="vl_z_mu")
    with c2:
        sigma = st.slider("Standardavvik σ", 20, 800, 210, 10, key="vl_z_sd")
    with c3:
        x = st.slider("Observasjon x", 0, 3000, 1240, 10, key="vl_z_x")

    z = (x - mu) / sigma
    tail = float(stats.norm.sf(abs(z)))
    grid = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 500)
    dens = pd.DataFrame({"x": grid, "tetthet": stats.norm.pdf(grid, mu, sigma)})
    lo_t, hi_t = (grid <= min(x, 2 * mu - x)), (grid >= max(x, 2 * mu - x))
    shade = dens[lo_t | hi_t]

    base = alt.Chart(dens).mark_area(color=C_BLUE, opacity=0.25, line={"size": 2, "color": C_BLUE}).encode(
        x=alt.X("x:Q", title="Verdi"),
        y=alt.Y("tetthet:Q", title="Tetthet", axis=alt.Axis(labels=False, grid=False)))
    tails = alt.Chart(shade).mark_area(color=S_CRITICAL, opacity=0.55).encode(x="x:Q", y="tetthet:Q")
    rule = alt.Chart(pd.DataFrame({"x": [x]})).mark_rule(color=S_CRITICAL, size=2.5).encode(x="x:Q")
    mean_rule = alt.Chart(pd.DataFrame({"x": [mu]})).mark_rule(
        color=INK_MUTED, strokeDash=[4, 3], size=2).encode(x="x:Q")
    st.altair_chart((base + tails + mean_rule + rule).properties(height=260), use_container_width=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Z", f"{z:+.3f}")
    m2.metric("Andel lenger ut (én hale)", f"{tail:.2%}")
    m3.metric("Begge haler", f"{2*tail:.2%}")
    reading = ("vanlig variasjon" if abs(z) < 1 else "noe uvanlig" if abs(z) < 1.96
               else "uvanlig — verdt et blikk" if abs(z) < 2.58 else "sjelden — undersøk")
    m4.metric("Lesning", reading)

    st.markdown("**Og bakover — den retningen som faktisk brukes:**")
    zt = st.select_slider("Velg terskel i Z", [1.0, 1.645, 1.96, 2.576, 3.0], value=1.96,
                          format_func=lambda v: f"Z = {v}", key="vl_z_thr")
    st.info(f"x = μ + Z × σ = {mu:,} + {zt} × {sigma:,} = **{mu + zt*sigma:,.0f}**  ·  "
            f"nedre terskel: **{mu - zt*sigma:,.0f}**")
    _point(
        f"**Framover** svarer den «hvor uvanlig var denne observasjonen» — her {z:+.2f} standardavvik, "
        f"med {tail:.1%} av fordelingen lenger ut i den halen.\n\n"
        f"**Bakover** svarer den «hvilken verdi skal alarmen stå på», og det er den retningen som gjør "
        f"en z-score til noe operativt: den oversetter et valgt konfidensnivå til et tall i kroner. "
        f"Det er slik en terskel settes fra dataene i stedet for fra magefølelsen.\n\n"
        f"**To forbehold.** Tolkningen forutsetter en tilnærmet symmetrisk fordeling — på skjeve data "
        f"som ordreverdier stempler den vanlige verdier som ekstreme. Og μ og σ er selv estimater som "
        f"uteliggeren din er med på å blåse opp."
    )


@st.cache_data(show_spinner=False)
def _overfit_data(seed=11, n_train=18, n_hold=40):
    rng = np.random.default_rng(seed)
    xt = np.sort(rng.uniform(0, 10, n_train))
    yt = 2 + 1.4 * xt + rng.normal(0, 2.2, n_train)
    xh = np.sort(rng.uniform(0, 10, n_hold))
    yh = 2 + 1.4 * xh + rng.normal(0, 2.2, n_hold)
    return xt, yt, xh, yh


def _overfitting():
    st.markdown("#### 12 · R² som ser bedre ut jo verre modellen blir")
    st.caption(
        "Den sanne sammenhengen er en rett linje med støy. Skru opp modellens fleksibilitet og se "
        "de to R²-ene skille lag."
    )
    deg = st.select_slider("Modellens fleksibilitet (polynomgrad)", [1, 2, 3, 4, 5, 7, 9, 11, 13],
                           value=1, key="vl_of_deg")
    xt, yt, xh, yh = _overfit_data()
    coef = np.polyfit(xt, yt, deg)

    def r2(y, pred):
        return 1 - ((y - pred) ** 2).sum() / ((y - y.mean()) ** 2).sum()
    r2_train, r2_hold = r2(yt, np.polyval(coef, xt)), r2(yh, np.polyval(coef, xh))

    grid = np.linspace(0, 10, 300)
    curve = pd.DataFrame({"x": grid, "y": np.polyval(coef, grid)})
    curve = curve[(curve["y"] > -10) & (curve["y"] < 30)]
    pts = pd.concat([
        pd.DataFrame({"x": xt, "y": yt, "sett": "Treningsdata (modellen så disse)"}),
        pd.DataFrame({"x": xh, "y": yh, "sett": "Hold-out (modellen har aldri sett disse)"}),
    ])
    sc = alt.Chart(pts).mark_point(size=75, filled=True, opacity=0.7).encode(
        x=alt.X("x:Q", title="Prediktor"),
        y=alt.Y("y:Q", title="Utfall", scale=alt.Scale(domain=[-10, 30])),
        color=alt.Color("sett:N", scale=alt.Scale(
            domain=["Treningsdata (modellen så disse)", "Hold-out (modellen har aldri sett disse)"],
            range=[C_ORANGE, C_BLUE]), legend=alt.Legend(title=None, orient="top", columns=1)),
        shape=alt.Shape("sett:N", legend=None),
        tooltip=[alt.Tooltip("sett:N"), alt.Tooltip("x:Q", format=".2f"), alt.Tooltip("y:Q", format=".2f")])
    ln = alt.Chart(curve).mark_line(size=2.5, color=S_CRITICAL).encode(x="x:Q", y="y:Q")
    st.altair_chart((sc + ln).properties(height=320), use_container_width=True)

    m1, m2, m3 = st.columns(3)
    m1.metric("R² på treningsdata", f"{r2_train:.3f}")
    m2.metric("R² på hold-out", f"{r2_hold:,.3f}" if r2_hold > -100 else f"{r2_hold:,.0f}")
    m3.metric("Gapet", f"{r2_train - r2_hold:,.3f}" if r2_hold > -100 else "kollapset")

    if deg == 1:
        _callout(
            f"**Riktig modell.** R² på treningsdata er {r2_train:.2f} og på hold-out {r2_hold:.2f} — "
            f"nær hverandre, som de skal være når modellformen stemmer med virkeligheten. "
            f"Skru nå fleksibiliteten oppover.", S_GOOD, "rgba(12,163,12,0.08)")
    elif r2_hold < 0:
        _callout(
            f"**Se på de to tallene.** Treningsdataene sier {r2_train:.3f} — nesten perfekt. "
            f"Hold-out sier {r2_hold:,.0f}, altså verre enn å gjette gjennomsnittet hver gang.\n\n"
            f"Modellen har memorert de {len(xt)} punktene den fikk se, inkludert støyen i dem. "
            f"**Og den eneste av de to tallene et resultattabell-utdrag vanligvis viser, er det første.**",
            S_CRITICAL, "rgba(208,59,59,0.08)")
    else:
        _callout(
            f"**Gapet åpner seg.** R² på treningsdata stiger til {r2_train:.3f} mens hold-out faller "
            f"til {r2_hold:.3f}. Modellen blir bedre til å beskrive fortiden og dårligere til å "
            f"forutsi noe.", S_WARNING, "rgba(250,178,25,0.10)")

    _point(
        "**Dette er hvorfor et høyt R² ikke er en anbefaling.** R² kan alltid heves ved å legge til "
        "fleksibilitet, og hver eneste andre diagnostikk i tabellen spør om modellen beskriver *dette* "
        "datasettet godt. Bare en hold-out spør om den virker på data den ikke har sett — som er "
        "spørsmålet en forretningsbeslutning faktisk hviler på.\n\n"
        "**Får du bare ett datasett i en oppgave,** si eksplisitt at en hold-out-evaluering ville "
        "vært nødvendig før resultatet kunne stoles på i drift. Det er ofte verdt et poeng i seg selv."
    )


@st.cache_data(show_spinner=False)
def _simpson_data(strength, seed=3, per=30):
    rng = np.random.default_rng(seed)
    rows = []
    for i, (cx, cy) in enumerate([(20, 300), (45, 520), (70, 760), (95, 1000)]):
        x = rng.normal(cx, 7, per)
        y = cy - strength * (x - cx) + rng.normal(0, 25, per)
        rows.append(pd.DataFrame({"x": x, "y": y, "segment": f"Segment {i+1}"}))
    return pd.concat(rows, ignore_index=True)


def _confounding():
    st.markdown("#### 13 · Sammenhengen som snur når du deler opp dataene")
    st.caption(
        "Rabattdybde mot omsetning per kunde. Se på skyen samlet, og se så på hvert kundesegment for seg."
    )
    c1, c2 = st.columns(2)
    with c1:
        strength = st.slider("Effekt innad i hvert segment", -4.0, 4.0, 3.2, 0.2, key="vl_sp_str",
                             help="Positiv verdi = fallende sammenheng innad i segmentet")
    with c2:
        split = st.toggle("Del opp i segmenter", value=False, key="vl_sp_split")

    df = _simpson_data(strength)
    overall = np.polyfit(df["x"], df["y"], 1)[0]
    within = [np.polyfit(g["x"], g["y"], 1)[0] for _, g in df.groupby("segment")]

    if split:
        pts = alt.Chart(df).mark_point(size=55, filled=True, opacity=0.7).encode(
            x=alt.X("x:Q", title="Rabattdybde (%)"), y=alt.Y("y:Q", title="Omsetning per kunde"),
            color=alt.Color("segment:N", scale=alt.Scale(range=[C_BLUE, C_ORANGE, C_AQUA, S_WARNING]),
                            legend=alt.Legend(title=None, orient="top")),
            tooltip=["segment:N", alt.Tooltip("x:Q", format=".1f"), alt.Tooltip("y:Q", format=".0f")])
        lines = pts.transform_regression("x", "y", groupby=["segment"]).mark_line(size=2.5)
    else:
        pts = alt.Chart(df).mark_point(size=55, filled=True, opacity=0.6, color=INK_MUTED).encode(
            x=alt.X("x:Q", title="Rabattdybde (%)"), y=alt.Y("y:Q", title="Omsetning per kunde"),
            tooltip=[alt.Tooltip("x:Q", format=".1f"), alt.Tooltip("y:Q", format=".0f")])
        lines = pts.transform_regression("x", "y").mark_line(size=3, color=S_CRITICAL)
    st.altair_chart((pts + lines).properties(height=340), use_container_width=True)

    m1, m2, m3 = st.columns(3)
    m1.metric("Samlet stigningstall", f"{overall:+.2f}")
    m2.metric("Innad i segmentene", " · ".join(f"{w:+.1f}" for w in within))
    m3.metric("Snur fortegnet?", "JA" if overall * np.mean(within) < 0 else "nei")

    if overall * np.mean(within) < 0:
        _callout(
            f"**Samlet sett stiger sammenhengen ({overall:+.2f}). Innad i hvert eneste segment faller "
            f"den ({np.mean(within):+.1f} i snitt).** Begge er korrekt regnet ut på de samme dataene.\n\n"
            f"Forklaringen er den skjulte variabelen: segmentene ligger på forskjellige nivåer *og* får "
            f"forskjellig rabatt. Når du ser på skyen samlet, måler du forskjellen **mellom** segmenter "
            f"og tror du måler effekten **innad** i dem.\n\n"
            f"Dette har et navn — **Simpsons paradoks** — og det er den skarpeste illustrasjonen av "
            f"hvorfor korrelasjon ikke er årsakssammenheng. Ingen mengde flere datapunkter oppdager det. "
            f"Bare det å spørre «hva mer skiller disse observasjonene?» gjør det.",
            S_CRITICAL, "rgba(208,59,59,0.08)")
    else:
        _point(
            "Nå peker samlet og innad samme vei. **Dra «effekt innad» over på den andre siden av null** "
            "og se hva som skjer med det samlede stigningstallet.")

    _point(
        "**Den praktiske testen:** før du tolker et stigningstall, spør hva som ellers skiller "
        "observasjonene fra hverandre, og om den variabelen henger sammen både med prediktoren og med "
        "utfallet. Hvis ja, er den en **konfunder**, og koeffisienten din svarer på et annet spørsmål "
        "enn du tror.\n\n"
        "Det er også nøyaktig samme mekanisme som simulator 9: å legge inn segmentet som prediktor er "
        "det som skiller *innad*-effekten fra *mellom*-effekten."
    )



@st.cache_data(show_spinner=False)
def _house_data(expo, noise, hi, n, seed):
    """Prices follow a power law, so price per square metre falls as size rises."""
    A = 4.5e6 / 50 ** expo
    rng = np.random.default_rng(seed)
    size = rng.uniform(45, hi, n)
    price = A * size ** expo * np.exp(rng.normal(0, noise, n))
    return size, price, A


def _real_estate():
    st.markdown("#### 14 · Boligprisene — når en rett linje er nesten riktig")
    st.caption(
        "Leksjonens eiendomscase. Meglerkontoret plotter areal mot pris og ser en kurve: "
        "prisen per kvadratmeter faller når boligene blir større."
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        model = st.radio("Modell", ["Rett linje", "Polynom (kvadratledd)", "Logaritmisk (log-log)"],
                         key="vl_re_model")
    with c2:
        expo = st.slider("Hvor kraftig avtar prisen per m²?", 0.45, 1.0, 0.60, 0.05, key="vl_re_expo",
                         help="1,0 = ingen avtakende effekt, altså en ekte rett linje")
    with c3:
        target = st.slider("Vurder en bolig på (m²)", 60, 750, 700, 10, key="vl_re_tgt")

    size, price, A = _house_data(expo, 0.08, 450, 140, 7)
    grid = np.linspace(45, max(460, target + 20), 300)

    lin = np.polyfit(size, price, 1)
    quad = np.polyfit(size, price, 2)
    lg = np.polyfit(np.log(size), np.log(price), 1)

    def predict(x, which):
        if which == "Rett linje":
            return np.polyval(lin, x)
        if which == "Polynom (kvadratledd)":
            return np.polyval(quad, x)
        return np.exp(np.polyval(lg, np.log(x)))

    fitted = predict(size, model)
    resid = price - fitted

    def r2(y, pred):
        return 1 - ((y - pred) ** 2).sum() / ((y - y.mean()) ** 2).sum()

    pts = pd.DataFrame({"areal": size, "pris": price / 1e6,
                        "per_m2": price / size / 1000, "residual": resid / 1e6,
                        "tilpasset": fitted / 1e6})
    curve = pd.DataFrame({"areal": grid, "pris": predict(grid, model) / 1e6, "hva": "Valgt modell"})
    truth = pd.DataFrame({"areal": grid, "pris": A * grid ** expo / 1e6, "hva": "Sann sammenheng"})
    band = pd.DataFrame({"x": [45, 450]})

    sc = alt.Chart(pts).mark_circle(size=55, opacity=0.5, color=INK_MUTED).encode(
        x=alt.X("areal:Q", title="Areal (m²)"), y=alt.Y("pris:Q", title="Pris (mill. kr)"),
        tooltip=[alt.Tooltip("areal:Q", format=".0f", title="m²"),
                 alt.Tooltip("pris:Q", format=".2f", title="MNOK")])
    lines = alt.Chart(pd.concat([curve, truth])).mark_line(size=2.5).encode(
        x="areal:Q", y="pris:Q",
        color=alt.Color("hva:N", scale=alt.Scale(domain=["Valgt modell", "Sann sammenheng"],
                                                 range=[C_ORANGE, C_BLUE]),
                        legend=alt.Legend(title=None, orient="top")),
        strokeDash=alt.StrokeDash("hva:N", legend=None))
    edge = alt.Chart(band).mark_rule(color=S_WARNING, strokeDash=[5, 4], size=2).encode(x="x:Q")
    st.altair_chart((sc + lines + edge).properties(height=330), use_container_width=True)
    st.caption("De gule strekene markerer hvor dataene slutter. Alt utenfor dem er ekstrapolering.")

    left = alt.Chart(pts).mark_circle(size=55, opacity=0.6, color=C_AQUA).encode(
        x=alt.X("areal:Q", title="Areal (m²)"),
        y=alt.Y("per_m2:Q", title="Pris per m² (tusen kr)"),
        tooltip=[alt.Tooltip("areal:Q", format=".0f"), alt.Tooltip("per_m2:Q", format=".1f")])
    trend = left.transform_regression("areal", "per_m2").mark_line(size=2.5, color=C_BLUE)
    right = alt.Chart(pts).mark_circle(size=55, opacity=0.6, color=C_ORANGE).encode(
        x=alt.X("tilpasset:Q", title="Modellens prediksjon (mill. kr)"),
        y=alt.Y("residual:Q", title="Residual (mill. kr)"),
        tooltip=[alt.Tooltip("tilpasset:Q", format=".2f"), alt.Tooltip("residual:Q", format=".2f")])
    zero = alt.Chart(pd.DataFrame({"y": [0]})).mark_rule(
        color=INK_MUTED, strokeDash=[4, 3], size=2).encode(y="y:Q")
    st.altair_chart(
        ((left + trend).properties(title="Det meglerne la merke til: pris per m² faller", height=250)
         | (right + zero).properties(title="Residualene til valgt modell", height=250)),
        use_container_width=True)

    order = np.argsort(size)
    thirds = np.array_split(resid[order], 3)
    arc = [t.mean() / 1e6 for t in thirds]
    true_at = A * target ** expo
    pred_at = float(predict(np.array([target]), model)[0])

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("R² for valgt modell", f"{r2(price, fitted):.3f}")
    m2.metric("R², rett linje", f"{r2(price, np.polyval(lin, size)):.3f}")
    m3.metric("Residualsnitt: lav / midt / høy", " · ".join(f"{a:+.2f}" for a in arc))
    m4.metric(f"Bom på {target} m²", f"{(pred_at/true_at-1)*100:+.1f} %",
              delta=f"{(pred_at-true_at)/1e6:+.2f} MNOK", delta_color="inverse")

    inside = target <= 450
    if model == "Rett linje":
        _callout(
            f"**Se på de to R²-ene: {r2(price, fitted):.3f} mot {r2(price, np.polyval(lin, size)):.3f}.** "
            f"Den rette linja forklarer nesten like mye av variasjonen som de krumme modellene. "
            f"**R² skiller dem knapt** — og det er derfor R² alene ikke er en modellsjekk.\n\n"
            f"**Residualene skiller dem umiddelbart.** Snittet i lav, midtre og høy tredjedel er "
            f"{arc[0]:+.2f}, {arc[1]:+.2f} og {arc[2]:+.2f} millioner: modellen bommer *nedover* i begge "
            f"ender og *oppover* på midten, hver eneste gang. Det er buen, og den er systematisk, "
            f"ikke tilfeldig.\n\n"
            f"**Og prisen betales i enden.** På {target} m² bommer linja med "
            f"{(pred_at-true_at)/1e6:+.2f} millioner — {(pred_at/true_at-1)*100:+.0f} %. "
            + ("Det er innenfor datagrunnlaget, så feilen er moderat. **Dra arealet forbi 450 m² og se hva som skjer.**"
               if inside else
               "Det er *utenfor* datagrunnlaget: her legger ekstrapolering seg oppå feil modellform, "
               "og en rett linje gjennom en metningskurve overdriver alltid oppover."),
            S_CRITICAL if not inside else S_WARNING,
            "rgba(208,59,59,0.08)" if not inside else "rgba(250,178,25,0.10)")
    else:
        _callout(
            f"**Buen er borte.** Residualsnittene er nå {arc[0]:+.2f}, {arc[1]:+.2f} og {arc[2]:+.2f} "
            f"millioner — ingen systematisk retning igjen, og bommen på {target} m² er nede i "
            f"{(pred_at/true_at-1)*100:+.1f} %.\n\n"
            + ("**Log-log-modellen gjør noe mer:** koeffisienten er en *elastisitet*. "
               f"Her er den {lg[0]:.2f}, altså «10 % større bolig gir omtrent {lg[0]*10:.1f} % høyere pris» — "
               "presis den formuleringen meglerkontoret trenger, og den kommer gratis av transformasjonen."
               if model.startswith("Log") else
               "**Kvadratleddet koster én kolonne** og fanger krumningen. Merk at dette fortsatt er "
               "lineær regresjon: modellen er lineær i *parametrene*, ikke i variablene."),
            S_GOOD, "rgba(12,163,12,0.08)")

    _point(
        "**Hvorfor kurven i det hele tatt oppstår** er en forretningsforklaring, ikke en statistisk: "
        "store boliger ligger oftere utenfor sentrum, og luksusboliger betaler for andre kvaliteter enn "
        "areal. Modellformen bør velges ut fra hva du vet om markedet, ikke bare ut fra hva som passer.\n\n"
        "**Rekkefølgen å svare i på eksamen:** plott dataene og se kurven · bekreft den i residualplottet · "
        "forklar *hvorfor* sammenhengen krummer · velg transformasjon · vis at buen forsvant · og si "
        "eksplisitt hvilket areal-intervall modellen gjelder for."
    )



@st.cache_data(show_spinner=False)
def _endo_data(kind, strength, seed=5, n=600):
    """Two ways to break exogeneity, both with a known true slope of 5.1."""
    rng = np.random.default_rng(seed)
    b1, sx = 5.1, 42.0
    if kind == "Målefeil i x":
        x_true = 100 + sx * rng.normal(size=n)
        y = 3000 + b1 * x_true + rng.normal(0, 150, n)
        x_obs = x_true + rng.normal(0, strength * sx, n)
        return x_obs, y, b1 * (sx ** 2 / (sx ** 2 + (strength * sx) ** 2))
    z = rng.normal(size=n)
    x_obs = 100 + sx * z + rng.normal(0, 20, n)
    y = 3000 + b1 * x_obs + strength * 900 * z + rng.normal(0, 150, n)
    var_x = np.var(x_obs)
    return x_obs, y, b1 + strength * 900 * np.cov(x_obs, z)[0, 1] / var_x


def _endogeneity():
    st.markdown("#### 15 · Forutsetningen residualplottet ikke kan sjekke")
    st.caption(
        "Den sanne sammenhengen er alltid 5,1 her. Se hva estimatet gjør — og se så på residualene, "
        "som ser upåklagelige ut hele veien."
    )
    c1, c2 = st.columns([1.3, 1])
    with c1:
        kind = st.radio("Hvordan brytes forutsetningen?",
                        ["Målefeil i x", "Utelatt konfunder"], key="vl_en_kind", horizontal=True)
    with c2:
        strength = st.slider("Hvor kraftig?", 0.0, 2.0, 1.0, 0.1, key="vl_en_str")

    x, y, expected = _endo_data(kind, strength)
    coef = np.polyfit(x, y, 1)
    fit = np.polyval(coef, x)
    res = y - fit
    corr_res_x = float(np.corrcoef(res, x)[0, 1])

    df = pd.DataFrame({"x": x, "y": y, "tilpasset": fit, "residual": res})
    sc = alt.Chart(df).mark_circle(size=40, opacity=0.4, color=C_BLUE).encode(
        x=alt.X("x:Q", title="Målt x", scale=alt.Scale(zero=False)),
        y=alt.Y("y:Q", title="y", scale=alt.Scale(zero=False)))
    grid = np.linspace(x.min(), x.max(), 100)
    lines = pd.concat([
        pd.DataFrame({"x": grid, "y": np.polyval(coef, grid), "hva": "Modellens linje"}),
        pd.DataFrame({"x": grid, "y": np.mean(y) + 5.1 * (grid - np.mean(x)), "hva": "Sann sammenheng (5,1)"}),
    ])
    ln = alt.Chart(lines).mark_line(size=2.5).encode(
        x="x:Q", y="y:Q",
        color=alt.Color("hva:N", scale=alt.Scale(domain=["Modellens linje", "Sann sammenheng (5,1)"],
                                                 range=[S_CRITICAL, C_BLUE]),
                        legend=alt.Legend(title=None, orient="top")),
        strokeDash=alt.StrokeDash("hva:N", legend=None))
    rp = alt.Chart(df).mark_circle(size=40, opacity=0.4, color=C_AQUA).encode(
        x=alt.X("tilpasset:Q", title="Tilpasset verdi"), y=alt.Y("residual:Q", title="Residual"))
    zero = alt.Chart(pd.DataFrame({"y": [0]})).mark_rule(
        color=INK_MUTED, strokeDash=[4, 3], size=2).encode(y="y:Q")
    st.altair_chart(((sc + ln).properties(title="Data, modellens linje og sannheten", height=290)
                     | (rp + zero).properties(title="Residualene — feilfrie uansett", height=290)),
                    use_container_width=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Sant stigningstall", "5.10")
    m2.metric("Estimert", f"{coef[0]:.2f}", delta=f"{coef[0]-5.1:+.2f}", delta_color="inverse")
    m3.metric("Forventet ut fra teorien", f"{expected:.2f}")
    m4.metric("Korrelasjon residual mot x", f"{corr_res_x:.1e}")

    if strength == 0:
        _callout("**Forutsetningen holder.** Estimatet treffer 5,1, og residualene er formløse. "
                 "Dra i «Hvor kraftig?» og følg med på de to første tallene.", S_GOOD, "rgba(12,163,12,0.08)")
    elif kind == "Målefeil i x":
        _callout(
            f"**Estimatet er trukket mot null: {coef[0]:.2f} mot sanne 5,10.** Det kalles "
            f"**attenuering**, og retningen er forutsigbar — målefeil i en forklaringsvariabel "
            f"underdriver alltid effekten, aldri motsatt.\n\n"
            f"Formelen er kjent: estimatet blir sant stigningstall × σ²ₓ / (σ²ₓ + σ²ᵤ), altså "
            f"{expected:.2f} her, og du ser {coef[0]:.2f}.\n\n"
            f"**Konsekvensen i praksis:** en variabel som er slurvete målt ser uviktig ut. Du kan "
            f"forkaste en ekte driver fordi måleinstrumentet var dårlig, ikke fordi effekten ikke fantes.",
            S_WARNING, "rgba(250,178,25,0.10)")
    else:
        _callout(
            f"**Estimatet er blåst opp: {coef[0]:.2f} mot sanne 5,10.** Den utelatte variabelen "
            f"påvirker både x og y, så modellen tilskriver x alt sammen — den har ingen måte å vite "
            f"at noe annet drev bevegelsen.\n\n"
            f"Her er avviket **{coef[0]/5.1:.1f} ganger** den sanne effekten. Å basere en "
            f"budsjettbeslutning på dette tallet ville bomme like mye.",
            S_CRITICAL, "rgba(208,59,59,0.08)")

    _point(
        f"**Og nå det som gjør denne forutsetningen spesiell — se på det fjerde tallet.** "
        f"Korrelasjonen mellom residualene og x er {corr_res_x:.1e}, altså null. Den er null "
        f"uansett hvor kraftig du drar slideren, fordi minste kvadraters metode **konstruerer** "
        f"residualene til å være ortogonale på forklaringsvariablene. Det er en egenskap ved "
        f"regnestykket, ikke et bevis på at modellen er riktig.\n\n"
        f"**Derfor kan ikke residualplottet avsløre dette bruddet.** Linearitet ser du som en bue, "
        f"heteroskedastisitet som en vifte — men eksogenitet er usynlig i diagnostikken, uansett hvor "
        f"galt estimatet er. Du må argumentere for den fra **designet**: hvordan ble x bestemt, hva "
        f"mer påvirker y, og kan y påvirke x tilbake?\n\n"
        f"Det er også grunnen til at et randomisert forsøk er gullstandarden. Når du *trekker lodd* om "
        f"hvem som får behandlingen, er x uavhengig av alt annet ved konstruksjon — og da holder "
        f"forutsetningen fordi du sørget for det, ikke fordi du håpet på det."
    )



@st.cache_data(show_spinner=False)
def _classsize_data(z_strength, leak, seed=11, n=1200):
    """Class size is driven by unobserved resources, so OLS is biased.

    z is a policy instrument. `leak` is its direct effect on performance, which
    is the exclusion restriction being violated.
    """
    rng = np.random.default_rng(seed)
    resources = rng.normal(size=n)
    z = rng.normal(size=n)
    size = 24 - 3.0 * resources - z_strength * z + rng.normal(0, 1.5, n)
    perf = 70 - 0.8 * size + 4.0 * resources + leak * z + rng.normal(0, 3, n)
    return size, perf, resources, z


def _instrumental_variables():
    st.markdown("#### 16 · Klassestørrelse — og instrumentet som kan gjøre vondt verre")
    st.caption(
        "Leksjonens utdanningscase. Den sanne effekten er **−0,80** poeng per ekstra elev i klassen. "
        "Ressurser påvirker både klassestørrelse og resultat, og er ikke i modellen."
    )
    c1, c2 = st.columns(2)
    with c1:
        z_strength = st.slider("Hvor mye flytter politikken klassestørrelsen?", 0.1, 3.0, 2.0, 0.1,
                               key="vl_iv_z", help="Relevans — første trinn i 2SLS")
    with c2:
        leak = st.slider("Politikkens direkte effekt på resultatet", 0.0, 3.0, 0.0, 0.25,
                         key="vl_iv_leak",
                         help="0 = gyldig instrument. Over 0 er eksklusjonskravet brutt — "
                              "reformen kom med penger også")

    size, perf, res, z = _classsize_data(z_strength, leak)

    def ols(y, *xs):
        X = np.column_stack([np.ones(len(y))] + list(xs))
        return np.linalg.lstsq(X, y, rcond=None)[0]

    naive = ols(perf, size)[1]
    controlled = ols(perf, size, res)[1]
    first = ols(size, z)
    size_hat = first[0] + first[1] * z
    iv = ols(perf, size_hat)[1]
    resid_first = size - size_hat
    se_pi = np.std(resid_first, ddof=2) / np.sqrt(((z - z.mean()) ** 2).sum())
    f_stat = (first[1] / se_pi) ** 2 if se_pi else np.inf

    est = pd.DataFrame({
        "metode": ["Sann effekt", "Naiv regresjon\n(ressurser utelatt)",
                   "Kontrollert for ressurser", "2SLS med instrumentet"],
        "verdi": [-0.8, naive, controlled, iv],
    })
    est["avvik"] = (est["verdi"] - (-0.8)).abs()
    est["status"] = np.where(est["metode"] == "Sann effekt", "Sannheten",
                             np.where(est["avvik"] < 0.15, "Treffer", "Bommer"))
    bars = (
        alt.Chart(est).mark_bar(cornerRadiusEnd=4, size=40)
        .encode(
            y=alt.Y("metode:N", sort=None, title=None),
            x=alt.X("verdi:Q", title="Estimert effekt av én elev mer i klassen"),
            color=alt.Color("status:N", scale=alt.Scale(
                domain=["Sannheten", "Treffer", "Bommer"], range=[INK_MUTED, C_BLUE, S_CRITICAL]),
                legend=alt.Legend(title=None, orient="top")),
            tooltip=[alt.Tooltip("metode:N"), alt.Tooltip("verdi:Q", format="+.3f")],
        ).properties(height=190)
    )
    labs = alt.Chart(est).mark_text(align="right", dx=-8, fontSize=12, color="white").encode(
        y=alt.Y("metode:N", sort=None), x="verdi:Q", text=alt.Text("verdi:Q", format="+.2f"))
    truth = alt.Chart(pd.DataFrame({"x": [-0.8]})).mark_rule(
        color=INK_MUTED, strokeDash=[4, 3], size=2).encode(x="x:Q")
    st.altair_chart(bars + labs + truth, use_container_width=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Naiv regresjon", f"{naive:+.3f}", delta=f"{naive+0.8:+.3f} fra sannheten",
              delta_color="inverse")
    m2.metric("2SLS", f"{iv:+.3f}", delta=f"{iv+0.8:+.3f} fra sannheten", delta_color="inverse")
    m3.metric("Første trinns F", f"{f_stat:,.0f}",
              help="Under ca. 10 er instrumentet svakt")
    m4.metric("Overdriver gevinsten med", f"{abs(naive)/0.8:.2f}×")

    if leak == 0 and f_stat >= 10:
        _callout(
            f"**Instrumentet virker.** Den naive regresjonen sier {naive:+.2f} — den framstiller "
            f"gevinsten av små klasser som **{abs(naive)/0.8:.1f} ganger** så stor som den er, fordi "
            f"velutstyrte skoler både har små klasser og gode resultater.\n\n"
            f"2SLS henter fram {iv:+.2f} **uten å måle ressurser i det hele tatt**. Det er hele "
            f"poenget med et instrument: politikken flytter klassestørrelsen av grunner som ikke har "
            f"noe med den enkelte skolens ressurser å gjøre, så bare den delen av variasjonen brukes.",
            S_GOOD, "rgba(12,163,12,0.08)")
    elif leak > 0:
        worse = abs(iv + 0.8) > abs(naive + 0.8)
        _callout(
            f"**Eksklusjonskravet er brutt, og se hva det gjør.** Reformen påvirker nå resultatet "
            f"også direkte — den kom med penger, ikke bare med mindre klasser.\n\n"
            f"2SLS gir {iv:+.2f} mot sanne −0,80. "
            + (f"**Det er lenger unna sannheten enn den naive regresjonens {naive:+.2f}.** "
               f"Et ugyldig instrument er ikke en delvis reparasjon — det er en ny skjevhet, og den "
               f"kan peke lenger bort enn problemet den skulle løse."
               if worse else
               f"Fortsatt nærmere enn naiv ({naive:+.2f}), men skjevheten er tilbake og vokser med lekkasjen.")
            + f"\n\n**Og dette kan du ikke teste deg ut av** med ett instrument. Eksklusjonskravet "
              f"må begrunnes fra hvordan reformen faktisk virket, ikke fra tallene.",
            S_CRITICAL, "rgba(208,59,59,0.08)")
    else:
        _callout(
            f"**Instrumentet er for svakt.** Første trinns F er {f_stat:,.0f}, og tommelfingerregelen "
            f"er at under 10 duger det ikke. Politikken flytter knapt klassestørrelsen, så det finnes "
            f"nesten ingen ren variasjon å bruke.\n\n"
            f"Et svakt instrument er ikke bare upresist. Estimatet blir **ustabilt**, og det er "
            f"forventningsrett trukket mot den naive regresjonen — altså mot nøyaktig den skjevheten "
            f"du prøvde å unnslippe. Én enkelt kjøring kan derfor lande hvor som helst: her gir 2SLS "
            f"{iv:+.2f} mot naiv {naive:+.2f} og sanne −0,80. Dra styrken sakte oppover og se hvor "
            f"urolig tallet er før F passerer 10.",
            S_WARNING, "rgba(250,178,25,0.10)")

    _point(
        "**Tre ting å ta med videre.**\n\n"
        "**Retningen kan regnes ut på forhånd:** skjevheten er ressurseffekten på resultatet (positiv) "
        "ganger samvariasjonen mellom klassestørrelse og ressurser (negativ), altså negativ — lagt til "
        "en allerede negativ koeffisient blir tallet større i tallverdi. Gevinsten av små klasser "
        "*overdrives*.\n\n"
        "**Rapporter alltid første trinns F.** En IV-analyse uten den er en påstand.\n\n"
        "**Og det beste designet er ikke et instrument i det hele tatt**, men en regel som allerede "
        "finnes: der et tak tvinger et kull på 30 til å deles i to klasser på 15 og 16, er skolene på "
        "hver side av terskelen ellers like. Da flytter klassestørrelsen seg av en grunn som ikke har "
        "noe med elevene eller ressursene å gjøre."
    )



@st.cache_data(show_spinner=False)
def _metrics_junk(k_junk, n=60, seed=9):
    """One real predictor plus k pure-noise ones, so every rise in R2 past the first is fake."""
    rng = np.random.default_rng(seed)
    x1 = rng.normal(size=n)
    y = 2 + 1.5 * x1 + rng.normal(0, 1.2, n)
    junk = rng.normal(size=(n, 15))
    rows = []
    for k in range(1, k_junk + 2):
        cols = [np.ones(n), x1] + ([junk[:, :k - 1]] if k > 1 else [])
        X = np.column_stack(cols)
        coef, *_ = np.linalg.lstsq(X, y, rcond=None)
        res = y - X @ coef
        r2 = 1 - (res ** 2).sum() / ((y - y.mean()) ** 2).sum()
        adj = 1 - (1 - r2) * (n - 1) / (n - k - 1)
        f = (r2 / k) / ((1 - r2) / (n - k - 1))
        rows.append({"prediktorer": k, "R²": r2, "Justert R²": adj, "F": f,
                     "p(F)": float(stats.f.sf(f, k, n - k - 1))})
    return pd.DataFrame(rows)


def _advanced_metrics():
    st.markdown("#### 17 · Justert R², F og standardfeil")
    demo = st.radio("Demonstrasjon", ["R² som belønner deg for å ødelegge modellen",
                                      "Når F og t sier motsatt", "Hva som gjør standardfeilen liten"],
                    key="vl_am_demo")

    if demo.startswith("R²"):
        st.caption("Modellen har **én** ekte prediktor. Alt du legger til etterpå er ren støy.")
        k = st.slider("Hvor mange støyprediktorer legger vi til?", 0, 14, 8, 1, key="vl_am_k")
        df = _metrics_junk(k)
        long = df.melt("prediktorer", ["R²", "Justert R²"], var_name="mål", value_name="verdi")
        chart = alt.Chart(long).mark_line(size=3, point=alt.OverlayMarkDef(size=60, filled=True)).encode(
            x=alt.X("prediktorer:Q", title="Antall prediktorer i modellen"),
            y=alt.Y("verdi:Q", title=None, scale=alt.Scale(zero=False)),
            color=alt.Color("mål:N", scale=alt.Scale(domain=["R²", "Justert R²"],
                                                     range=[S_CRITICAL, C_BLUE]),
                            legend=alt.Legend(title=None, orient="top")),
            tooltip=["prediktorer:Q", "mål:N", alt.Tooltip("verdi:Q", format=".4f")])
        fchart = alt.Chart(df).mark_bar(color=C_ORANGE, cornerRadiusEnd=3, size=18).encode(
            x=alt.X("prediktorer:Q", title="Antall prediktorer"),
            y=alt.Y("F:Q", title="F-statistikk"),
            tooltip=["prediktorer:Q", alt.Tooltip("F:Q", format=".2f"),
                     alt.Tooltip("p(F):Q", format=".5f")])
        st.altair_chart((chart.properties(title="R² mot justert R²", height=270)
                         | fchart.properties(title="F-statistikken", height=270)),
                        use_container_width=True)
        first, last = df.iloc[0], df.iloc[-1]
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("R²", f"{last['R²']:.4f}", delta=f"{last['R²']-first['R²']:+.4f}")
        m2.metric("Justert R²", f"{last['Justert R²']:.4f}",
                  delta=f"{last['Justert R²']-first['Justert R²']:+.4f}")
        m3.metric("F", f"{last['F']:.2f}", delta=f"{last['F']-first['F']:+.1f}", delta_color="normal")
        m4.metric("p(F)", f"{last['p(F)']:.5f}")
        _point(
            f"**R² gikk fra {first['R²']:.3f} til {last['R²']:.3f} på ren støy.** Den kan ikke annet: "
            f"å legge til en variabel gir modellen mer å tilpasse seg med, og den tilpasser seg også "
            f"tilfeldighetene i akkurat disse {60} radene.\n\n"
            f"**Justert R² falt til {last['Justert R²']:.3f}**, fordi straffen (n−1)/(n−k−1) vokser med "
            f"hver prediktor. Og **F kollapset fra {first['F']:.0f} til {last['F']:.1f}** — modellen "
            f"forklarer marginalt mer per prediktor og mye mindre per frihetsgrad.\n\n"
            f"**Derfor sammenlignes modeller med ulikt antall prediktorer på justert R², aldri på R².**"
        )

    elif demo.startswith("Når F"):
        st.caption(
            "To prediktorer som nesten er samme variabel. Modellen vet noe — den kan bare ikke si hvilken "
            "av dem det kom fra."
        )
        corr_jitter = st.select_slider(
            "Hvor like er de to prediktorene?",
            options=[0.60, 0.30, 0.15, 0.08, 0.03], value=0.03,
            format_func=lambda v: {0.60: "ganske ulike", 0.30: "en del overlapp", 0.15: "svært like",
                                   0.08: "nesten identiske", 0.03: "praktisk talt samme variabel"}[v],
            key="vl_am_j")
        n = 40
        rng = np.random.default_rng(4)
        a = rng.normal(size=n)
        bvar = a + rng.normal(0, corr_jitter, n)
        y = 3 + 2 * a + rng.normal(0, 2.0, n)
        X = np.column_stack([np.ones(n), a, bvar])
        coef, *_ = np.linalg.lstsq(X, y, rcond=None)
        res = y - X @ coef
        s2 = (res ** 2).sum() / (n - 3)
        se = np.sqrt(np.diag(np.linalg.inv(X.T @ X)) * s2)
        pv = 2 * stats.t.sf(np.abs(coef / se), n - 3)
        r2 = 1 - (res ** 2).sum() / ((y - y.mean()) ** 2).sum()
        f = (r2 / 2) / ((1 - r2) / (n - 3))
        pf = float(stats.f.sf(f, 2, n - 3))
        r_ab = float(np.corrcoef(a, bvar)[0, 1])
        vif = 1 / (1 - r_ab ** 2)

        tbl = pd.DataFrame({
            "prediktor": ["Prediktor a", "Prediktor b"],
            "koeffisient": coef[1:], "standardfeil": se[1:], "p": pv[1:],
        })
        tbl["signifikant"] = np.where(tbl["p"] < 0.05, "Ja", "Nei")
        bars = alt.Chart(tbl).mark_bar(cornerRadiusEnd=4, size=44).encode(
            y=alt.Y("prediktor:N", title=None, sort=None),
            x=alt.X("koeffisient:Q", title="Koeffisient"),
            color=alt.Color("signifikant:N", scale=alt.Scale(domain=["Ja", "Nei"],
                                                             range=[C_BLUE, S_CRITICAL]),
                            legend=alt.Legend(title="Individuelt signifikant", orient="top")),
            tooltip=[alt.Tooltip("prediktor:N"), alt.Tooltip("koeffisient:Q", format="+.2f"),
                     alt.Tooltip("standardfeil:Q", format=".2f"), alt.Tooltip("p:Q", format=".3f")])
        err = alt.Chart(tbl).mark_rule(size=3, color=INK_MUTED).encode(
            y=alt.Y("prediktor:N", sort=None),
            x=alt.X("lav:Q", title="Koeffisient"), x2="høy:Q"
        ).transform_calculate(lav="datum.koeffisient - 1.96*datum.standardfeil",
                              høy="datum.koeffisient + 1.96*datum.standardfeil")
        zero = alt.Chart(pd.DataFrame({"x": [0]})).mark_rule(
            color=INK_MUTED, strokeDash=[4, 3], size=2).encode(x="x:Q")
        st.altair_chart((bars + err + zero).properties(height=170), use_container_width=True)
        st.caption("De grå strekene er 95 %-intervallene. Den sanne effekten er a = 2,0 og b = 0.")

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("F for modellen", f"{f:,.1f}")
        m2.metric("p(F)", f"{pf:.4f}")
        m3.metric("Laveste p blant prediktorene", f"{pv[1:].min():.3f}")
        m4.metric("VIF", f"{vif:,.0f}")
        if pf < 0.05 and (pv[1:] > 0.05).all():
            _callout(
                f"**Der har du motsetningen.** F sier at modellen er klart signifikant "
                f"(F = {f:,.1f}, p = {pf:.4f}), og **ingen** av prediktorene er individuelt "
                f"signifikante (laveste p = {pv[1:].min():.2f}).\n\n"
                f"Det er ikke en selvmotsigelse — det er signaturen på **multikollinearitet**. "
                f"De to variablene er korrelert {r_ab:.4f}, med VIF på {vif:,.0f}, så modellen kan "
                f"forklare utfallet godt uten å kunne fordele æren mellom dem. Intervallene er så "
                f"brede at begge inneholder null.\n\n"
                f"**Leser du bare F, tror du modellen er god. Leser du bare t-ene, tror du ingenting "
                f"virker. Begge lesningene er feil.**",
                S_CRITICAL, "rgba(208,59,59,0.08)")
        else:
            _point(
                f"Her er prediktorene korrelert {r_ab:.3f} (VIF {vif:,.1f}), og minst én er fortsatt "
                f"individuelt signifikant. **Dra dem nærmere hverandre** og se hva som skjer med "
                f"standardfeilene — koeffisientene blir ustabile lenge før F merker noe.")

    else:
        st.caption("Samme sammenheng, samme n, samme støy. Bare hvor mye x varierer endrer seg.")
        spread = st.slider("Hvor mye varierer x?", 0.3, 4.0, 1.0, 0.1, key="vl_am_sp")
        n = 80
        rng = np.random.default_rng(7)
        x = rng.normal(0, spread, n)
        y = 2 + 1.5 * x + rng.normal(0, 1.2, n)
        b = np.polyfit(x, y, 1)
        res = y - np.polyval(b, x)
        sxx = ((x - x.mean()) ** 2).sum()
        se_b = np.sqrt((res ** 2).sum() / (n - 2) / sxx)
        tc = float(stats.t.ppf(0.975, n - 2))
        lo, hi = b[0] - tc * se_b, b[0] + tc * se_b

        grid = np.linspace(-6, 6, 100)
        band = pd.DataFrame({"x": grid, "lav": np.polyval([lo, b[1]], grid),
                             "høy": np.polyval([hi, b[1]], grid)})
        sc = alt.Chart(pd.DataFrame({"x": x, "y": y})).mark_circle(
            size=70, opacity=0.6, color=C_BLUE).encode(
            x=alt.X("x:Q", title="x", scale=alt.Scale(domain=[-6, 6])),
            y=alt.Y("y:Q", title="y", scale=alt.Scale(domain=[-10, 14])))
        ar = alt.Chart(band).mark_area(opacity=0.25, color=C_ORANGE).encode(
            x="x:Q", y=alt.Y("lav:Q", title="y"), y2="høy:Q")
        ln = alt.Chart(pd.DataFrame({"x": grid, "y": np.polyval(b, grid)})).mark_line(
            size=2.5, color=C_ORANGE).encode(x="x:Q", y="y:Q")
        st.altair_chart((ar + sc + ln).properties(height=320), use_container_width=True)
        st.caption("Det oransje feltet viser hvor linja kan ligge, gitt usikkerheten i stigningstallet.")

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Spredning i x", f"{np.std(x):.2f}")
        m2.metric("Standardfeil på stigningstallet", f"{se_b:.4f}")
        m3.metric("95 % intervall", f"{lo:.2f} – {hi:.2f}")
        m4.metric("t", f"{b[0]/se_b:,.1f}")
        _point(
            f"**Formelen er SE(b₁) = s ÷ √(Σ(x − x̄)²).** Nevneren er spredningen i x, så jo bredere "
            f"x varierer, jo mindre blir standardfeilen — her {se_b:.4f} ved en spredning på "
            f"{np.std(x):.2f}.\n\n"
            f"**Dra spredningen ned mot 0,3.** Punktene klumper seg, vifta åpner seg, og "
            f"stigningstallet blir dårlig bestemt selv om både n og støynivået er uendret. "
            f"To punkter tett sammen bestemmer knapt en linje; to punkter langt fra hverandre "
            f"bestemmer den godt.\n\n"
            f"**Det praktiske:** et designet forsøk varierer behandlingen *bredt* i stedet for å dulte "
            f"borti den. Og et observasjonsdatasett der en driver knapt beveger seg kan ikke fortelle "
            f"deg mye om den driveren, uansett hvor mange rader det har."
        )



@st.cache_data(show_spinner=False)
def _influence_base(seed=8, n=40):
    rng = np.random.default_rng(seed)
    x = np.sort(rng.uniform(10, 90, n))
    y = 100 + 2.5 * x + rng.normal(0, 18, n)
    return x, y


def _influence():
    st.markdown("#### 18 · Uteligger eller innflytelsesrik?")
    st.caption(
        "Et punkt kan være en grell uteligger og likevel ikke flytte linja i det hele tatt. "
        "Dra punktet rundt og se de tre målene bevege seg uavhengig av hverandre."
    )
    preset = st.radio(
        "Prøv en av disse, eller dra selv:",
        ["Ren uteligger (midt i x)", "Høy leverage (men på trenden)", "Innflytelsesrik (begge deler)", "Egen plassering"],
        key="vl_inf_preset", horizontal=False)
    defaults = {"Ren uteligger (midt i x)": (50, 320),
                "Høy leverage (men på trenden)": (150, 475),
                "Innflytelsesrik (begge deler)": (150, 315),
                "Egen plassering": (120, 380)}
    dx, dy = defaults[preset]
    c1, c2 = st.columns(2)
    with c1:
        px = st.slider("Punktets x", 10, 200, dx, 5, key=f"vl_inf_x_{preset}")
    with c2:
        py = st.slider("Punktets y", 50, 700, dy, 5, key=f"vl_inf_y_{preset}")

    x, y = _influence_base()
    # Both fits are kept in the same [intercept, slope] order as the design matrix,
    # so the two lines and the shift below can never be compared across orderings.
    X0 = np.column_stack([np.ones(len(x)), x])
    b_base = np.linalg.lstsq(X0, y, rcond=None)[0]
    xa, ya = np.append(x, px), np.append(y, py)
    X = np.column_stack([np.ones(len(xa)), xa])
    b = np.linalg.lstsq(X, ya, rcond=None)[0]
    r = ya - X @ b
    XtXinv = np.linalg.inv(X.T @ X)
    h = np.einsum("ij,jk,ik->i", X, XtXinv, X)
    s2 = (r ** 2).sum() / (len(xa) - 2)
    cook = (r ** 2 / (2 * s2)) * (h / (1 - h) ** 2)
    std_res = r / np.sqrt(s2)

    grid = np.array([5, 205])
    lines = pd.concat([
        pd.DataFrame({"x": grid, "y": b[0] + b[1] * grid, "linje": "Med punktet"}),
        pd.DataFrame({"x": grid, "y": b_base[0] + b_base[1] * grid, "linje": "Uten punktet"}),
    ])
    pts = pd.DataFrame({"x": x, "y": y})
    one = pd.DataFrame({"x": [px], "y": [py]})
    sc = alt.Chart(pts).mark_circle(size=70, opacity=0.55, color=C_BLUE).encode(
        x=alt.X("x:Q", title="x", scale=alt.Scale(domain=[5, 205])),
        y=alt.Y("y:Q", title="y", scale=alt.Scale(domain=[50, 700])))
    oc = alt.Chart(one).mark_point(size=300, filled=True, color=S_CRITICAL, shape="diamond").encode(
        x="x:Q", y="y:Q",
        tooltip=[alt.Tooltip("x:Q", format=".0f"), alt.Tooltip("y:Q", format=".0f")])
    ln = alt.Chart(lines).mark_line(size=2.5).encode(
        x="x:Q", y="y:Q",
        color=alt.Color("linje:N", scale=alt.Scale(domain=["Med punktet", "Uten punktet"],
                                                   range=[S_CRITICAL, INK_MUTED]),
                        legend=alt.Legend(title=None, orient="top")),
        strokeDash=alt.StrokeDash("linje:N", legend=None))

    cd = pd.DataFrame({"obs": np.arange(1, len(xa) + 1), "cook": cook})
    cd["hvem"] = np.where(cd["obs"] == len(xa), "Punktet du flytter", "De andre")
    cook_chart = alt.Chart(cd).mark_bar(size=6).encode(
        x=alt.X("obs:Q", title="Observasjon"),
        y=alt.Y("cook:Q", title="Cook's distance"),
        color=alt.Color("hvem:N", scale=alt.Scale(domain=["De andre", "Punktet du flytter"],
                                                  range=[C_BLUE, S_CRITICAL]),
                        legend=alt.Legend(title=None, orient="top")),
        tooltip=[alt.Tooltip("obs:Q"), alt.Tooltip("cook:Q", format=".3f")])
    thr = alt.Chart(pd.DataFrame({"y": [1.0, 4 / len(xa)],
                                  "hva": ["D = 1 (kursets regel)", "D = 4/n"]})).mark_rule(
        strokeDash=[4, 3], size=2, color=S_WARNING).encode(y="y:Q", tooltip="hva:N")
    # Altair shares colour scales across a concatenation by default, which would let the
    # line chart's two colours claim the bar chart's legend and repaint the bars.
    st.altair_chart(((sc + ln + oc).properties(title="Dataene og de to linjene", height=300)
                     | (cook_chart + thr).properties(title="Cook's distance per observasjon", height=300)
                     ).resolve_scale(color="independent"),
                    use_container_width=True)

    shift = b[1] - b_base[1]
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Standardisert residual", f"{std_res[-1]:+.2f}")
    m2.metric("Leverage (h)", f"{h[-1]:.3f}")
    m3.metric("Cook's D", f"{cook[-1]:.2f}")
    m4.metric("Endring i stigningstall", f"{shift:+.3f}",
              delta=f"{shift/b_base[1]*100:+.1f} %", delta_color="inverse")

    big_res, big_lev = abs(std_res[-1]) > 2, h[-1] > 4 / len(xa)
    if big_res and big_lev:
        _callout(
            f"**Innflytelsesrik.** Punktet er uvanlig i *begge* retninger — standardisert residual "
            f"{std_res[-1]:+.2f} og leverage {h[-1]:.3f} — og Cook's D på {cook[-1]:.2f} sier hvor mye "
            f"det betyr. Stigningstallet flyttet seg {shift:+.3f}, altså "
            f"**{abs(shift/b_base[1])*100:.0f} %**, av ett punkt av {len(xa)}.\n\n"
            f"Dette er punktet som fortjener en undersøkelse — og undersøkelsen kommer *før* enhver "
            f"beslutning om å fjerne det.", S_CRITICAL, "rgba(208,59,59,0.08)")
    elif big_res:
        _callout(
            f"**Uteligger, men ikke innflytelsesrik.** Standardisert residual er {std_res[-1]:+.2f}, "
            f"altså grelt — og leverage er bare {h[-1]:.3f}, fordi punktet ligger midt i x-området "
            f"der det er masse andre punkter som holder linja på plass.\n\n"
            f"**Stigningstallet flyttet seg {shift:+.3f}.** Praktisk talt ingenting. Det er kursets "
            f"poeng i tall: en uteligger påvirker ikke nødvendigvis resultatet.", S_WARNING,
            "rgba(250,178,25,0.10)")
    elif big_lev:
        _callout(
            f"**Høy leverage, men ufarlig.** Punktet ligger langt ute i x (leverage {h[-1]:.3f}), så det "
            f"*kunne* dominert linja — men det ligger på trenden, med en residual på bare "
            f"{std_res[-1]:+.2f}. Cook's D er {cook[-1]:.2f}.\n\n"
            f"**Stigningstallet flyttet seg {shift:+.3f}.** Leverage er en *mulighet* for innflytelse, "
            f"ikke innflytelse i seg selv. Dra punktet opp eller ned og se hva som skjer.",
            S_GOOD, "rgba(12,163,12,0.08)")
    else:
        _callout(
            f"**Helt ordinært punkt.** Residual {std_res[-1]:+.2f}, leverage {h[-1]:.3f}, "
            f"Cook's D {cook[-1]:.2f}. Ingenting å se her.", S_GOOD, "rgba(12,163,12,0.08)")

    _point(
        "**De tre målene svarer på tre forskjellige spørsmål.** Den standardiserte residualen spør "
        "om punktet er uvanlig i **y** — bommer modellen på det? Leverage spør om det er uvanlig i "
        "**x** — ligger det langt fra tyngdepunktet? Og Cook's D ganger dem sammen, så den blir stor "
        "bare når *begge* er det.\n\n"
        "**Prøv de tre forhåndsvalgene etter hverandre.** En standardisert residual på 3,75 flytter "
        "linja med 0,03. Høy leverage alene flytter den med 0,05. Begge sammen flytter den med 0,66 — "
        "en firedel av hele effekten, fra ett punkt.\n\n"
        "**Og terskelen som er mest nyttig i praksis** er ikke D > 1 eller D > 4/n, men *«vesentlig "
        "større enn naboene»*. Se på søylediagrammet til høyre: et punkt som stikker opp fra flokken "
        "er verdt å undersøke selv om det ligger under begge de formelle grensene."
    )



B_SIZE, B_ROOMS = 140_000.0, 1_400_000.0   # true direct effects, NOK
ROOMS_PER_M2 = 0.036                       # a 28 m2 room, roughly


def _kr(v):
    """Norwegian thousands separator, applied to one number rather than a whole
    sentence - a blanket replace would also swallow the commas in the prose."""
    return f"{v:,.0f}".replace(",", "\u00a0")


@st.cache_data(show_spinner=False)
def _collinear_draw(corr, n, seed):
    """Alpha Estates listings where the correlation between size and rooms is dialled in.

    rooms = ROOMS_PER_M2 * size + noise, and the noise sd is solved from the target
    correlation so the *indirect path* stays fixed at ROOMS_PER_M2 while only the
    overlap changes. That keeps the omitted-variable identity comparable across the
    slider instead of moving two things at once.
    """
    rng = np.random.default_rng(seed)
    size = rng.normal(95, 30, n).clip(35, 250)
    sd_signal = ROOMS_PER_M2 * size.std(ddof=0)
    corr = min(max(corr, 0.01), 0.995)
    sd_noise = sd_signal * np.sqrt(1 / corr ** 2 - 1)
    rooms = 1.0 + ROOMS_PER_M2 * size + rng.normal(0, sd_noise, n)
    price = B_SIZE * size + B_ROOMS * rooms + rng.normal(0, 1_600_000, n)
    return size, rooms, price


def _fit(X, y):
    b = np.linalg.lstsq(X, y, rcond=None)[0]
    r = y - X @ b
    n, k = X.shape
    s2 = (r ** 2).sum() / (n - k)
    se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
    return b, se


@st.cache_data(show_spinner=False)
def _mc_draws(corr, n, reps=300):
    """Sampling distribution of the size coefficient, with and without rooms.

    These are fresh datasets rather than bootstrap resamples of one. A bootstrap
    would centre on the estimate this particular sample happened to produce, which
    at high correlation can sit far from the truth - and the whole point of the
    picture is that collinearity widens the distribution without moving it.
    """
    out = np.empty((reps, 2))
    for i in range(reps):
        size, rooms, price = _collinear_draw(corr, n, 5000 + i)
        ones = np.ones(n)
        out[i, 0] = _fit(np.column_stack([ones, size, rooms]), price)[0][1]
        out[i, 1] = _fit(np.column_stack([ones, size]), price)[0][1]
    return out


def _multicollinearity():
    st.markdown("#### 19 · Multikollinearitet og VIF")
    st.caption(
        "Alpha Estates-caset. To prediktorer som overlapper — boligstørrelse og antall rom — "
        "og spørsmålet caset svarer feil på: skal du kaste den ene?"
    )
    c1, c2 = st.columns(2)
    with c1:
        corr = st.slider("Korrelasjon mellom størrelse og antall rom", 0.30, 0.98, 0.95, 0.01,
                         key="vl_mc_corr")
    with c2:
        n = st.select_slider("Antall boliger i utvalget", [60, 120, 240, 420, 800], value=420,
                             key="vl_mc_n")

    size, rooms, price = _collinear_draw(corr, n, 11)
    ones = np.ones(n)
    XA = np.column_stack([ones, size, rooms])
    XB = np.column_stack([ones, size])
    bA, seA = _fit(XA, price)
    bB, seB = _fit(XB, price)
    r_obs = float(np.corrcoef(size, rooms)[0, 1])
    v = 1 / (1 - r_obs ** 2)

    m = st.columns(4)
    m[0].metric("VIF", f"{v:.2f}", help="1 / (1 − R²) fra hjelperegresjonen av den ene prediktoren på den andre")
    m[1].metric("Standardfeil blåses opp", f"{np.sqrt(v):.2f}×")
    m[2].metric("t for størrelse (begge med)", f"{bA[1]/seA[1]:.2f}")
    m[3].metric("t for antall rom", f"{bA[2]/seA[2]:.2f}")

    draws = _mc_draws(corr, n)
    aux = np.linalg.lstsq(np.column_stack([ones, size]), rooms, rcond=None)[0][1]
    total = B_SIZE + aux * B_ROOMS

    lo = min(draws.min(), B_SIZE, total) - 12_000
    hi = max(draws.max(), B_SIZE, total) + 12_000
    edges = np.linspace(lo, hi, 46)
    ctr = (edges[:-1] + edges[1:]) / 2
    hist = pd.concat([
        pd.DataFrame({"b": ctr, "antall": np.histogram(draws[:, 0], edges)[0],
                      "modell": "Begge prediktorer"}),
        pd.DataFrame({"b": ctr, "antall": np.histogram(draws[:, 1], edges)[0],
                      "modell": "Antall rom kastet"}),
    ])
    bars = alt.Chart(hist).mark_area(opacity=0.5, interpolate="step").encode(
        x=alt.X("b:Q", title="Estimert kroner per m²", axis=alt.Axis(format=",.0f")),
        y=alt.Y("antall:Q", title="Antall utvalg", stack=None),
        color=alt.Color("modell:N",
                        scale=alt.Scale(domain=["Begge prediktorer", "Antall rom kastet"],
                                        range=[C_BLUE, C_ORANGE]),
                        legend=alt.Legend(title=None, orient="top")))
    # The two truth lines are labelled with text on the chart rather than through a
    # second colour legend: Altair would otherwise merge the two colour scales and
    # print one truncated four-entry legend for what are two different things.
    truth = pd.DataFrame({
        "v": [B_SIZE, total],
        "hva": ["Sann direkte effekt\n(rom holdt fast)", "Sann total effekt\n(direkte + indirekte)"],
        "farge": [INK_MUTED, S_CRITICAL],
    })
    rules = alt.Chart(truth).mark_rule(size=2, strokeDash=[5, 3]).encode(
        x="v:Q", color=alt.Color("farge:N", scale=None),
        tooltip=[alt.Tooltip("hva:N", title="Sannhet"), alt.Tooltip("v:Q", format=",.0f")])
    labels = alt.Chart(truth).mark_text(
        align="left", dx=5, dy=-4, baseline="top", fontSize=11, lineBreak="\n",
    ).encode(x="v:Q", y=alt.value(2), text="hva:N", color=alt.Color("farge:N", scale=None))
    st.altair_chart((bars + rules + labels).resolve_scale(color="independent").properties(
        height=CHART_H, title="Hvor estimatet lander over 300 nye utvalg"),
        use_container_width=True)

    t1, t2 = st.columns(2)
    with t1:
        st.markdown("**Med begge prediktorer**")
        st.dataframe(pd.DataFrame({
            "Ledd": ["Størrelse (kr/m²)", "Antall rom (kr)"],
            "Estimat": [_kr(bA[1]), _kr(bA[2])],
            "Standardfeil": [_kr(seA[1]), _kr(seA[2])],
            "t": [f"{bA[1]/seA[1]:.2f}", f"{bA[2]/seA[2]:.2f}"],
        }), hide_index=True, use_container_width=True)
    with t2:
        st.markdown("**Antall rom kastet**")
        st.dataframe(pd.DataFrame({
            "Ledd": ["Størrelse (kr/m²)"],
            "Estimat": [_kr(bB[1])],
            "Standardfeil": [_kr(seB[1])],
            "t": [f"{bB[1]/seB[1]:.2f}"],
        }), hide_index=True, use_container_width=True)

    _callout(
        f"**Identiteten, regnet ut på dette utvalget.** Hjelperegresjonen sier at hver ekstra "
        f"kvadratmeter kommer med **{aux:.4f}** rom. Da er\n\n"
        f"| | |\n|---|---|\n"
        f"| Direkte effekt av størrelse, rom holdt fast | {_kr(bA[1])} kr/m² |\n"
        f"| Indirekte: {aux:.4f} × {_kr(bA[2])} kr | + {_kr(aux*bA[2])} kr/m² |\n"
        f"| **Sum** | **{_kr(bA[1] + aux*bA[2])} kr/m²** |\n"
        f"| Størrelseskoeffisienten når rom er kastet | **{_kr(bB[1])} kr/m²** |\n\n"
        f"De to siste radene er samme tall. Det er ikke omtrentlig — det er en algebraisk "
        f"identitet, og den er nøyaktig formelen for utelatt-variabel-skjevhet.",
        C_ORANGE, "rgba(235,104,52,0.07)")

    if np.sqrt(v) > 2.2:
        _callout(
            f"**Høy VIF ({v:.1f}) — og legg merke til hva den gjør og ikke gjør.** Den blå "
            f"fordelingen er bred: standardfeilen er {np.sqrt(v):.2f} ganger større enn den "
            f"hadde vært uten overlapp. Men den er **sentrert på riktig sted**. Den oransje er "
            f"smalere og sentrert et helt annet sted.\n\n"
            f"Multikollinearitet gir upresise estimater. Å kaste variabelen gir presise estimater "
            f"av noe annet. Det første er en ulempe du kan rapportere; det andre er en feil "
            f"leseren ikke kan se.\n\n"
            f"Dra slideren helt ned til 0,30 og se at avstanden mellom fordelingene ikke "
            f"endrer seg. VIF og skjevhet er uavhengige.", S_WARNING, "rgba(250,178,25,0.10)")
    else:
        _callout(
            f"**Lav VIF ({v:.1f}) — og se hva som *ikke* forsvant.** Prediktorene overlapper lite "
            f"og standardfeilen er bare {np.sqrt(v):.2f} ganger oppblåst, så den blå fordelingen "
            f"er smal. Men avstanden mellom de to fordelingene er like stor som før.\n\n"
            f"Det er poenget denne slideren er bygget for å vise: **VIF og utelatt-variabel-"
            f"skjevhet er to uavhengige ting.** Slideren endrer bare hvor mye støy det er i "
            f"antall rom, ikke hvor mange rom en kvadratmeter fører med seg — den indirekte "
            f"veien er {aux:.4f} × {_kr(bA[2])} kr uansett hvor slideren står. Så selv uten "
            f"antydning til kollinearitet koster det å kaste variabelen "
            f"**{_kr(aux*bA[2])} kr/m²** i skjevhet. Kollinearitet gjør estimatet upresist; "
            f"å kaste en variabel gjør det skjevt. De to problemene har ingenting med hverandre "
            f"å gjøre.", S_GOOD, "rgba(12,163,12,0.08)")

    _point(
        "**Tre ting å ta med til eksamen.**\n\n"
        "**1. VIF måler overlapp, ikke feil.** Den forteller deg hvor mye av denne prediktoren "
        "som allerede ligger i de andre — og den eneste skaden er √VIF ganger bredere "
        "standardfeil. Koeffisientene er fortsatt forventningsrette.\n\n"
        "**2. Er begge signifikante, har kollineariteten allerede tapt.** Symptomet den advarer "
        "mot er at du *ikke finner* effekter som er der. Fant du dem likevel — med den "
        "oppblåste standardfeilen inkludert — er det ingenting å reparere.\n\n"
        "**3. Kast bare når du ikke skal tolke koeffisienten.** Skru på n-slideren: flere "
        "boliger gjør den blå fordelingen smalere uten å flytte den, mens den oransje "
        "blir smalere rundt feil sted. Mer data løser multikollinearitet. Ingen "
        "datamengde reparerer en utelatt variabel."
    )



# --------------------------------------------------------------------------
# F. Distributions and five-point summaries
# --------------------------------------------------------------------------

@st.cache_data(show_spinner=False)
def _trial_draw(speedup, consistency, n, seed):
    """Placebo and drug recovery times.

    speedup is multiplicative, consistency scales the log-scale spread. Keeping
    those two on separate sliders is the whole point: the case's 'tighter IQR'
    appears from the first alone, with the second untouched.
    """
    rng = np.random.default_rng(seed)
    placebo = np.exp(rng.normal(np.log(20), 0.42, n))
    drug = np.exp(rng.normal(np.log(20 * (1 - speedup)), 0.42 * consistency, n))
    return placebo, drug


# Sampling sd of the change in (IQR / median) under a pure shift, measured over
# 4000 simulated trials per arm size. The ratio diagnostic is itself noisy, so the
# verdict below is judged against this band rather than an arbitrary cutoff.
_RATIO_SD = {10: 0.752, 20: 0.458, 40: 0.293, 80: 0.204, 200: 0.127, 600: 0.072}


def _five(x):
    return dict(zip(["min", "Q1", "median", "Q3", "maks"],
                    [np.min(x), np.quantile(x, .25), np.median(x),
                     np.quantile(x, .75), np.max(x)]))


def _five_point():
    st.markdown("#### 20 · Fempunktsoppsummering og IQR-fellen")
    st.caption(
        "PharmaCorp-caset. Legemiddelet gjør pasientene raskere friske — og IQR-en blir "
        "strammere. Spørsmålet er om det betyr «jevnere resultater», eller bare er regning."
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        speed = st.slider("Hvor mye raskere (multiplikativt)", 0, 50, 25, 5,
                          format="%d %%", key="vl_fp_speed") / 100
    with c2:
        cons = st.slider("Endring i spredning (log-skala)", 0.50, 1.50, 1.00, 0.05,
                         key="vl_fp_cons",
                         help="1,00 = uendret konsistens. Under 1 = genuint jevnere. "
                              "Over 1 = mer uforutsigbart.")
    with c3:
        n = st.select_slider("Pasienter per arm", [10, 20, 40, 80, 200, 600], value=600,
                             key="vl_fp_n")

    placebo, drug = _trial_draw(speed, cons, n, 31)
    long = pd.concat([pd.DataFrame({"dager": placebo, "gruppe": "Placebo"}),
                      pd.DataFrame({"dager": drug, "gruppe": "Legemiddel"})])
    box = alt.Chart(long).mark_boxplot(size=48, extent=1.5).encode(
        y=alt.Y("gruppe:N", title=None, sort=["Placebo", "Legemiddel"]),
        x=alt.X("dager:Q", title="Restitusjonstid (dager)"),
        color=alt.Color("gruppe:N", scale=alt.Scale(domain=["Placebo", "Legemiddel"],
                                                    range=[INK_MUTED, C_AQUA]),
                        legend=None))
    st.altair_chart(box.properties(height=170, title="Fempunktsoppsummeringen som boksplott"),
                    use_container_width=True)

    fp, fd = _five(placebo), _five(drug)
    iqr_p, iqr_d = fp["Q3"] - fp["Q1"], fd["Q3"] - fd["Q1"]
    rp, rd = iqr_p / fp["median"], iqr_d / fd["median"]

    st.dataframe(pd.DataFrame({
        "Gruppe": ["Placebo", "Legemiddel"],
        "Min": [f"{fp['min']:.1f}", f"{fd['min']:.1f}"],
        "Q1": [f"{fp['Q1']:.1f}", f"{fd['Q1']:.1f}"],
        "Median": [f"{fp['median']:.1f}", f"{fd['median']:.1f}"],
        "Q3": [f"{fp['Q3']:.1f}", f"{fd['Q3']:.1f}"],
        "Maks": [f"{fp['maks']:.1f}", f"{fd['maks']:.1f}"],
        "IQR": [f"{iqr_p:.2f}", f"{iqr_d:.2f}"],
        "IQR / median": [f"{rp:.4f}", f"{rd:.4f}"],
    }), hide_index=True, use_container_width=True)

    m = st.columns(4)
    m[0].metric("Median kortere med", f"{fp['median'] - fd['median']:.1f} dager")
    m[1].metric("IQR strammere med", f"{(1 - iqr_d / iqr_p) * 100:.1f} %")
    m[2].metric("IQR / median endret", f"{(rd / rp - 1) * 100:+.1f} %")
    u = stats.mannwhitneyu(placebo, drug, alternative="two-sided")
    m[3].metric("Mann–Whitney p", f"{u.pvalue:.4g}")

    change = rd / rp - 1
    band = 1.96 * _RATIO_SD[n]
    tighter = iqr_d < iqr_p * 0.98
    if abs(change) <= band:
        _callout(
            f"**Dette er nøyaktig fellen i caset.** IQR-en er **{(1-iqr_d/iqr_p)*100:.1f} % "
            f"strammere** — det ser ut som jevnere resultater. Men IQR delt på medianen "
            f"endret seg {change*100:+.1f} %, og med {n} pasienter per arm svinger det tallet "
            f"±{band*100:.0f} % av rene tilfeldigheter. **Endringen er ikke til å skille fra "
            f"null.**\n\n"
            f"Spredningen krympet i takt med medianen, fordi restitusjonstid har et gulv på "
            f"null og effekten er multiplikativ. «Strammere IQR» og «kortere median» er ikke "
            f"to funn her — det er ett funn rapportert to ganger.",
            S_WARNING, "rgba(250,178,25,0.10)")
    elif change < -band:
        _callout(
            f"**Her er det et ekte konsistensfunn.** IQR er {(1-iqr_d/iqr_p)*100:.1f} % "
            f"strammere, og — det avgjørende — IQR delt på medianen falt **{-change*100:.1f} %**, "
            f"godt utenfor støybåndet på ±{band*100:.0f} % ved {n} pasienter per arm. "
            f"Spredningen krympet *mer* enn forskyvningen alene forklarer.\n\n"
            f"Dette er påstanden PharmaCorp gjør. Den kan være sann — men den krever denne "
            f"utregningen, ikke bare en IQR-sammenligning.", S_GOOD, "rgba(12,163,12,0.08)")
    else:
        _callout(
            f"**Legg merke til hva som skjer nå.** Medianen er fortsatt kortere, men IQR delt "
            f"på medianen **steg {change*100:.1f} %**, utenfor støybåndet på ±{band*100:.0f} %. "
            f"Legemiddelet gjør forløpet **mindre forutsigbart**, selv om det gjør det "
            f"kortere.\n\n"
            f"En leser som bare får «IQR-en er strammere enn placebo» kan ikke skille dette "
            f"fra tilfellet over — begge har strammere IQR. Det er derfor forholdstallet må "
            f"rapporteres.", S_CRITICAL, "rgba(208,59,59,0.08)")

    if not tighter and speed < 0.05:
        _callout(
            f"**Ingen forskyvning å snakke om.** Median {fp['median']:.1f} mot "
            f"{fd['median']:.1f} dager. Skru opp «hvor mye raskere» og se hva som skjer med "
            f"IQR-en helt uten at du rører konsistens-slideren.", C_BLUE)

    if n <= 20:
        _callout(
            f"**Og med bare {n} pasienter per arm:** Mann–Whitney gir p = {u.pvalue:.3f}. "
            f"Dra n-slideren opp og ned med alt annet fast, og se hvor mye boksene og "
            f"p-verdien hopper. Caset oppgir «fem dager kortere» uten å si hvor mange "
            f"pasienter det gjelder — og med n = 10 bommer en ekte femdagerseffekt sju "
            f"ganger av ti.", S_CRITICAL, "rgba(208,59,59,0.08)")

    _point(
        "**Diagnosen som skiller de to, og den er én divisjon.** Under en ren multiplikativ "
        "effekt skalerer IQR med nøyaktig samme faktor som medianen. Så sammenlign "
        "**IQR ÷ median** mellom gruppene: uendret betyr forskyvning, lavere betyr ekte "
        "jevnere forløp.\n\n"
        "**Hvorfor det skjer.** Restitusjonstid kan ikke bli negativ og har en lang høyrehale. "
        "En behandling som virker, virker prosentvis — og da krymper ethvert *absolutt* "
        "spredningsmål av seg selv. Samme sak gjelder lønn, priser, omsetning og ventetid.\n\n"
        "**Men diagnosen trenger data.** Forholdstallet er selv et estimat, og det er "
        "støyende: ved 40 pasienter per arm svinger det ±57 % av seg selv, ved 200 ±25 %, "
        "og først ved 600 er båndet nede i ±14 %. Med et lite forsøk kan du altså ikke "
        "avgjøre spørsmålet i det hele tatt — noe caset heller ikke forsøker.\n\n"
        "**Og det boksplottet ikke viser.** Antall pasienter, om fordelingen har to topper, "
        "og om noen fortsatt ikke var friske da studien ble avsluttet. Fempunktsoppsummeringen "
        "er en *beskrivelse*. Den er riktig verktøy for å få øye på en hypotese, og aldri "
        "bevis for den."
    )


SECTIONS = {
    "A · Utvalg og usikkerhet": [_sampling_distribution, _coverage, _bias_vs_noise],
    "B · Test og effektstørrelse": [_p_vs_d, _power, _multiple_comparisons],
    "C · Regresjon og residualer": [_leverage, _residuals, _real_estate, _omitted_variable, _confounding, _endogeneity, _instrumental_variables, _influence, _multicollinearity],
    "D · Z-score og overtilpasning": [_zscore, _overfitting, _advanced_metrics],
    "F · Fordelinger og oppsummering": [_five_point],
    "E · Eksamensdrill": [_drill],
}

_INTRO = {
    "A · Utvalg og usikkerhet": "Hvorfor et utvalg kan si noe om en populasjon, hva de 95 prosentene faktisk lover, og hvorfor mer data ikke redder et skjevt utvalg.",
    "B · Test og effektstørrelse": "Hvorfor en p-verdi og en effektstørrelse svarer på to forskjellige spørsmål, hva styrke er, og hvordan tjue sammenligninger produserer et funn av ingenting.",
    "C · Regresjon og residualer": "Hvordan én observasjon kan vri hele linja, hva strukturen i et residualplott betyr, eiendomscaset der en rett linje er nesten riktig, hvorfor en koeffisient endrer seg når en variabel til kommer inn, sammenhengen som snur fortegn når du deler opp dataene, hva endogenitet gjør med estimatet og hva en instrumentvariabel redder — forskjellen på en uteligger og et punkt som faktisk flytter linja, og til slutt hva VIF egentlig måler.",
    "D · Z-score og overtilpasning": "Z-scoren brukt begge veier, hvorfor et høyt R² kan bety at modellen er blitt verre, og hva justert R², F og standardfeilen faktisk forteller.",
    "F · Fordelinger og oppsummering": "Fempunktsoppsummeringen fra PharmaCorp-caset, og hvorfor en strammere IQR som regel er regning framfor et funn.",
    "E · Eksamensdrill": "Oppgavetypene fra aktivitetene, med nye tall hver gang og tilbakemelding på hvert steg underveis.",
}


def render_visual_lab():
    from visual_lab_kpi import INTRO_11, SECTIONS_11

    st.title("🔬 Visual Lab")
    st.markdown(
        "Simulatorer for **EVO modul 1**. Leksjonene forklarer dette i tekst og tabeller; her kan du "
        "dra i det. Hver graf står med poenget sitt under, så et skjermbilde er verdt noe alene."
    )
    lesson = st.radio(
        "Leksjon",
        ["1.1 — KPI-er, dashbord og beslutninger", "1.2 — Statistisk inferens"],
        horizontal=True, key="vl_lesson",
    )
    groups, intros = ((SECTIONS_11, INTRO_11) if lesson.startswith("1.1") else (SECTIONS, _INTRO))
    st.divider()

    own = "📂 Egne data"
    tabs = st.tabs(list(groups.keys()) + [own])
    for tab, (name, fns) in zip(tabs, groups.items()):
        with tab:
            st.caption(intros[name])
            for i, fn in enumerate(fns):
                if i:
                    st.divider()
                fn()
    with tabs[-1]:
        st.caption(
            "Last opp din egen CSV eller Excel-fil og kjør de samme analysene på den — "
            "beskrivende statistikk, konfidensintervall, gruppesammenligning og regresjon med "
            "residualdiagnostikk."
        )
        from visual_lab_data import render_own_data
        render_own_data()
