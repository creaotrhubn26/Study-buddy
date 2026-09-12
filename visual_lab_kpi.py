"""Interactive simulators for EVO lesson 1.1 - KPIs, dashboards and decisions.

Lesson 1.1 argues that a KPI is a proxy, that a number without its partner is
uninterpretable, and that a threshold is a decision people stop re-examining.
Those are claims you can be shown rather than told, so each simulator here puts
the reader in the position of the person reading the dashboard.

The running business is Nordtre AS, the same fictional firm used throughout the
activities, so the figures connect to the written solutions.

Shares the validated palette with visual_lab.
"""

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from visual_lab import (
    C_AQUA, C_BLUE, C_ORANGE, INK_MUTED, S_CRITICAL, S_GOOD, S_WARNING,
    _callout, _point, _seed_control,
)


# --------------------------------------------------------------------------
# A. KPIs and the money
# --------------------------------------------------------------------------

def _cac_ltv():
    st.markdown("#### 1 · CAC alene betyr ingenting")
    st.caption(
        "Aktivitet 1.1.1 sitt hovedfunn: markedsføringen halverte anskaffelseskostnaden og "
        "kalte kvartalet en suksess. Se hva som mangler."
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        cac_now = st.slider("CAC i år (kr)", 20, 600, 126, 2, key="vk_a1_cac")
    with c2:
        ltv_now = st.slider("LTV i år (kr)", 100, 4000, 1735, 5, key="vk_a1_ltv")
    with c3:
        margin = st.slider("Dekningsgrad på LTV", 0.1, 1.0, 0.45, 0.05, key="vk_a1_m",
                           help="LTV bygget på omsetning overvurderer hver kunde. Bruk dekningsbidrag.")

    cac_last, ltv_last = 176.0, 1728.0
    ratio_now = ltv_now / cac_now
    ratio_gross = ltv_now * margin / cac_now
    ratio_last = ltv_last / cac_last
    payback_mo = cac_now / (ltv_now * margin / 24) if ltv_now else 0

    df = pd.DataFrame({
        "periode": ["I fjor", "I fjor", "I år", "I år"],
        "mål": ["CAC", "LTV", "CAC", "LTV"],
        "verdi": [cac_last, ltv_last, cac_now, ltv_now],
    })
    chart = (
        alt.Chart(df).mark_bar(cornerRadiusEnd=4)
        .encode(
            x=alt.X("periode:N", title=None, axis=alt.Axis(labelAngle=0)),
            y=alt.Y("verdi:Q", title="Kroner"),
            color=alt.Color("mål:N", scale=alt.Scale(domain=["CAC", "LTV"], range=[C_ORANGE, C_BLUE]),
                            legend=alt.Legend(title=None, orient="top")),
            xOffset="mål:N",
            tooltip=[alt.Tooltip("periode:N"), alt.Tooltip("mål:N"), alt.Tooltip("verdi:Q", format=",.0f")],
        ).properties(height=240)
    )
    labels = alt.Chart(df).mark_text(dy=-8, fontSize=12, color=INK_MUTED).encode(
        x=alt.X("periode:N"), xOffset="mål:N", y="verdi:Q", text=alt.Text("verdi:Q", format=",.0f"))
    st.altair_chart(chart + labels, use_container_width=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("CAC-endring", f"{(cac_now/cac_last-1)*100:+.1f} %")
    m2.metric("LTV-endring", f"{(ltv_now/ltv_last-1)*100:+.1f} %")
    m3.metric("LTV:CAC nå", f"{ratio_now:.1f}×", delta=f"{ratio_now-ratio_last:+.1f} mot i fjor")
    m4.metric("På dekningsbidrag", f"{ratio_gross:.1f}×")

    if ratio_now > ratio_last * 1.02:
        verdict, colour = ("Ekte effektivisering", S_GOOD)
        why = ("CAC falt **og** forholdet til LTV ble bedre. Kundene du kjøper er verdt minst like mye "
               "som før. Dette er den gode nyheten markedsføringen tror de har.")
    elif ratio_now < ratio_last * 0.98:
        verdict, colour = ("Billigere kunder, ikke bedre markedsføring", S_CRITICAL)
        why = ("CAC falt, men LTV falt mer. Kampanjen har flyttet seg mot **billigere kunder som er verdt "
               "mindre**. Det er motsatt konklusjon av den rapporten trekker — fra nøyaktig samme CAC-tall.")
    else:
        verdict, colour = ("Uavgjort — og det er poenget", S_WARNING)
        why = ("CAC og LTV beveget seg omtrent likt, så forholdet står stille. Hele endringen i CAC "
               "forteller deg ingenting alene.")
    _callout(f"**{verdict}.** {why}", colour, "rgba(0,0,0,0.03)")

    _point(
        f"**Dra LTV ned mot 1 200 og la CAC stå.** CAC ser fortsatt like bra ut, og forholdet kollapser. "
        f"Det er derfor CAC uten LTV er utolkbart — nøyaktig samme tall støtter to motsatte konklusjoner.\n\n"
        f"**Og legg merke til dekningsgrad-slideren.** LTV bygget på *omsetning* i stedet for "
        f"dekningsbidrag overvurderer hver eneste kunde: her går forholdet fra {ratio_now:.1f}× til "
        f"{ratio_gross:.1f}× når du regner på det du faktisk sitter igjen med. "
        f"Tilbakebetaling per kunde: **{payback_mo:.1f} måneder**."
    )


def _blended_cac_mix():
    st.markdown("#### 2 · Den samlede CAC-en som falt uten at noe ble billigere")
    st.caption(
        "Nordtre kjøper to slags kunder: D2C billig, B2B dyrt. Den rapporterte CAC-en er et vektet "
        "snitt — så den beveger seg når *fordelingen* endrer seg, selv om ingen av segmentene gjør det."
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        cac_d2c = st.slider("CAC, D2C (kr)", 40, 400, 100, 5, key="vk_a1b_d")
    with c2:
        cac_b2b = st.slider("CAC, B2B (kr)", 1000, 12000, 5000, 100, key="vk_a1b_b")
    with c3:
        share = st.slider("Andel D2C-kunder", 0.70, 0.995, 0.95, 0.005, key="vk_a1b_s", format="%.1f%%")

    base_share = 0.95
    blended = share * cac_d2c + (1 - share) * cac_b2b
    base_blended = base_share * cac_d2c + (1 - base_share) * cac_b2b
    grid = np.linspace(0.70, 0.995, 60)
    df = pd.DataFrame({"andel": grid, "blended": grid * cac_d2c + (1 - grid) * cac_b2b})

    line = alt.Chart(df).mark_line(size=3, color=C_BLUE).encode(
        x=alt.X("andel:Q", title="Andel D2C-kunder", axis=alt.Axis(format="%")),
        y=alt.Y("blended:Q", title="Rapportert samlet CAC (kr)"),
        tooltip=[alt.Tooltip("andel:Q", format=".1%"), alt.Tooltip("blended:Q", format=",.0f")])
    now = alt.Chart(pd.DataFrame({"x": [share], "y": [blended]})).mark_point(
        size=200, filled=True, color=S_CRITICAL).encode(x="x:Q", y="y:Q")
    was = alt.Chart(pd.DataFrame({"x": [base_share], "y": [base_blended]})).mark_point(
        size=140, filled=True, color=INK_MUTED, shape="diamond").encode(x="x:Q", y="y:Q")
    st.altair_chart((line + was + now).properties(height=280), use_container_width=True)

    m1, m2, m3 = st.columns(3)
    m1.metric("Samlet CAC nå", f"{blended:,.0f} kr")
    m2.metric("Ved 95 % D2C", f"{base_blended:,.0f} kr")
    m3.metric("Tilsynelatende endring", f"{(blended/base_blended-1)*100:+.1f} %")
    _point(
        f"**Ingen av de to segmentenes CAC har endret seg** — de står på {cac_d2c:,} og {cac_b2b:,} kroner "
        f"uansett hvor du drar miksen. Likevel «faller» den rapporterte CAC-en med "
        f"{abs(min(0,(blended/base_blended-1)*100)):.0f} % når andelen D2C stiger.\n\n"
        f"**Dette er hele forklaringen på funnet i aktivitet 1.1.1.** En samlet CAC som faller kan bety "
        f"at markedsføringen ble bedre, eller at miksen forskjøv seg mot den billige kundetypen — som "
        f"også er den minst verdifulle. Første spørsmål til en fallende CAC er derfor ikke «hvorfor?» "
        f"men **«er den brutt ned per segment?»**\n\n"
        f"Et vektet snitt uten vektene er ikke et måltall, det er en oppsummering av to ting du ikke får se."
    )


def _margin_waterfall():
    st.markdown("#### 3 · Hvilken margin snakker du om?")
    st.caption("Tre marginer, samme omsetning, tre helt ulike tall. Aktivitet 1.1.1 spurte hvilken du mente.")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        rev = st.slider("Omsetning (mill. kr)", 5.0, 40.0, 18.4, 0.1, key="vk_a2_rev")
    with c2:
        cogs_pct = st.slider("Varekost", 0.20, 0.80, 0.55, 0.01, key="vk_a2_cogs", format="%.0f%%")
    with c3:
        opex_pct = st.slider("Driftskostnader", 0.05, 0.60, 0.35, 0.01, key="vk_a2_opex", format="%.0f%%")
    with c4:
        tax_pct = st.slider("Skatt og finans", 0.0, 0.50, 0.22, 0.01, key="vk_a2_tax", format="%.0f%%")

    gross = rev * (1 - cogs_pct)
    oper = gross - rev * opex_pct
    net = oper * (1 - tax_pct)
    steps = pd.DataFrame({
        "trinn": ["Omsetning", "Bruttoresultat", "Driftsresultat", "Resultat etter skatt"],
        "verdi": [rev, gross, oper, net],
        "margin": [1.0, gross / rev, oper / rev, net / rev],
    })
    bars = (
        alt.Chart(steps).mark_bar(cornerRadiusEnd=4, size=46)
        .encode(
            y=alt.Y("trinn:N", sort=None, title=None),
            x=alt.X("verdi:Q", title="Millioner kroner"),
            color=alt.value(C_BLUE),
            tooltip=[alt.Tooltip("trinn:N"), alt.Tooltip("verdi:Q", format=",.2f"),
                     alt.Tooltip("margin:Q", format=".1%")],
        ).properties(height=210)
    )
    lab = alt.Chart(steps).mark_text(align="left", dx=8, fontSize=13, color=INK_MUTED).encode(
        y=alt.Y("trinn:N", sort=None), x="verdi:Q",
        text=alt.Text("margin:Q", format=".1%"))
    st.altair_chart(bars + lab, use_container_width=True)

    m1, m2, m3 = st.columns(3)
    m1.metric("Bruttomargin", f"{gross/rev:.1%}")
    m2.metric("Driftsmargin", f"{oper/rev:.1%}")
    m3.metric("Nettomargin", f"{net/rev:.1%}")
    _point(
        f"**«Marginen vår er {gross/rev:.0%}» og «marginen vår er {net/rev:.1%}» kan begge være sanne "
        f"om samme selskap i samme kvartal.** Forskjellen er ikke regnefeil, den er hvilken kostnadslinje "
        f"du har trukket fra.\n\n"
        f"I en eksamensbesvarelse er dette et gratispoeng: **si hvilken margin du mener, hver gang.** "
        f"Og når noen presenterer en margin uten å si hvilken, er første spørsmål hva som er trukket fra."
    )


def _roi_horizon():
    st.markdown("#### 4 · ROI-en som snur når du endrer horisonten")
    st.caption("Samme prosjekt, samme kontantstrøm. Bare rapporteringsvinduet endrer seg.")
    c1, c2, c3 = st.columns(3)
    with c1:
        invest = st.slider("Investering (tusen kr)", 100, 3000, 1200, 50, key="vk_a3_inv")
    with c2:
        year1 = st.slider("Avkastning år 1 (tusen kr)", 0, 1500, 312, 6, key="vk_a3_y1")
    with c3:
        decay = st.slider("Årlig endring i avkastning", -0.6, 0.6, -0.25, 0.05, key="vk_a3_dec",
                          format="%.0f%%")

    years = np.arange(1, 9)
    flows = year1 * (1 + decay) ** (years - 1)
    cum = np.cumsum(flows) - invest
    df = pd.DataFrame({"år": years, "kumulativt": cum, "årlig": flows})
    df["status"] = np.where(df["kumulativt"] >= 0, "I pluss", "Fortsatt i minus")

    bars = alt.Chart(df).mark_bar(cornerRadiusEnd=3, size=30).encode(
        x=alt.X("år:O", title="År", axis=alt.Axis(labelAngle=0)),
        y=alt.Y("kumulativt:Q", title="Kumulativt resultat (tusen kr)"),
        color=alt.Color("status:N", scale=alt.Scale(domain=["Fortsatt i minus", "I pluss"],
                                                    range=[S_CRITICAL, C_BLUE]),
                        legend=alt.Legend(title=None, orient="top")),
        tooltip=[alt.Tooltip("år:O"), alt.Tooltip("årlig:Q", format=",.0f", title="Året"),
                 alt.Tooltip("kumulativt:Q", format=",.0f", title="Kumulativt")])
    zero = alt.Chart(pd.DataFrame({"y": [0]})).mark_rule(color=INK_MUTED, size=2).encode(y="y:Q")
    st.altair_chart((bars + zero).properties(height=280), use_container_width=True)

    roi1 = year1 / invest * 100
    roi3 = (flows[:3].sum() - invest) / invest * 100
    roi8 = (flows.sum() - invest) / invest * 100
    pos = np.where(cum >= 0)[0]
    if len(pos):
        k = pos[0]
        prev = cum[k - 1] if k else -invest
        payback = k + (0 - prev) / (cum[k] - prev)
    else:
        payback = None
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("ROI, kun år 1", f"{roi1:+.1f} %")
    m2.metric("ROI over 3 år", f"{roi3:+.1f} %")
    m3.metric("ROI over 8 år", f"{roi8:+.1f} %")
    m4.metric("Tilbakebetaling", f"{payback:.2f} år" if payback else "aldri")

    _point(
        f"**Tre ROI-tall om det samme prosjektet: {roi1:+.0f} %, {roi3:+.0f} % og {roi8:+.0f} %.** "
        f"Ingen av dem er feil. De svarer på forskjellige spørsmål, og den som velger horisonten "
        f"velger i praksis konklusjonen.\n\n"
        f"**Dra «årlig endring» ned mot −50 %.** År 1 kan fortsatt se strålende ut mens prosjektet "
        f"aldri tjener inn investeringen. Det er derfor **en ROI uten oppgitt horisont er ubrukelig**, "
        f"og hvorfor tilbakebetalingstid hører med."
    )


# --------------------------------------------------------------------------
# B. Signals and dashboards
# --------------------------------------------------------------------------

def _vanity_metric():
    st.markdown("#### 5 · Vanity-metrikken")
    st.caption("Trafikken stuper oppover og teamet feirer. Se hva som skjer med det som faktisk teller.")
    c1, c2 = st.columns(2)
    with c1:
        traffic_growth = st.slider("Endring i trafikk", -0.3, 1.0, 0.378, 0.01, key="vk_b1_t", format="%.0f%%")
    with c2:
        conv_change = st.slider("Endring i konverteringsrate", -0.5, 0.5, -0.124, 0.005, key="vk_b1_c", format="%.1f%%")

    t0, c0 = 15_600.0, 0.0132
    t1, c1v = t0 * (1 + traffic_growth), c0 * (1 + conv_change)
    o0, o1 = t0 * c0, t1 * c1v
    df = pd.DataFrame({
        "periode": ["Før", "Etter"] * 3,
        "mål": ["Trafikk (økter)"] * 2 + ["Konvertering"] * 2 + ["Ordrer"] * 2,
        "indeks": [100, (1 + traffic_growth) * 100, 100, (1 + conv_change) * 100, 100, o1 / o0 * 100],
        "verdi": [t0, t1, c0, c1v, o0, o1],
    })
    chart = (
        alt.Chart(df).mark_line(point=alt.OverlayMarkDef(size=90, filled=True), size=3)
        .encode(
            x=alt.X("periode:N", title=None, sort=["Før", "Etter"], axis=alt.Axis(labelAngle=0)),
            y=alt.Y("indeks:Q", title="Indeksert, før = 100"),
            color=alt.Color("mål:N", scale=alt.Scale(
                domain=["Trafikk (økter)", "Konvertering", "Ordrer"], range=[C_ORANGE, C_AQUA, C_BLUE]),
                legend=alt.Legend(title=None, orient="top")),
            tooltip=[alt.Tooltip("mål:N"), alt.Tooltip("periode:N"), alt.Tooltip("indeks:Q", format=".1f")],
        ).properties(height=280)
    )
    ends = df[df["periode"] == "Etter"]
    lab = alt.Chart(ends).mark_text(align="left", dx=10, fontSize=12).encode(
        x=alt.X("periode:N", sort=["Før", "Etter"]), y="indeks:Q",
        text=alt.Text("indeks:Q", format=".0f"),
        color=alt.Color("mål:N", scale=alt.Scale(
            domain=["Trafikk (økter)", "Konvertering", "Ordrer"], range=[C_ORANGE, C_AQUA, C_BLUE]), legend=None))
    base = alt.Chart(pd.DataFrame({"y": [100]})).mark_rule(color=INK_MUTED, strokeDash=[4, 3]).encode(y="y:Q")
    st.altair_chart(chart + lab + base, use_container_width=True)

    st.dataframe(pd.DataFrame({
        "Måltall": ["Trafikk (økter/mnd)", "Konverteringsrate", "Ordrer/mnd"],
        "Før": [f"{t0:,.0f}", f"{c0:.2%}", f"{o0:,.0f}"],
        "Etter": [f"{t1:,.0f}", f"{c1v:.2%}", f"{o1:,.0f}"],
        "Endring": [f"{traffic_growth:+.1%}", f"{conv_change:+.1%}", f"{o1/o0-1:+.1%}"],
    }), hide_index=True, use_container_width=True)

    _point(
        f"**Ordrer = trafikk × konvertering.** Trafikken er opp {traffic_growth:+.0%}, konverteringen "
        f"{conv_change:+.1%}, og resultatet er {o1/o0-1:+.1%}.\n\n"
        f"**Dra konverteringen til rundt −27 %.** Da står ordrene stille mens trafikkgrafen fortsatt "
        f"peker bratt oppover — og trafikk er akkurat den typen tall som havner på forsiden av et dashbord. "
        f"Leksjonens vanity-test forklarer hvorfor: trafikk kan nesten bare gå opp, har ingen nevner, "
        f"og ingen beslutning henger i den. Konverteringsraten består alle tre."
    )


def _lead_lag():
    st.markdown("#### 6 · Ledende mot etterslepende indikator")
    st.caption("Det ledende signalet snur først. Det etterslepende bekrefter det — når det er for sent å handle.")
    c1, c2, c3 = st.columns(3)
    with c1:
        lag = st.slider("Etterslep (måneder)", 0, 9, 4, 1, key="vk_b2_lag")
    with c2:
        shock = st.slider("Hvor kraftig snur signalet?", -40, 10, -22, 1, key="vk_b2_shock")
    with c3:
        noise = st.slider("Støy i målingene", 0.0, 8.0, 2.5, 0.5, key="vk_b2_noise")

    rng = np.random.default_rng(12)
    months = np.arange(1, 25)
    step = np.clip((months - 9) / 3.0, 0, 1)
    leading = 100 + shock * step + rng.normal(0, noise, 24)
    lag_step = np.clip((months - 9 - lag) / 3.0, 0, 1)
    lagging = 100 + shock * lag_step + rng.normal(0, noise * 0.6, 24)
    df = pd.concat([
        pd.DataFrame({"måned": months, "verdi": leading, "indikator": "Ledende: kundetilfredshet"}),
        pd.DataFrame({"måned": months, "verdi": lagging, "indikator": "Etterslepende: omsetning"}),
    ])
    chart = (
        alt.Chart(df).mark_line(size=2.5)
        .encode(
            x=alt.X("måned:Q", title="Måned"),
            y=alt.Y("verdi:Q", title="Indeks", scale=alt.Scale(zero=False)),
            color=alt.Color("indikator:N", scale=alt.Scale(
                domain=["Ledende: kundetilfredshet", "Etterslepende: omsetning"], range=[C_ORANGE, C_BLUE]),
                legend=alt.Legend(title=None, orient="top")),
            tooltip=[alt.Tooltip("indikator:N"), alt.Tooltip("måned:Q"), alt.Tooltip("verdi:Q", format=".1f")],
        ).properties(height=280)
    )
    marks = alt.Chart(pd.DataFrame({"x": [9, 9 + lag], "hva": ["Ledende snur", "Etterslepende snur"]})).mark_rule(
        strokeDash=[4, 3], size=2, color=INK_MUTED).encode(x="x:Q", tooltip="hva:N")
    st.altair_chart(chart + marks, use_container_width=True)
    _point(
        f"**Det er {lag} måneder mellom de to knekkpunktene.** I det vinduet er problemet allerede skjedd "
        f"og omsetningstallet viser fortsatt full styrke.\n\n"
        f"**Dra støyen opp til 6.** Nå er knekkpunktet i det ledende signalet mye vanskeligere å se — "
        f"som er den prisen ledende indikatorer betaler: de kommer tidlig og de er mer utsatt for "
        f"falske alarmer. Et KPI-sett med bare etterslepende mål er alltid for sent ute; et med bare "
        f"ledende reagerer på støy."
    )


def _threshold_alarms():
    st.markdown("#### 7 · Terskelen som utløser seg selv")
    st.caption(
        "Et KPI som svinger normalt rundt målet. Ingenting endrer seg i virksomheten. "
        "Se hvor mange ganger dashbordet slår alarm."
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        sd = st.slider("Normal variasjon (standardavvik)", 1.0, 12.0, 6.0, 0.5, key="vk_b3_sd")
    with c2:
        thr = st.slider("Terskel (avvik fra målet)", 2.0, 25.0, 8.0, 0.5, key="vk_b3_thr")
    with c3:
        cadence = st.radio("Rapporteringstakt", ["Daglig", "Ukentlig", "Månedlig"], key="vk_b3_cad")

    seed = _seed_control("vk_b3", "Nytt år med data")
    rng = np.random.default_rng(seed)
    daily = 100 + rng.normal(0, sd, 364)
    group = {"Daglig": 1, "Ukentlig": 7, "Månedlig": 28}[cadence]
    series = daily.reshape(-1, group).mean(axis=1)
    idx = np.arange(1, len(series) + 1)
    df = pd.DataFrame({"periode": idx, "verdi": series})
    df["alarm"] = np.where(np.abs(df["verdi"] - 100) > thr, "Alarm", "Innenfor")

    line = alt.Chart(df).mark_line(size=2, color=C_BLUE).encode(
        x=alt.X("periode:Q", title=f"Rapporteringsperiode ({cadence.lower()})"),
        y=alt.Y("verdi:Q", title="KPI", scale=alt.Scale(zero=False)))
    pts = alt.Chart(df).mark_point(size=70, filled=True).encode(
        x="periode:Q", y="verdi:Q",
        color=alt.Color("alarm:N", scale=alt.Scale(domain=["Innenfor", "Alarm"], range=[C_BLUE, S_CRITICAL]),
                        legend=alt.Legend(title=None, orient="top")),
        tooltip=[alt.Tooltip("periode:Q"), alt.Tooltip("verdi:Q", format=".1f"), alt.Tooltip("alarm:N")])
    bands = alt.Chart(pd.DataFrame({"y": [100 - thr, 100 + thr]})).mark_rule(
        color=S_WARNING, strokeDash=[5, 4], size=2).encode(y="y:Q")
    target = alt.Chart(pd.DataFrame({"y": [100]})).mark_rule(color=INK_MUTED, size=1.5).encode(y="y:Q")
    st.altair_chart((line + bands + target + pts).properties(height=300), use_container_width=True)

    alarms = int((df["alarm"] == "Alarm").sum())
    m1, m2, m3 = st.columns(3)
    m1.metric("Alarmer", f"{alarms} av {len(df)}")
    m2.metric("Andel perioder", f"{alarms/len(df):.1%}")
    m3.metric("Terskel i σ", f"{thr/sd:.2f}σ")
    _point(
        f"**Ingenting skjedde, og dashbordet slo alarm {alarms} ganger.** Terskelen ligger på "
        f"{thr/sd:.2f} standardavvik, og ved normal variasjon vil målingen krysse den av seg selv.\n\n"
        f"**Bytt til månedlig.** Samme underliggende data, langt færre alarmer — fordi et månedssnitt "
        f"jevner ut støyen som en dagsmåling viser rå. Det er refresh-rate-fella fra leksjonen: "
        f"jo oftere du ser på et tall, jo flere anledninger til å forveksle normal variasjon med et signal.\n\n"
        f"**Og ankringen:** når terskelen først står i systemet, slutter folk å spørre om den var riktig satt. "
        f"Forsvaret er å kreve et *vedvarende* utslag, og å oppgi den normale variasjonen på selve tavla."
    )


def _definition_change():
    st.markdown("#### 8 · KPI-en som stupte uten at noe skjedde")
    st.caption(
        "Samme kunder, samme data, samme måned. Bare definisjonen av «aktiv kunde» ble endret — "
        "og ingen skrev det ned. Case 6 i leksjonen."
    )
    window = st.select_slider("Vindu for «aktiv kunde»", [1, 3, 6, 12, 18, 24],
                              value=12, key="vk_b4_win",
                              format_func=lambda v: f"kjøpt siste {v} md.")
    rng = np.random.default_rng(21)
    n = 4000
    months_since = rng.exponential(9.0, n)
    retention = float((months_since <= window).mean())
    grid = pd.DataFrame({"vindu": [1, 3, 6, 12, 18, 24]})
    grid["retensjon"] = [float((months_since <= w).mean()) for w in grid["vindu"]]
    grid["valgt"] = np.where(grid["vindu"] == window, "Valgt definisjon", "Andre definisjoner")

    bars = (
        alt.Chart(grid).mark_bar(cornerRadiusEnd=4, size=44)
        .encode(
            x=alt.X("vindu:O", title="Vindu (måneder)", axis=alt.Axis(labelAngle=0)),
            y=alt.Y("retensjon:Q", title="Rapportert retensjon", axis=alt.Axis(format="%")),
            color=alt.Color("valgt:N", scale=alt.Scale(domain=["Andre definisjoner", "Valgt definisjon"],
                                                       range=[C_BLUE, C_ORANGE]),
                            legend=alt.Legend(title=None, orient="top")),
            tooltip=[alt.Tooltip("vindu:O", title="Måneder"), alt.Tooltip("retensjon:Q", format=".1%")],
        ).properties(height=250)
    )
    lab = alt.Chart(grid).mark_text(dy=-8, fontSize=12, color=INK_MUTED).encode(
        x="vindu:O", y="retensjon:Q", text=alt.Text("retensjon:Q", format=".0%"))
    st.altair_chart(bars + lab, use_container_width=True)

    r12 = float((months_since <= 12).mean())
    m1, m2 = st.columns(2)
    m1.metric("Rapportert retensjon", f"{retention:.1%}")
    m2.metric("Mot 12-måneders definisjon", f"{(retention-r12)*100:+.1f} pp")
    _point(
        f"**Alle disse søylene beskriver nøyaktig samme kundebase.** Ingen kunde kom eller gikk. "
        f"Retensjonen «falt» fra {r12:.0%} til {retention:.0%} fordi vinduet ble endret.\n\n"
        f"**Dette er poenget ingen datakvalitetssjekk fanger.** Hver eneste verdi er gyldig, hver "
        f"beregning er riktig, og tallet er likevel ikke sammenlignbart med forrige måned. "
        f"Validering fanger *verdifeil*; den fanger ikke *definisjonsendringer*.\n\n"
        f"**Forsvaret er versjonskontroll på definisjonen**, ikke bare på dataene: en datert, skriftlig "
        f"definisjon som endres i en logg alle kan lese. Det er hele argumentet i leksjon 1.1 — "
        f"du bytter et skjønn mot en logg."
    )


# --------------------------------------------------------------------------
# C. Qualitative measures
# --------------------------------------------------------------------------

_NPS_DEFAULT = [3, 2, 4, 6, 9, 14, 38, 52, 74, 86, 60]


def _nps():
    st.markdown("#### 9 · NPS — og de bevegelsene den ikke ser")
    st.caption(
        "Net Promoter Score = andel ambassadører (9–10) minus andel kritikere (0–6). "
        "Aktivitet 1.1.2 fant at den er blind for det meste av skalaen."
    )
    counts = np.array(_NPS_DEFAULT, dtype=float)
    move = st.radio(
        "Hva om kundene flytter seg?",
        ["Ingen endring", "Alle 6-ere blir 7", "Alle 0–5 blir 6", "Alle 8-ere blir 9"],
        key="vk_c1_move", horizontal=True)
    c = counts.copy()
    if move == "Alle 6-ere blir 7":
        c[7] += c[6]; c[6] = 0
    elif move == "Alle 0–5 blir 6":
        c[6] += c[:6].sum(); c[:6] = 0
    elif move == "Alle 8-ere blir 9":
        c[9] += c[8]; c[8] = 0

    n = c.sum()
    prom, pas, det = c[9:].sum(), c[7:9].sum(), c[:7].sum()
    nps = (prom - det) / n * 100
    base_nps = (counts[9:].sum() - counts[:7].sum()) / counts.sum() * 100
    mean_now = float((np.arange(11) * c).sum() / n)
    mean_base = float((np.arange(11) * counts).sum() / counts.sum())

    df = pd.DataFrame({"score": np.arange(11), "antall": c})
    df["gruppe"] = np.where(df["score"] >= 9, "Ambassadør (9–10)",
                            np.where(df["score"] >= 7, "Passiv (7–8)", "Kritiker (0–6)"))
    chart = (
        alt.Chart(df).mark_bar(cornerRadiusTopLeft=4, cornerRadiusTopRight=4)
        .encode(
            x=alt.X("score:O", title="Score", axis=alt.Axis(labelAngle=0)),
            y=alt.Y("antall:Q", title="Antall svar"),
            color=alt.Color("gruppe:N", scale=alt.Scale(
                domain=["Kritiker (0–6)", "Passiv (7–8)", "Ambassadør (9–10)"],
                range=[S_CRITICAL, INK_MUTED, C_BLUE]), legend=alt.Legend(title=None, orient="top")),
            tooltip=[alt.Tooltip("score:O"), alt.Tooltip("antall:Q"), alt.Tooltip("gruppe:N")],
        ).properties(height=270)
    )
    st.altair_chart(chart, use_container_width=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("NPS", f"{nps:+.1f}", delta=f"{nps-base_nps:+.1f}")
    m2.metric("Snittscore", f"{mean_now:.2f}", delta=f"{mean_now-mean_base:+.2f}")
    m3.metric("Ambassadører", f"{prom/n:.1%}")
    m4.metric("Kritikere", f"{det/n:.1%}")

    if move == "Alle 0–5 blir 6":
        _callout(
            f"**{int(counts[:6].sum())} kunder ble målbart mindre misfornøyde, og NPS rørte seg ikke ett hakk.** "
            f"Snittscoren steg fra {mean_base:.2f} til {mean_now:.2f}, men alle disse kundene var kritikere "
            f"før og er kritikere etter.\n\nDet er NPS-ens konstruksjon: den bryr seg bare om **hvilken bøtte** "
            f"du er i, ikke hvor i bøtta. En reell forbedring for de sinteste kundene er usynlig.",
            S_CRITICAL, "rgba(208,59,59,0.08)")
    elif move == "Alle 6-ere blir 7":
        _callout(
            f"**Én scores forflytning, og NPS hopper {nps-base_nps:+.1f} poeng.** De {int(counts[6])} kundene "
            f"gikk fra 6 til 7 — knapt merkbart i opplevelsen, og de krysset bøttegrensen.\n\n"
            f"Sammenlign med snittscoren, som bare steg {mean_now-mean_base:+.2f}. **All NPS-ens følsomhet "
            f"ligger konsentrert rundt terskelverdiene 6/7 og 8/9**, og ingen andre steder.",
            S_WARNING, "rgba(250,178,25,0.10)")
    else:
        _point(
            "**Prøv «Alle 0–5 blir 6» og deretter «Alle 6-ere blir 7».** Den første er en stor reell "
            "forbedring som NPS ikke registrerer i det hele tatt. Den andre er en minimal forflytning "
            "som flytter NPS kraftig. Det forteller deg hvor målet er følsomt — og hvor det er blindt.")

    st.caption(
        f"Basert på {int(counts.sum())} svar, som i aktivitet 1.1.2. Husk også svarprosenten: "
        f"348 svar av 1 200 utsendte er 29 %, og de 71 prosentene som ikke svarte er ikke med i noen av tallene."
    )


def _likert_spread():
    st.markdown("#### 10 · Snittet som skjuler polariseringen")
    st.caption("To avdelinger, identisk gjennomsnittsscore, helt ulik virkelighet.")
    spread = st.slider("Hvor polarisert er avdeling B?", 0.0, 1.0, 0.75, 0.05, key="vk_c2_sp")
    base = np.array([2, 6, 18, 34, 20], dtype=float)          # 1..5, samlet rundt midten
    polar = np.array([22, 6, 8, 6, 38], dtype=float)
    b = base * (1 - spread) + polar * spread
    b = b / b.sum() * base.sum()
    scores = np.arange(1, 6)
    mean_a = float((scores * base).sum() / base.sum())
    mean_b = float((scores * b).sum() / b.sum())
    sd_a = float(np.sqrt(((scores - mean_a) ** 2 * base).sum() / base.sum()))
    sd_b = float(np.sqrt(((scores - mean_b) ** 2 * b).sum() / b.sum()))
    unhappy_a = float(base[:2].sum() / base.sum())
    unhappy_b = float(b[:2].sum() / b.sum())

    df = pd.concat([
        pd.DataFrame({"score": scores, "antall": base, "avdeling": "Avdeling A"}),
        pd.DataFrame({"score": scores, "antall": b, "avdeling": "Avdeling B"}),
    ])
    chart = (
        alt.Chart(df).mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3)
        .encode(
            x=alt.X("score:O", title="Likert-score (1 = svært misfornøyd)", axis=alt.Axis(labelAngle=0)),
            y=alt.Y("antall:Q", title="Antall svar"),
            color=alt.Color("avdeling:N", scale=alt.Scale(domain=["Avdeling A", "Avdeling B"],
                                                          range=[C_BLUE, C_ORANGE]),
                            legend=alt.Legend(title=None, orient="top")),
            xOffset="avdeling:N",
            tooltip=[alt.Tooltip("avdeling:N"), alt.Tooltip("score:O"), alt.Tooltip("antall:Q", format=".0f")],
        ).properties(height=270)
    )
    st.altair_chart(chart, use_container_width=True)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Snitt A", f"{mean_a:.2f}")
    m2.metric("Snitt B", f"{mean_b:.2f}")
    m3.metric("Spredning", f"{sd_a:.2f} mot {sd_b:.2f}")
    m4.metric("Andel 1–2", f"{unhappy_a:.0%} mot {unhappy_b:.0%}")
    _point(
        f"**Snittene er {mean_a:.2f} og {mean_b:.2f}** — praktisk talt like, og de ville stått som ett "
        f"tall hver på et dashbord. Men i avdeling B er **{unhappy_b:.0%}** dypt misfornøyde mot "
        f"{unhappy_a:.0%} i A.\n\n"
        f"To ting følger. **Et snitt trenger sin spredning** for å bety noe — her {sd_a:.2f} mot {sd_b:.2f}. "
        f"Og en Likert-skala er **ordinal**: avstanden fra 1 til 2 er ikke nødvendigvis den samme som fra "
        f"4 til 5, så gjennomsnittet er strengt tatt et regnestykke på rangeringer. "
        f"Rapporter fordelingen, eller minst andelen i ytterkantene."
    )


SECTIONS_11 = {
    "1.1 A · KPI-er og økonomi": [_cac_ltv, _blended_cac_mix, _margin_waterfall, _roi_horizon],
    "1.1 B · Signaler og dashbord": [_vanity_metric, _lead_lag, _threshold_alarms, _definition_change],
    "1.1 C · Kvalitative mål": [_nps, _likert_spread],
}

INTRO_11 = {
    "1.1 A · KPI-er og økonomi": "Hvorfor CAC uten LTV er utolkbart, hvordan en samlet CAC kan falle uten at noe ble billigere, hvilken margin du egentlig mener, og hvordan horisonten alene bestemmer om et prosjekt er lønnsomt.",
    "1.1 B · Signaler og dashbord": "Vanity-metrikken som peker oppover mens ordrene står stille, avstanden mellom ledende og etterslepende signal, terskelen som utløser seg selv, og KPI-en som stupte fordi noen endret en definisjon.",
    "1.1 C · Kvalitative mål": "Hva NPS ser og hva den er blind for, og hvorfor to avdelinger med samme snittscore kan ha helt ulik virkelighet.",
}
