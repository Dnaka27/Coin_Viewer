import plotly.express as px
import pandas as pd

# Dados de exemplo
data = [[4.9631, 5.4188], [4.9631, 5.4103], [4.9073, 5.3541], [4.9073, 5.3652]]

df = pd.DataFrame(data, columns=['a', 'b'])

# Criar um gráfico de linhas com Plotly
fig = px.line(df, title='Gráfico de Linhas')
fig.show()