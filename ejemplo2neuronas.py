import numpy as np

#! 6 Entradas
x = np.array([1.0, 2.0, 3.0])
x1 =np.array([2.0, 3.0, 5.0])

# 1 neurona oculta
w1 = np.array([0.2, -0.4, 0.1])  # 3 pesos (uno por entrada)
b1 = 0.3
h = np.tanh(np.dot(x, w1) + b1)  # escalar

# 1 neurona de salida
w2 = 0.6  # un solo peso desde la capa oculta (escala h)
b2 = -0.5
h2 = np.tanh(np.dot(x1, w2) + b2)  # escalar

y = np.tanh(w2 * (h+h2) + b2)         # escalar

print("Salida:", y)
