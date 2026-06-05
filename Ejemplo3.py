import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# 1️⃣ Cargar los datos con Pandas
data = pd.read_csv("personas.csv")  # columnas: Nombre,Edad
print("Datos originales:\n", data)

# 2️⃣ Normalizar edades (usando NumPy)
max_edad = np.max(data["Edad"])
data["Edad_Normalizada"] = data["Edad"] / max_edad

print("\nDatos normalizados:\n", data)

# 3️⃣ Graficar edades originales y normalizadas
plt.plot(data["Nombre"], data["Edad"], label="Edad real", marker="o")
plt.plot(data["Nombre"], data["Edad_Normalizada"] * max_edad, label="Edad normalizada * max", marker="x")
plt.title("Comparación entre Edad real y normalizada")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.legend()
plt.grid(True)
plt.show()

# 4️⃣ TensorFlow (mini modelo lineal sin Keras)
# Entradas (x) = Edad normalizada, Salidas (y) = Edad real
x = tf.constant(data["Edad_Normalizada"].values, dtype=tf.float32)
y = tf.constant(data["Edad"].values, dtype=tf.float32)

# Variables entrenables
w = tf.Variable(0.0)
b = tf.Variable(0.0)

# Entrenamiento manual
for step in range(100):
    with tf.GradientTape() as tape:
        y_pred = w * x + b
        loss = tf.reduce_mean((y - y_pred) ** 2)
    grads = tape.gradient(loss, [w, b])
    w.assign_sub(0.1 * grads[0])
    b.assign_sub(0.1 * grads[1])

print(f"\nResultados TensorFlow: w={w.numpy():.2f}, b={b.numpy():.2f}, pérdida={loss.numpy():.4f}")
