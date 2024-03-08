import streamlit as st
import pandas as pd
import numpy as np

st.title("Teste :purple[STREAMLIT]")

bids = {'m1': [0.97, 1.2], 'm2': [0.8, 1.5], 'm3': [0.5, 0.3]}
cambioMoedas = ["USD", "EUR", "LIB"]

chart_data = pd.DataFrame(
    bids,
    columns=cambioMoedas
)

st.line_chart(chart_data)