import numpy as np
import pandas as pd

array_original = [
    ['4.9073', '4.9073', '4.8927', '4.9032', '4.9006', '4.8989', '4.8757'],
    ['5.3652', '5.3652', '5.3571', '5.3787', '5.3615', '5.3825', '5.3579'],
    ['0.03384', '0.03385', '0.0338', '0.03412', '0.0342', '0.03438', '0.03443']
]

# Converter os valores para números de ponto flutuante
array_numerico = [[float(valor) for valor in linha] for linha in array_original]

array_transposto = np.array(array_numerico).T

# Criar um DataFrame com o array transposto
chart_data = pd.DataFrame(array_transposto, columns=["moeda1", "moeda2", "moeda3"])

print(chart_data)