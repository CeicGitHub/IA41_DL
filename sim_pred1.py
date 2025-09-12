import time

# Calificaciones conocidas
# Escala: 1 a 5
ana_matrix = 5
ana_frozen = None   # No ha calificado Frozen
luis_matrix = 4
luis_frozen = 2

# Paso 1: calcular similitud entre Ana y Luis (coseno simple en este caso)
# Fórmula: sim = (a*b) / (|a|*|b|)
numerador = ana_matrix * luis_matrix
denominador = (ana_matrix**2)**0.5 * (luis_matrix**2)**0.5
sim_ana_luis = numerador / denominador

# Paso 2: predecir la calificación de Ana para Frozen
# Fórmula: pred = (sim * calificación vecino) / sim
pred_ana_frozen = (sim_ana_luis * luis_frozen) / sim_ana_luis

# Mostrar resultados
print("Similitud Ana-Luis:", (sim_ana_luis, 2))
print("Predicción de Ana para Frozen:", (pred_ana_frozen, 2))
