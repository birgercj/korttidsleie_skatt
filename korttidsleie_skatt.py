import streamlit as st

st.set_page_config(page_title="Airbnb Skatteberegning", page_icon="🏡")

st.title("🏡 Skatteberegning for privat Airbnb/Korttidsleie")

st.write(
    """
    Fyll inn hvor mye du har tjent på utleie gjennom Airbnb eller korttidsleie, så viser vi deg
    hvor mye du eventuelt må skatte.
    """
)

# Brukeren legger inn inntekt
inntekt = st.number_input(
    "Hvor mye har du tjent?", 
    min_value=0.0,
    step=1000.0, 
    format="%.2f", 
    help="Oppgi beløpet i norske kroner (NOK)"
)

# Parametre
bunnfradrag = 10000  # 10 000 kr skattefritt
skattesats = 0.22    # 22% skatt på netto skattepliktig inntekt

# Beregning
if inntekt <= bunnfradrag:
    skattepliktig_inntekt = 0
    skattbar_inntekt = 0
    skatt = 0
else:
    skattepliktig_inntekt = inntekt - bunnfradrag
    skattbar_inntekt = skattepliktig_inntekt * 0.85  # Bare 85 % beskattes
    skatt = skattbar_inntekt * skattesats

# Resultat
st.header("Resultat")
st.metric(label="Total inntekt", value=f"{inntekt:,.2f} kr")
st.metric(label="Skattepliktig inntekt etter bunnfradrag (85%)", value=f"{skattbar_inntekt:,.2f} kr")
st.metric(label="Beregnet skatt (22%)", value=f"{skatt:,.2f} kr")

st.info("Merk: Dette er en forenklet kalkulator. Faktisk skatt kan variere. Kontakt skatterådgiver ved behov.")
