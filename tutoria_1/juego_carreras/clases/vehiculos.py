from abc import ABC, abstractmethod
import os

class Vehiculo(ABC):
    def __init__(self, placa:str, anio:int, color:str):
        self.__placa = placa
        self.anio = anio
        self.color = color
        self.distancia = 0
        
    # Getters
    def get_placa(self):
        return self.__placa
    
    # Setters
    def set_placa(self, nueva_placa):
        self.__placa = nueva_placa
        return self.__placa

    @abstractmethod
    def recorrer_distancia(self, distancia):
        pass
    
    @abstractmethod
    def __str__(self):
        pass
    
    
class Carro(Vehiculo):
    def __init__(self, placa: str, anio: int, color: str, marca: str, piloto:str):
        super().__init__(placa, anio, color)
        self.marca = marca
        self.piloto = piloto
        
    def __str__(self):
        return f"Hola, soy {self.piloto} y corro un carro {self.marca} de color {self.color} del año {self.anio} 🏎️"
    
    def recorrer_distancia(self, distancia):
        self.distancia += distancia
        
class Moto(Vehiculo):
    def __init__(self, placa: str, anio: int, color: str, marca: str, piloto:str):
        super().__init__(placa, anio, color)
        self.marca = marca
        self.piloto = piloto
        
    def __str__(self):
        return f"Hola, soy {self.piloto} y corro una moto {self.marca} de color {self.color} del año {self.anio} 🏍️"
    
    def recorrer_distancia(self, distancia):
        self.distancia += distancia
        
class VehiculoFactory:
    @staticmethod
    def crear_vehiculo(tipo):
        
        match tipo:
            case "carro":
                placa = input("Ingresa la placa de tu carro (Ej. ABC123): ").upper()
                anio = int(input("Ingresa el año de tu carro: "))
                color = input("Ingresa el color de tu carro: ").title()
                marca = input("Ingresa la marca de tu carro: ").title()
                piloto = input("Ingresa el nombre del piloto: ").title()
                os.system("cls" if os.name == "nt" else "clear")
                return Carro(placa, anio, color, marca, piloto)
            
            case "moto":
                placa = input("Ingresa la placa de tu moto (Ej. ABC123): ").upper()
                anio = int(input("Ingresa el año de tu moto: "))
                color = input("Ingresa el color de tu moto: ").title()
                marca = input("Ingresa la marca de tu moto: ").title()
                piloto = input("Ingresa el nombre del piloto: ").title()
                os.system("cls" if os.name == "nt" else "clear")
                return Moto(placa, anio, color, marca, piloto)