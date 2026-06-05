import pandas as pd
import tensorflow as tf

data = pd.read_csv("personas.csv")
data = data.dropna()  # elimina filas vacías
data["Edad"] = data["Edad"] / data["Edad"].max()  # normaliza columna Edad
print(data)
data.to_csv("personas_limpio.csv", index=False)  # guarda el DataFrame limpio en un nuevo archivo CSV


