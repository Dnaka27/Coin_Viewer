import pandas as pd
import numpy as np

numbers = np.array(
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9],
 [10, 11, 12],
 [13, 14, 15]])

chart_data = pd.DataFrame(
    numbers,
    columns = ["moeda1", "moeda2", "moeda3"]
)

print(chart_data)