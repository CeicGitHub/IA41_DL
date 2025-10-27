import numpy
import matplotlib.pyplot as plt
import time
import math

#! Estas entradas son para 2 neuronas
inputs1 = numpy.array([1.0, 2.0,])
inputs2 = numpy.array([1.5, 2.5])
#*Pesos y bias para la neurona 1
weights_1 = [0.2, -0.4,]
bias_1 = 0.3
#*Pesos y bias para la neurona 2
weights_2 = [-0.1, 0.7,]
bias_2 = -0.5

#todo: Capa oculta (2 neuronas)
hidden = numpy.tanh(numpy.dot(inputs1, weights_1) + bias_1)

#todo: Capa de salida (1 neurona)
output = numpy.tanh(numpy.dot(hidden, weights_2) + bias_2)
print("Salida Activación:", output)



output = numpy.linspace(-5, 5, 100)   # valores de entrada
y = numpy.tanh(output)                # aplicar tanh a cada valor
plt.plot(output, y)
plt.title("Función de activación tanh")
plt.xlabel("Entrada")
plt.ylabel("Salida tanh(x)")
plt.grid(True)
plt.show()


