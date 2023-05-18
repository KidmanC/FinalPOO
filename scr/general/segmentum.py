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
        print(f"Added planet {planet.name} to Segmentum {self.__name}")

    def search_planet(self, name: str) -> bool:
        for planet in self.__planets:
            if(planet.name == name):
                return True
        return False

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def planets (self) -> str:
        return self.__planets
    
    
        