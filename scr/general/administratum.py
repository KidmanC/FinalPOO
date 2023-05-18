from typing import List
from person.person import Bureaucrat

class Administratum:
    def __init__(self, planet_registry: List[int]= None, bureaucrats: List["Bureaucrat"]= None) -> None:
        self.__planet_registry = [] if planet_registry is None else planet_registry
        self.__bureaucrats = [] if bureaucrats is None else bureaucrats
    
    @property
    def bureaucrats(self):
        return self.__bureaucrats
    
    @property
    def planet_registry(self):
        return self.__planet_registry