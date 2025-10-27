import numpy
import matplotlib.pyplot as plt
import time
import math

#! 1 Sola Neurona con 3 Entradas
inputs = numpy.array([1.0, 2.0, 3.0])

#! 3 Pesos Definidos Para Cada Entrada
weights = numpy.array([0.2, -0.5, 0.3])

#! Bias (constante que ajusta la salida)
bias = 0.4

#? Impresión de los valores
"""print("Entradas:", inputs)
print("Pesos:", weights)
print("Bias:", bias)"""

suma_ponderada = numpy.dot(inputs, weights) + bias
print("Suma ponderada:", suma_ponderada)

#? Función de activación tangente hiperbólica
output = numpy.tanh(suma_ponderada)
print("Salida activada (tanh):", output)

x = numpy.linspace(-5, 5, 100)   # valores de entrada
y = numpy.tanh(x)                # aplicar tanh a cada valor
plt.plot(x, y)
plt.title("Función de activación tanh")
plt.xlabel("Entrada")
plt.ylabel("Salida tanh(x)")
plt.grid(True)
plt.show()


# Capa oculta (2 neuronas)
hidden = numpy.tanh(numpy.dot(inputs, W1) + b1)

# Capa de salida (1 neurona)
output = numpy.tanh(numpy.dot(hidden, W2) + b2)



#todo: Additional Note
""" #*******
numpy.tanh(x, /, out=None, *, where=True, dtype=None)
z = numpy.array([-2., -1., 0., 1., 2.])
mask = z > 0                 #! solo aplicar donde z es positiva
out = z.copy()               #! para conservar valores donde where=False
numpy.tanh(z, out=out, where=mask)
print("mask:", mask)
print("resultado con where:", out)
""" #*******

""" #*******
#?Preguntas: 
#un sesgo y bia es lo mismo?
#la consideración de que la bia se añade a la entrada solo aplica en tanh?
"""#*******