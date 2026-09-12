"""Bring your own data into the Visual Lab.

The simulators elsewhere run on generated data so the true answer is known. This
module runs the same analyses on the reader's own file, which is the step that
turns a demonstration into a tool they can use on an assignment.

Two practical things it handles that otherwise stop people:

* Norwegian Excel writes CSV with ';' as the separator and ',' as the decimal
  mark. Pandas' defaults read that as one text column, so the separator and
  decimal mark are sniffed rather than assumed.
* Real columns have blanks, thousands separators and stray spaces. Numeric
  coercion is explicit and reports how many rows it dropped, instead of failing
  silently or throwing.
"""

import io
import re

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from scipy import stats

from visual_lab import (
    C_AQUA, C_BLUE, C_ORANGE, INK_MUTED, S_CRITICAL, S_GOOD, S_WARNING,
    _callout, _point,
)

MAX_ROWS = 200_000


# --------------------------------------------------------------------------
# Loading
# --------------------------------------------------------------------------

def _sniff_csv(raw: bytes):
    """Guess separator and decimal mark from the first few lines."""
    head = raw[:8000].decode("utf-8", errors="replace")
    first = head.splitlines()[0] if head.splitlines() else ""
    sep = max([",", ";", "\t", "|"], key=first.count)
    if first.count(sep) == 0:
        sep = ","
    body = "\n".join(head.splitlines()[1:6])
    # A comma decimal only makes sense when the comma is not the separator.
    decimal = "," if sep != "," and re.search(r"\d,\d", body) else "."
    return sep, decimal


@st.cache_data(show_spinner=False)
def _read_upload(name: str, raw: bytes):
    if name.lower().endswith((".xlsx", ".xlsm", ".xls")):
        return pd.read_excel(io.BytesIO(raw)), "Excel"
    sep, decimal = _sniff_csv(raw)
    df = pd.read_csv(io.BytesIO(raw), sep=sep, decimal=decimal, engine="python")
    if df.shape[1] == 1 and sep != ";":
        df = pd.read_csv(io.BytesIO(raw), sep=";", decimal=",", engine="python")
        sep, decimal = ";", ","
    label = f"CSV (skilletegn «{sep}», desimal «{decimal}»)"
    return df, label


# A dot is only treated as a thousands separator when that reading is unambiguous:
# either a comma is present and is doing the decimal job (1.234,56), or there are
# at least two dot-groups (1.234.567). A single group like "1.234" or "0.123" is
# genuinely ambiguous, and the decimal reading is the safer default - stripping
# the dot there would silently turn 0.123 into 123.
_THOUSANDS_ONLY = re.compile(r"^-?\d{1,3}(\.\d{3}){2,}$")


def _to_numeric(series):
    """Coerce a column to numbers, tolerating spaces and thousands separators."""
    if pd.api.types.is_numeric_dtype(series):
        return pd.to_numeric(series, errors="coerce")

    def one(value):
        if value is None or (isinstance(value, float) and np.isnan(value)):
            return np.nan
        text = str(value).strip()
        for ch in ("\u00a0", "\u202f", " "):
            text = text.replace(ch, "")
        if not text:
            return np.nan
        if "," in text:
            # The comma is the decimal mark, so any remaining dots are thousands.
            text = text.replace(".", "").replace(",", ".")
        elif _THOUSANDS_ONLY.match(text):
            text = text.replace(".", "")
        try:
            return float(text)
        except ValueError:
            return np.nan

    return series.map(one).astype(float)


def _numeric_cols(df):
    out = []
    for c in df.columns:
        v = _to_numeric(df[c])
        if v.notna().sum() >= max(3, 0.5 * len(df)):
            out.append(c)
    return out


_EXAMPLE = """maaned;segment;annonse_knok;rabatt_pct;omsetning_knok;tilfredshet
2024-01;D2C;72;6,5;1402;7,8
2024-02;D2C;95;8,0;1580;7,4
2024-03;D2C;61;5,5;1288;8,1
2024-04;D2C;120;9,5;1811;7,0
2024-05;D2C;84;7,0;1495;7,6
2024-06;D2C;140;11,0;1902;6,8
2024-07;D2C;55;5,0;1204;8,3
2024-08;D2C;103;8,5;1666;7,2
2024-09;D2C;78;6,5;1440;7,9
2024-10;D2C;131;10,5;1858;6,9
2024-11;D2C;168;12,5;2240;6,5
2024-12;D2C;152;11,5;2098;6,7
2024-01;B2B;40;3,0;980;8,4
2024-02;B2B;52;4,0;1105;8,0
2024-03;B2B;35;2,5;918;8,6
2024-04;B2B;66;5,0;1240;7,7
2024-05;B2B;48;3,5;1062;8,2
2024-06;B2B;74;5,5;1318;7,5
2024-07;B2B;31;2,0;872;8,8
2024-08;B2B;58;4,5;1164;7,9
2024-09;B2B;44;3,5;1020;8,3
2024-10;B2B;69;5,0;1277;7,6
2024-11;B2B;88;6,5;1452;7,2
2024-12;B2B;80;6,0;1385;7,4
"""


def _loader():
    st.markdown("#### Last inn dine egne data")
    st.caption(
        "CSV eller Excel. Norsk Excel skriver CSV med semikolon og komma som desimaltegn — "
        "det oppdages automatisk, du trenger ikke gjøre om noe."
    )
    c1, c2 = st.columns([2, 1])
    with c1:
        up = st.file_uploader("Slipp en fil her", type=["csv", "txt", "xlsx", "xlsm", "xls"],
                              key="vd_file", label_visibility="collapsed")
    with c2:
        st.download_button("⬇️ Last ned eksempelfil", _EXAMPLE.encode("utf-8"),
                           file_name="visual_lab_eksempeldata.csv", mime="text/csv",
                           use_container_width=True, key="vd_dl")
        use_example = st.toggle("Bruk eksempeldata", value=up is None, key="vd_ex")

    df, source = None, ""
    if up is not None and not use_example:
        try:
            df, source = _read_upload(up.name, up.getvalue())
            source = f"{up.name} · {source}"
        except Exception as exc:
            st.error(f"Klarte ikke lese filen: {type(exc).__name__} — {exc}")
            return None, ""
    elif use_example:
        df, source = pd.read_csv(io.StringIO(_EXAMPLE), sep=";", decimal=","), "Eksempeldata (Nordtre AS)"

    if df is None:
        st.info("Last opp en fil, eller slå på eksempeldata for å se hvordan verktøyene virker.")
        return None, ""
    if len(df) > MAX_ROWS:
        st.warning(f"Filen har {len(df):,} rader. Bruker de første {MAX_ROWS:,}.")
        df = df.head(MAX_ROWS)

    st.success(f"Lest inn **{len(df):,} rader × {df.shape[1]} kolonner** fra {source}")
    with st.expander("Se dataene og kolonnetypene", expanded=False):
        st.dataframe(df.head(30), use_container_width=True)
        info = pd.DataFrame({
            "Kolonne": df.columns,
            "Type": [("tall" if c in _numeric_cols(df) else "tekst/kategori") for c in df.columns],
            "Manglende": [int(df[c].isna().sum()) for c in df.columns],
            "Unike verdier": [int(df[c].nunique()) for c in df.columns],
        })
        st.dataframe(info, hide_index=True, use_container_width=True)
    return df, source


# --------------------------------------------------------------------------
# Tools
# --------------------------------------------------------------------------

def _clean(df, col):
    v = _to_numeric(df[col])
    dropped = int(v.isna().sum())
    return v.dropna().to_numpy(), dropped


def _dropped_note(dropped, col):
    if dropped:
        st.caption(f"⚠️ {dropped} rad(er) i «{col}» kunne ikke leses som tall og er utelatt.")


def _tool_describe(df, nums):
    col = st.selectbox("Kolonne", nums, key="vd_d_col")
    v, dropped = _clean(df, col)
    _dropped_note(dropped, col)
    if len(v) < 3:
        st.warning("For få tallverdier i denne kolonnen."); return

    q1, med, q3 = np.percentile(v, [25, 50, 75])
    iqr = q3 - q1
    skew = float(stats.skew(v))
    src = pd.DataFrame({"verdi": v})
    hist = alt.Chart(src).mark_bar(color=C_BLUE, cornerRadiusTopLeft=3, cornerRadiusTopRight=3).encode(
        x=alt.X("verdi:Q", bin=alt.Bin(maxbins=40), title=col),
        y=alt.Y("count()", title="Antall"))
    rules = alt.Chart(pd.DataFrame({"x": [v.mean(), med], "hva": ["Gjennomsnitt", "Median"]})).mark_rule(
        size=2.5).encode(x="x:Q", color=alt.Color("hva:N", scale=alt.Scale(
            domain=["Gjennomsnitt", "Median"], range=[C_ORANGE, C_AQUA]),
            legend=alt.Legend(title=None, orient="top")))
    st.altair_chart((hist + rules).properties(height=280), use_container_width=True)

    m = st.columns(6)
    for col_, (lab, val) in zip(m, [("n", f"{len(v):,}"), ("Gjennomsnitt", f"{v.mean():,.2f}"),
                                    ("Median", f"{med:,.2f}"), ("Std.avvik", f"{v.std(ddof=1):,.2f}"),
                                    ("IQR", f"{iqr:,.2f}"), ("Skjevhet", f"{skew:+.2f}")]):
        col_.metric(lab, val)

    fences = (q1 - 1.5 * iqr, q3 + 1.5 * iqr)
    n_out = int(((v < fences[0]) | (v > fences[1])).sum())
    z = (v - v.mean()) / v.std(ddof=1)
    n_z = int((np.abs(z) > 3).sum())
    if abs(skew) > 1:
        _callout(
            f"**Fordelingen er tydelig skjev (skjevhet {skew:+.2f}), og gjennomsnittet ligger "
            f"{'over' if v.mean() > med else 'under'} medianen.** På skjeve data er gjennomsnittet "
            f"trukket av halen, så medianen beskriver «en typisk verdi» bedre.\n\n"
            f"Det har to følger for resten av verktøyene: et t-intervall underdekker litt ved lite n "
            f"(se simulator 2), og **z-score-grensene mistolker vanlige verdier som ekstreme** — "
            f"her flagger IQR-gjerdene {n_out} punkter mot z-testens {n_z}. Bruk IQR på slike data.",
            S_WARNING, "rgba(250,178,25,0.10)")
    else:
        _point(
            f"Fordelingen er noenlunde symmetrisk (skjevhet {skew:+.2f}), så gjennomsnitt og median "
            f"ligger nær hverandre og z-baserte grenser er brukbare. "
            f"IQR-gjerdene flagger {n_out} punkter, |z| > 3 flagger {n_z}.")


def _tool_ci(df, nums):
    col = st.selectbox("Kolonne", nums, key="vd_ci_col")
    level = st.select_slider("Konfidensnivå", [0.80, 0.90, 0.95, 0.99], value=0.95,
                             format_func=lambda v: f"{v:.0%}", key="vd_ci_lvl")
    v, dropped = _clean(df, col)
    _dropped_note(dropped, col)
    if len(v) < 3:
        st.warning("For få tallverdier."); return

    n = len(v)
    mean, sd = v.mean(), v.std(ddof=1)
    se = sd / np.sqrt(n)
    tc = float(stats.t.ppf(1 - (1 - level) / 2, n - 1))
    lo, hi = mean - tc * se, mean + tc * se
    band = pd.DataFrame({"lav": [lo], "høy": [hi], "snitt": [mean], "y": [0]})
    rule = alt.Chart(band).mark_rule(size=6, color=C_BLUE, strokeCap="round").encode(
        x=alt.X("lav:Q", title=col, scale=alt.Scale(zero=False)), x2="høy:Q", y=alt.Y("y:Q", axis=None))
    dot = alt.Chart(band).mark_point(size=180, filled=True, color=C_ORANGE).encode(x="snitt:Q", y="y:Q")
    st.altair_chart((rule + dot).properties(height=110), use_container_width=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Gjennomsnitt", f"{mean:,.3f}")
    m2.metric("Standardfeil", f"{se:,.3f}")
    m3.metric(f"{level:.0%} intervall", f"{lo:,.2f} – {hi:,.2f}")
    m4.metric("Bredde", f"{hi-lo:,.3f}")
    need = int(np.ceil((tc * sd / ((hi - lo) / 4)) ** 2)) if hi > lo else 0
    _point(
        f"**Tolkning:** hvis denne målingen ble gjentatt mange ganger og et intervall regnet ut på samme "
        f"måte hver gang, ville omtrent {level:.0%} av dem inneholde den sanne populasjonsverdien. "
        f"Dette ene intervallet inneholder den eller ikke.\n\n"
        f"**Bredden er {hi-lo:,.2f}.** Å halvere den ville krevd omtrent **{need:,} observasjoner** "
        f"i stedet for {n:,} — bredden krymper med √n.\n\n"
        f"**Og det intervallet ikke dekker:** frafall, dekning og hvordan utvalget ble trukket. "
        f"Det kvantifiserer bare tilfeldig utvalgsvariasjon."
    )


def _tool_groups(df, nums):
    cats = [c for c in df.columns if df[c].nunique() >= 2 and df[c].nunique() <= 40]
    if not cats:
        st.warning("Fant ingen kolonne med mellom 2 og 40 grupper å dele på."); return
    c1, c2 = st.columns(2)
    with c1:
        gcol = st.selectbox("Grupperingskolonne", cats, key="vd_g_g")
    with c2:
        vcol = st.selectbox("Måltall", nums, key="vd_g_v")

    work = df[[gcol, vcol]].copy()
    work[vcol] = _to_numeric(work[vcol])
    work = work.dropna()
    levels = list(work[gcol].astype(str).unique())
    if len(levels) < 2:
        st.warning("Trenger minst to grupper med data."); return
    pick = st.multiselect("Sammenlign to grupper", levels, default=levels[:2], max_selections=2,
                          key="vd_g_pick")
    if len(pick) != 2:
        st.info("Velg nøyaktig to grupper."); return

    a = work.loc[work[gcol].astype(str) == pick[0], vcol].to_numpy()
    b = work.loc[work[gcol].astype(str) == pick[1], vcol].to_numpy()
    if min(len(a), len(b)) < 3:
        st.warning("Trenger minst tre observasjoner i hver gruppe."); return

    box = alt.Chart(work[work[gcol].astype(str).isin(pick)]).mark_boxplot(size=48, extent="min-max").encode(
        x=alt.X(f"{gcol}:N", title=None), y=alt.Y(f"{vcol}:Q", title=vcol, scale=alt.Scale(zero=False)),
        color=alt.Color(f"{gcol}:N", scale=alt.Scale(domain=pick, range=[C_BLUE, C_ORANGE]), legend=None))
    pts = alt.Chart(work[work[gcol].astype(str).isin(pick)]).mark_circle(
        size=45, opacity=0.45, color=INK_MUTED, xOffset=26).encode(
        x=alt.X(f"{gcol}:N"), y=alt.Y(f"{vcol}:Q"),
        tooltip=[alt.Tooltip(f"{gcol}:N"), alt.Tooltip(f"{vcol}:Q", format=",.2f")])
    st.altair_chart((box + pts).properties(height=300), use_container_width=True)

    n1, n2 = len(a), len(b)
    sp = np.sqrt(((n1 - 1) * a.var(ddof=1) + (n2 - 1) * b.var(ddof=1)) / (n1 + n2 - 2))
    se = sp * np.sqrt(1 / n1 + 1 / n2)
    diff = a.mean() - b.mean()
    t = diff / se if se else np.nan
    dfree = n1 + n2 - 2
    p = float(2 * stats.t.sf(abs(t), dfree))
    d = diff / sp if sp else np.nan
    tc = float(stats.t.ppf(0.975, dfree))
    lo, hi = diff - tc * se, diff + tc * se

    m = st.columns(6)
    for col_, (lab, val) in zip(m, [("Forskjell", f"{diff:,.3f}"), ("t", f"{t:,.3f}"),
                                    ("p (tosidig)", f"{p:.4f}"), ("Cohen's d", f"{d:,.3f}"),
                                    ("95 % KI", f"{lo:,.2f} – {hi:,.2f}"),
                                    ("n", f"{n1} mot {n2}")]):
        col_.metric(lab, val)

    sig, big = p < 0.05, abs(d) >= 0.5
    cells = {
        (True, True): ("✅ Signifikant + stor effekt", "Handle, og oppgi størrelsen.", S_GOOD),
        (True, False): ("⚠️ Signifikant + liten effekt", "Ekte, men marginal. Avgjør på kost/nytte.", S_WARNING),
        (False, False): ("➖ Ikke signifikant + liten effekt", "Uinformativt: kan være ingen effekt, kan være for lite utvalg.", INK_MUTED),
        (False, True): ("🚨 Ikke signifikant + stor effekt", "Nesten alltid for lite utvalg. Ikke rapporter som «ingen forskjell».", S_CRITICAL),
    }
    title, body, colour = cells[(sig, big)]
    _callout(f"**{title}**\n\n{body}\n\nForskjellen mellom **{pick[0]}** og **{pick[1]}** er "
             f"{diff:,.2f}, med et 95 %-intervall fra {lo:,.2f} til {hi:,.2f}. "
             f"{'Intervallet utelukker null, i tråd med testen.' if lo*hi > 0 else 'Intervallet inneholder null, i tråd med testen.'}",
             colour, "rgba(0,0,0,0.03)")
    _point(
        "**Før du stoler på dette:** ble de to gruppene dannet av deg (et eksperiment) eller fantes de "
        "allerede (observasjonsdata)? Bare det første støtter en årsakspåstand. Og hvis du har prøvd "
        "flere grupperinger eller flere måltall før du landet på denne, gjelder multippel testing — "
        "se simulator 6."
    )


def _tool_regression(df, nums):
    if len(nums) < 2:
        st.warning("Trenger minst to tallkolonner."); return
    c1, c2, c3 = st.columns(3)
    with c1:
        xcol = st.selectbox("Forklaringsvariabel (x)", nums, key="vd_r_x")
    with c2:
        ycol = st.selectbox("Utfall (y)", [c for c in nums if c != xcol], key="vd_r_y")
    with c3:
        model = st.radio("Modell", ["Rett linje", "Kvadratledd", "Log-log"], key="vd_r_m")

    work = pd.DataFrame({"x": _to_numeric(df[xcol]), "y": _to_numeric(df[ycol])}).dropna()
    if model == "Log-log":
        work = work[(work["x"] > 0) & (work["y"] > 0)]
        if work.empty:
            st.warning("Log-log krever positive verdier i begge kolonner."); return
    if len(work) < 5:
        st.warning("Trenger minst fem komplette rader."); return
    x, y = work["x"].to_numpy(), work["y"].to_numpy()

    if model == "Rett linje":
        coef = np.polyfit(x, y, 1); fit = np.polyval(coef, x); k = 1
        eq = f"y = {coef[1]:,.3f} + {coef[0]:,.4f}·x"
    elif model == "Kvadratledd":
        coef = np.polyfit(x, y, 2); fit = np.polyval(coef, x); k = 2
        eq = f"y = {coef[2]:,.3f} + {coef[1]:,.4f}·x + {coef[0]:,.6f}·x²"
    else:
        coef = np.polyfit(np.log(x), np.log(y), 1); fit = np.exp(np.polyval(coef, np.log(x))); k = 1
        eq = f"ln(y) = {coef[1]:,.3f} + {coef[0]:,.4f}·ln(x)   →   elastisitet {coef[0]:.3f}"

    res = y - fit
    n = len(x)
    r2 = 1 - (res ** 2).sum() / ((y - y.mean()) ** 2).sum()
    adj = 1 - (1 - r2) * (n - 1) / (n - k - 1)
    sxx = ((x - x.mean()) ** 2).sum()
    se_slope = np.sqrt((res ** 2).sum() / (n - k - 1) / sxx) if sxx else np.nan
    slope = coef[0]
    t_slope = slope / se_slope if se_slope else np.nan
    p_slope = float(2 * stats.t.sf(abs(t_slope), n - k - 1)) if se_slope else np.nan

    grid = np.linspace(x.min(), x.max(), 200)
    if model == "Rett linje":
        gy = np.polyval(coef, grid)
    elif model == "Kvadratledd":
        gy = np.polyval(coef, grid)
    else:
        gy = np.exp(np.polyval(coef, np.log(grid)))
    sc = alt.Chart(work).mark_circle(size=70, opacity=0.6, color=C_BLUE).encode(
        x=alt.X("x:Q", title=xcol, scale=alt.Scale(zero=False)),
        y=alt.Y("y:Q", title=ycol, scale=alt.Scale(zero=False)),
        tooltip=[alt.Tooltip("x:Q", format=",.2f"), alt.Tooltip("y:Q", format=",.2f")])
    ln = alt.Chart(pd.DataFrame({"x": grid, "y": gy})).mark_line(size=2.5, color=C_ORANGE).encode(
        x="x:Q", y="y:Q")
    rd = pd.DataFrame({"tilpasset": fit, "residual": res})
    rd["std"] = res / res.std(ddof=1) if res.std(ddof=1) else 0
    rd["flagg"] = np.where(np.abs(rd["std"]) > 2, "Utenfor ±2", "Innenfor")
    rp = alt.Chart(rd).mark_circle(size=70, opacity=0.7).encode(
        x=alt.X("tilpasset:Q", title="Tilpasset verdi"), y=alt.Y("residual:Q", title="Residual"),
        color=alt.Color("flagg:N", scale=alt.Scale(domain=["Innenfor", "Utenfor ±2"],
                                                   range=[C_BLUE, S_CRITICAL]),
                        legend=alt.Legend(title=None, orient="top")),
        tooltip=[alt.Tooltip("residual:Q", format=",.3f"), alt.Tooltip("std:Q", format=".2f")])
    zero = alt.Chart(pd.DataFrame({"y": [0]})).mark_rule(
        color=INK_MUTED, strokeDash=[4, 3], size=2).encode(y="y:Q")
    st.altair_chart(((sc + ln).properties(title="Data og tilpasset modell", height=280)
                     | (rp + zero).properties(title="Residualer mot tilpasset", height=280)),
                    use_container_width=True)

    st.code(eq, language=None)
    m = st.columns(5)
    for col_, (lab, val) in zip(m, [("n", f"{n:,}"), ("R²", f"{r2:.4f}"), ("Justert R²", f"{adj:.4f}"),
                                    ("p for stigningstall", f"{p_slope:.4f}" if p_slope == p_slope else "—"),
                                    ("Residual std.avvik", f"{res.std(ddof=1):,.3f}")]):
        col_.metric(lab, val)

    # Diagnose the residual shape: curvature and fanning, measured rather than eyeballed.
    order = np.argsort(fit)
    thirds = np.array_split(res[order], 3)
    arc = [float(t.mean()) for t in thirds]
    curved = (arc[1] - (arc[0] + arc[2]) / 2)
    spread = [float(t.std(ddof=1)) for t in thirds if len(t) > 1]
    fanning = max(spread) / min(spread) if len(spread) == 3 and min(spread) > 0 else 1.0
    scale = res.std(ddof=1) or 1.0

    notes = []
    if abs(curved) > 0.35 * scale:
        notes.append(
            f"**Bue i residualene.** Snittet i lav, midtre og høy tredjedel er {arc[0]:+,.2f}, "
            f"{arc[1]:+,.2f} og {arc[2]:+,.2f} — modellen bommer systematisk i samme retning innenfor "
            f"hvert område. Lineæritetsforutsetningen holder ikke. Prøv **Kvadratledd** eller **Log-log**.")
    if fanning > 2.2:
        notes.append(
            f"**Vifteform.** Spredningen i residualene er {fanning:.1f} ganger større i den ene enden "
            f"enn i den andre — heteroskedastisitet. Koeffisientene er fortsatt brukbare, men "
            f"**standardfeilene, og dermed p-verdien over, er det ikke.** Log-transformer utfallet, "
            f"eller bruk robuste standardfeil.")
    if int((np.abs(rd['std']) > 3).sum()):
        notes.append(
            f"**{int((np.abs(rd['std']) > 3).sum())} observasjon(er) utenfor ±3 standardiserte residualer.** "
            f"Undersøk dem før du gjør noe: feilregistrering rettes, en annen populasjon ekskluderes "
            f"etter en regel du skriver ned, og en manglende variabel legges til — men punktet slettes ikke "
            f"bare fordi det er stort.")
    if notes:
        _callout("\n\n".join(notes), S_WARNING, "rgba(250,178,25,0.10)")
    else:
        _callout(
            f"**Ingen tydelig struktur i residualene.** Ingen bue, ingen vifte, ingen ekstreme punkter. "
            f"Modellformen ser dekkende ut for disse dataene.", S_GOOD, "rgba(12,163,12,0.08)")

    _point(
        f"**R² på {r2:.3f} sier hvor mye av variasjonen modellen forklarer på *disse* radene.** "
        f"Det sier ingenting om hvordan den treffer på nye data — bytt til en mer fleksibel modell og "
        f"se R² stige uansett (simulator 12 viser hvorfor det er en felle).\n\n"
        f"**Og det viktigste:** et stigningstall er ikke en årsakssammenheng. Spør hva mer som skiller "
        f"observasjonene, og om den variabelen henger sammen både med {xcol} og {ycol}."
    )


TOOLS = {
    "Beskriv en kolonne": _tool_describe,
    "Konfidensintervall": _tool_ci,
    "Sammenlign to grupper": _tool_groups,
    "Regresjon og residualer": _tool_regression,
}


def render_own_data():
    st.markdown("#### Test metodene på dine egne tall")
    st.caption(
        "Simulatorene ellers kjører på genererte data, der fasiten er kjent. Her kjører de samme "
        "analysene på din egen fil — samme utregninger, samme diagnostikk, samme forbehold."
    )
    df, _ = _loader()
    if df is None:
        return
    nums = _numeric_cols(df)
    if not nums:
        st.error(
            "Fant ingen kolonner som kan leses som tall. Sjekk at desimaltegnet er konsekvent, "
            "og at det ikke ligger tekst som «i.a.» eller «-» i tallkolonnene.")
        return
    st.divider()
    tool = st.radio("Verktøy", list(TOOLS), horizontal=True, key="vd_tool")
    st.divider()
    TOOLS[tool](df, nums)
