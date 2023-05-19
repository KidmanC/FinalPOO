from typing import List
#from utils.planet import Planet
#from person.person import Soldier

class Regiment:
    def __init__(self, name: str, planet: "Planet", soldiers: List["Soldier"] = None) -> None:
        self.__name = name
        self.__planet = planet
        self.__soldiers = [] if soldiers is None else soldiers
        self.__planet.add_regiment(self)
        ##add this regiment to the planet (done)

    def add_planet(self, planet: "Planet"):
        self.__planet = planet

    def add_soldier(self, soldier: "Soldier"):
        self.__soldiers.append(soldier)

    @property
    def name(self):
        return self.__name
    
    @property
    def soldiers(self):
        return self.__soldiers
    
    def soldiers_quantity(self):
        return len(self.__soldiers)