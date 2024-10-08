import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.express

# ---- BASE ----

st.set_page_config(page_title="Coin Viewer")

# --------------

def APIRequest(moedaMain, moedaCheck, periodoCotacao):
    bids = []
    cambioMoedas = []
    for moedaReq in moedaCheck:
        if moedaReq != moedaMain:
            link = f"https://economia.awesomeapi.com.br/json/daily/{moedaReq[-4:-1]}-{moedaMain[-4:-1]}/{periodoCotacao}"

            # This project uses the Awesome API (https://docs.awesomeapi.com.br/) to retrieve currency quotes.
            # For more details and terms of use, please refer to their website.

            req = requests.get(link)
            resForm = req.json()
            bids.append([cambioRes['bid'] for cambioRes in resForm])
            cambioMoedas.append(moedaReq[-4:-1])
    
    bidsTransp = np.array(bids).T
    bidsTransp_df = np.array(bids)
    bidsFormatFloat = bidsTransp.astype(np.float32)
        
    with st.container():
        chart_data = pd.DataFrame(
            bidsFormatFloat,
            columns=cambioMoedas)
        
        chart_data_fig = plotly.express.line(chart_data, markers=True)
        chart_data_fig.update_layout(xaxis_title="Dias", yaxis_title="Valor")

        st.subheader(f"\nGráfico em relação a: {moedaMain}")
        st.plotly_chart(chart_data_fig)

with st.container():
    st.title("Coin Vi:green[€]wer")
    st.subheader("Acompanhe as principais moedas do mundo!")

st.write("---")

with st.container():
    listaMoedas = ["Real Brasileiro(BRL)", "Dólar americano(USD)", "Euro(EUR)", "Iene japonês(JPY)", "Libra esterlina(GBP)", "Yuan chinês(CNY)", "Franco suíço(CHF)", "Dólar australiano(AUD)", "Dólar canadense(CAD)", "Dólar de Singapura(SGD)", "Coroa norueguesa(NOK)"]

    st.header("Selecione as moedas:")
    moedaMain = st.selectbox("Moeda em relação", listaMoedas)
    moedaCheck = st.multiselect("Moedas a comparar", listaMoedas)
    periodoCotacao = int(st.slider("Período a comparar(dias): ", 0, 365, 30))

if st.button("Calcular"):
    if moedaCheck == []:
        st.warning("⚠️ - Selecione a(s) moeda(s) a comparar")
    else:
        APIRequest(moedaMain, moedaCheck, periodoCotacao)