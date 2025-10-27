import numpy
import matplotlib.pyplot as plt
import time
import math

Input1 = numpy.array([1.0, 2.0, 3.0])
Input2 = numpy.array([4.0, 5.0, 6.0])
Input3 = numpy.array([7.0, 8.0, 9.0])


w1 = [1.5, 2.5, 3.5]
w2 = [4.5, 5.5, 6.5]
w3 = [7.5, 8.5, 9.5]

b1 = 1
b2 = 2
b3 = 3

sumaponderada = numpy.dot((Input1+Input2+Input3) + (b1+b2+b3))

#todo: perhaps alternative...
""""
AllInputs = numpy.array(
    [1.0, 2.0, 3.0,
    4.0, 5.0, 6.0,
    7.0, 8.0, 9.0,])
"""


