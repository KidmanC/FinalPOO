from typing import List

class RuntimeError(Exception):
    pass

class Segmentum:
    planetas = []
    def __init__(self, name:str, location: str, planets: List["Planet"]= None) -> None:
        self.__name = name
        self.__location = location
        self.__planets = [] if planets is None else planets
        

    #def add_planet(self, planet: "Planet") -> None:
        #self.__planets.append(planet)
        #print(f"Added planet {planet.name} to Segmentum {self.__name}")

    def add_planet(self, planet: "Planet") -> None:
        for planeta in self.__planets:
            if(planeta.name == planet.name):
                return (f"RuntimeError: Planet already registered")
        self.__planets.append(planet)
        print(f"Added planet {planet.name} to Segmentum {self.__name}")

    @property
    def name(self) -> str:
        return self.__name
        