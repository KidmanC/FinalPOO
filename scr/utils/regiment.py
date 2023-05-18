from typing import List
#from utils.planet import Planet
#from person.person import Soldier

class Regiment:
    def __init__(self, name: str, planet: "Planet", soldiers: List["Soldier"]) -> None:
        self.__name = name
        self.__planet = [] if planet is None else planet
        self.__soldiers = [] if soldiers is None else soldiers
        ##add this regiment to the planet