
import numpy as np

#! 3 entradas ,3 pesos y 1 bia --> Corresponde HiddenLayer_1
inputs_1 = np.array([1.0, 2.0, 3.0])
weights_h1 = np.array([0.2, -0.3, 0.4])
bias_h1 = 0.1

#! 3 entradas ,3 pesos y 1 bia --> Corresponde HiddenLayer_2
inputs_2 = np.array([4.0, 5.0, 6.0])
weights_h2 = np.array([-0.5, 0.7, 0.2]) 
bias_h2 = -0.2

# === Capa oculta 1 y 2 (cada una con una sola neurona) ===
h1_output = np.tanh(np.dot(inputs_1, weights_h1) + bias_h1)
h2_output = np.tanh(np.dot(inputs_2, weights_h2) + bias_h2)

# Combinar las salidas de ambas capas ocultas
hidden_outputs = np.array([h1_output, h2_output])

# === Capa de salida ===
weights_out = np.array([0.6, -0.8])   # 2 pesos (uno por cada hidden layer)
bias_out = 0.3

#todo: SalidaFinal
output = np.tanh(np.dot(hidden_outputs, weights_out) + bias_out)

print("Salida final:", output)


