from clases.vehiculos import VehiculoFactory
from random import randint
import time

if __name__ == "__main__":
    num_jugadores = int(input("Cuántos jugadores van a correr en esta carrera 😎? (min 2 - max 5): "))
    print()
    
    jugadores = {}
    for i in range(1, num_jugadores + 1):
        jugadores[f"Jugador {i}"] = None
        
        print(f"#### JUGADOR {i} ####")
        tipo = input("Elige el tipo de vehículo con el que quieres correr (carro, moto): ").lower()
        fabrica = VehiculoFactory

        jugadores[f"Jugador {i}"] = fabrica.crear_vehiculo(tipo)
        
    for k, v in jugadores.items():
        print(f"{k}: {v}")
        print() 
        
    ganador = None
    carrera_terminada = False

    while not carrera_terminada:
        for jugador in jugadores.values():
            jugador.recorrer_distancia(randint(0,10))
        
            print(f"Distancia recorrida por {jugador.piloto} -> {jugador.distancia}")
            time.sleep(1)
            
            if jugador.distancia >= 100:
                ganador = jugador
                carrera_terminada = True
                break
            
        print("-"*60)
        
    print(f"\n🏁 El ganador de la carrera es {ganador.piloto} en su {ganador.marca} de color {ganador.color} 🏆")