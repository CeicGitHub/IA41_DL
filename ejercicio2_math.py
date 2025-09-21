import time
import math 

#nota:
#!la función abs(x) devuelve el valor absoluto de un número:
#!Si x es positivo → lo deja igual.
#!Si x es negativo → lo convierte en positivo
#? "abs" no es de la librería math, es una función integrada de Python

#! Pepe
pepe_la_isla = 4
pepe_interstellar = 5
pepe_pokemon = None

#! Stuart
stuart_la_isla = 2
stuart_interstellar = None
stuart_pokemon = 5

#! McLovin
mclo_la_isla = 3
mclo_interstellar = 5
mclo_pokemon = 4

#Paso1
#todo: Similitudes usando math.sqrt
# sim(Pepe, Stuart)  [co-calificados: La isla]
num_pepe_stuart = pepe_la_isla * stuart_la_isla
den_pepe_stuart = math.sqrt(pepe_la_isla**2) * math.sqrt(stuart_la_isla**2)
sim_pepe_stuart = num_pepe_stuart / den_pepe_stuart

# sim(Pepe, McLovin) [co-calificados: La isla, Interstellar]
num_pepe_mclo = (pepe_la_isla * mclo_la_isla) + (pepe_interstellar * mclo_interstellar)
den_pepe_mclo = (math.sqrt(pepe_la_isla**2 + pepe_interstellar**2) *
                 math.sqrt(mclo_la_isla**2 + mclo_interstellar**2))
sim_pepe_mclo = num_pepe_mclo / den_pepe_mclo

# sim(Stuart, McLovin) [co-calificados: La isla, Pokémon]
num_stuart_mclo = (stuart_la_isla * mclo_la_isla) + (stuart_pokemon * mclo_pokemon)
den_stuart_mclo = (math.sqrt(stuart_la_isla**2 + stuart_pokemon**2) *
                   math.sqrt(mclo_la_isla**2 + mclo_pokemon**2))
sim_stuart_mclo = num_stuart_mclo / den_stuart_mclo
#todo: Similitudes usando math.sqrt

#Paso1
#todo: Predicciones usando abs
num_pred_pepe_pok = (sim_pepe_stuart * stuart_pokemon) + (sim_pepe_mclo * mclo_pokemon)
den_pred_pepe_pok = abs(sim_pepe_stuart) + abs(sim_pepe_mclo)
pred_pepe_pokemon = num_pred_pepe_pok / den_pred_pepe_pok

# Stuart → Interstellar
num_pred_stuart_inter = (sim_pepe_stuart * pepe_interstellar) + (sim_stuart_mclo * mclo_interstellar)
den_pred_stuart_inter = abs(sim_pepe_stuart) + abs(sim_stuart_mclo)
pred_stuart_interstellar = num_pred_stuart_inter / den_pred_stuart_inter
#todo: Predicciones usando abs

#todo: Resultados
print("Sim(Pepe,Stuart):     ", round(sim_pepe_stuart, 6))
print("Sim(Pepe,McLovin):    ", round(sim_pepe_mclo, 6))
print("Sim(Stuart,McLovin):  ", round(sim_stuart_mclo, 6))

print("Pepe → Pokémon:       ", round(pred_pepe_pokemon, 4))
print("Stuart → Interstellar:", round(pred_stuart_interstellar, 4))
