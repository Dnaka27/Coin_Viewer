import streamlit as st
import pandas as pd
import numpy as np
import requests

st.set_page_config(page_title="Coin Viewer")

with st.container():
    st.title("Coin Vi:green[€]wer")
    st.subheader("Acompanhe as mudanças das principais moedas do mundo!")

st.write("---")

with st.container():
    listaMoedas = ["Dólar americano(USD)", "Euro(EUR)", "Iene japonês(JPY)", "Libra esterlina(GBP)", "Yuan chinês(CNY)", "Franco suíço(CHF)", "Dólar australiano(AUD)", "Dólar canadense(CAD)", "Dólar de Singapura(SGD)", "Coroa norueguesa(NOK)"]

    st.header("Selecione as moedas:")
    moedaMain = st.selectbox("Moeda em relação", listaMoedas)
    moedaCheck = st.multiselect("Moedas a comparar", listaMoedas)

    # reqMoedas = 
    # req = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL")
    # resMoedas = req.json().keys()
    # for key in resMoedas:
    #     print(f'Moedas: {key}')

st.markdown("<br>")

with st.container():
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)
