from typing import List

class RuntimeError(Exception):
    pass

class Segmentum:
    
    def __init__(self, name:str, location: str, planets: List["Planet"]= None) -> None:
        self.__name = name
        self.__location = location
        self.__planets = [] if planets is None else planets
        

    def add_planet(self, planet: "Planet") -> None:
        
            self.__planets.append(planet)
            print(f"Added Planet {planet.name} to Segmentum {self.__name}")
        

    def search_planet(self, planet: "Planet") -> bool:
        for planeta in self.__planets:
            if planeta == planet:
                return True
        return False

    def get_planet(self, planet_name: str) -> "Planet":
        for planet in self.__planets:
            if planet.name == planet_name:
                return planet
        return False

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def planets (self) -> str:
        return self.__planets
    
    
        