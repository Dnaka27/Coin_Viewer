import streamlit as st
import pandas as pd
import numpy as np
import requests
from datetime import datetime, timedelta

moedaMain = "BRL"
moedaCheck = ["USD", "EUR", "LIB"]
periodoCotacao = "1 semana"



data_atual = datetime.now()

periodoCalc = timedelta(days=periodoCotacao)

link = f"https://economia.awesomeapi.com.br/json/last/"
moedaMainReq = moedaMain[-4:-1]
for moedaReq in moedaCheck:
    link += f"{moedaMainReq}-{moedaReq[-4:-1]},"

linkReq = link[:-1]
req = requests.get(linkReq)
reqForm = req.json()