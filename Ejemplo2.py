import pandas as pd
import numpy as np

# Leer el archivo CSV
data = pd.read_csv("personas.csv")

# Mostrar los datos originales
print("📋 Datos originales:")
print(data)

# Normalizar la edad con NumPy (usando operaciones vectorizadas)
max_edad = np.max(data["Edad"])
data["Edad_Normalizada"] = np.round(data["Edad"] / max_edad, 2)

# Calcular el promedio de edad con NumPy
promedio_edad = np.mean(data["Edad"])

# Crear una nueva columna indicando si la persona está arriba o abajo del promedio
data["Sobre_Promedio"] = np.where(data["Edad"] > promedio_edad, "Sí", "No")

print("\n📊 Datos procesados:")
print(data)

# Mostrar valores estadísticos
print("\n📈 Estadísticas:")
print(f"Edad máxima: {max_edad}")
print(f"Edad promedio: {promedio_edad:.2f}")



