import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.express as px

# ---- BASE ----

st.set_page_config(page_title="Coin Viewer")

# ---- FUNCTIONS ----

def APIRequest(moedaMain, moedaCheck, periodoCotacao):
    bids = []
    cambioMoedas = []
    for moedaReq in moedaCheck:
        if moedaReq != moedaMain:
            link = f"https://economia.awesomeapi.com.br/json/daily/{moedaReq[-4:-1]}-{moedaMain[-4:-1]}/{periodoCotacao}"
            req = requests.get(link)
            resForm = req.json()
            bids.append([cambioRes['bid'] for cambioRes in resForm])
            cambioMoedas.append(moedaReq[-4:-1])

    # print(f"Moedas: {cambioMoedas}")
    # print(f"Bids: {bids}")
    
    bidsTransp = np.array(bids).T
    bidsFormatFloat = bidsTransp.astype(np.float32)
        
    with st.container():
        chart_data = pd.DataFrame(
            bidsFormatFloat,
            columns=cambioMoedas)
        
        chart_data_fig = px.line(chart_data, markers=True)
        chart_data_fig.update_layout(xaxis_title="Dias", yaxis_title="Valor")

        st.subheader(f"\nGráfico em relação a: {moedaMain}")
        st.line_chart(chart_data)
        st.bar_chart(chart_data)
        st.plotly_chart(chart_data_fig)

with st.container():
    st.title("Coin Vi:green[€]wer")
    st.subheader("Acompanhe as principais moedas do mundo!")

st.write("---")

with st.container():
    listaMoedas = ["Real Brasileiro(BRL)", "Dólar americano(USD)", "Euro(EUR)", "Iene japonês(JPY)", "Libra esterlina(GBP)", "Yuan chinês(CNY)", "Franco suíço(CHF)", "Dólar australiano(AUD)", "Dólar canadense(CAD)", "Dólar de Singapura(SGD)", "Coroa norueguesa(NOK)"]
    # listaPeriodo = ["1 MÊS - 30 d", "1 TRIMESTRE - 90 d", "1 SEMESTRE - 180 d", "1 ANO - 365 d"]
    # listaPeriodoDias = [30, 90, 180, 365]

    st.header("Selecione as moedas:")
    moedaMain = st.selectbox("Moeda em relação", listaMoedas)

    # for cond in moedaMain:

    moedaCheck = st.multiselect("Moedas a comparar", listaMoedas)
    periodoCotacao = int(st.slider("Período a comparar(dias): ", 0, 365, 30))

if st.button("Calcular"):
    if moedaCheck == []:
        st.warning("⚠️ - Selecione a(s) moeda(s) a comparar")
    else:
        APIRequest(moedaMain, moedaCheck, periodoCotacao)
    
