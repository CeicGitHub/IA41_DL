import time ##burst time or delays.

#! Calificaciones conocidas
#?Luis Calificaciones:
luis_matrix = 4
luis_frozen = 2

#?Ana Calificaciones:
ana_matrix = 5
ana_frozen = None
#! Calificaciones conocidas

#todo Paso 1: calcular similitud entre Ana(U) y Luis(V).
numerador = ana_matrix * luis_matrix
denominador =  (ana_matrix**2)**0.5 * (ana_matrix**2)**0.5
similutud = numerador / denominador
#todo Paso 1: calcular similitud entre Ana(U) y Luis(V).

#todo Paso 2: predecir la calificación de Ana para Frozen.
prediccion = (similutud * luis_frozen) / similutud  

#?Resultados:
print("Similitud Ana-Luis:", (similutud,2))
print("Predicción de Ana para Frozen:", (prediccion,2))

