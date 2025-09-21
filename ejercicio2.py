import time
#?todo: import math

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

#todo: Similitudes (coseno) sin usar math.sqrt
#? sim(Pepe, Stuart)  [co-calificados: La isla]
num_pepe_stuart = (pepe_la_isla * stuart_la_isla)
den_pepe_stuart = ((pepe_la_isla**2)**0.5) * ((stuart_la_isla**2)**0.5)
sim_pepe_stuart = num_pepe_stuart / den_pepe_stuart

#? sim(Pepe, McLovin) [co-calificados: La isla, Interstellar]
num_pepe_mclo = (pepe_la_isla * mclo_la_isla) + (pepe_interstellar * mclo_interstellar)
den_pepe_mclo = (((pepe_la_isla**2 + pepe_interstellar**2)**0.5) *
                 ((mclo_la_isla**2 + mclo_interstellar**2)**0.5))
sim_pepe_mclo = num_pepe_mclo / den_pepe_mclo

#? sim(Stuart, McLovin) [co-calificados: La isla, Pokémon]
num_stuart_mclo = (stuart_la_isla * mclo_la_isla) + (stuart_pokemon * mclo_pokemon)
den_stuart_mclo = (((stuart_la_isla**2 + stuart_pokemon**2)**0.5) *
                   ((mclo_la_isla**2 + mclo_pokemon**2)**0.5))
sim_stuart_mclo = num_stuart_mclo / den_stuart_mclo
#todo: Similitudes (coseno) sin usar math.sqrt


#todo Predicciónes (promedio ponderado)
num_pred_pepe_pok = (sim_pepe_stuart * stuart_pokemon) + (sim_pepe_mclo * mclo_pokemon)
den_pred_pepe_pok = (abs(sim_pepe_stuart) + abs(sim_pepe_mclo))
pred_pepe_pokemon = num_pred_pepe_pok / den_pred_pepe_pok 

num_pred_stuart_inter = (sim_pepe_stuart * pepe_interstellar) + (sim_stuart_mclo * mclo_interstellar)
den_pred_stuart_inter = (abs(sim_pepe_stuart) + abs(sim_stuart_mclo))
pred_stuart_interstellar = num_pred_stuart_inter / den_pred_stuart_inter 
#todo Predicciónes (promedio ponderado)


#todo: Resultados
print("Sim(Pepe,Stuart):     ", round(sim_pepe_stuart, 6))
print("Sim(Pepe,McLovin):    ", round(sim_pepe_mclo, 6))
print("Sim(Stuart,McLovin):  ", round(sim_stuart_mclo, 6))

print("Pepe → Pokémon:       ", round(pred_pepe_pokemon, 4))
print("Stuart → Interstellar:", round(pred_stuart_interstellar, 4))
#todo: Resultados
