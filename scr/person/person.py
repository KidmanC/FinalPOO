from abc import ABC, abstractmethod

class Person(ABC): # Abstract class
    def __init__(self, id_string: str, name:str , planet: "Planet") -> None:
        self._id_string = id_string
        self._name = name
        self._planet = planet


class Astarte (Person):
    def __init__(self, id_string: str, name:str , planet: "Planet", founding: int) -> None:
        super().__init__(id_string, name, planet)
        self.__founding = founding

class Bureraucrat(Person):
    def __init__(self, id_string: str, name:str , planet: "Planet", department: str) -> None:
        super().__init__(id_string, name, planet)
        self._department = department

class Soldier(Person):
    def __init__(self, id_string: str, name:str , planet: "Planet", age: int) -> None:
        super().__init__(id_string, name, planet)
        self._age = age

class Primarch(Person):
    def __init__(self, id_string: str, name: str , planet: "Planet", alias: str, loyalty: bool, status: "Status", imperium:"Imperium") -> None:
        super().__init__(id_string, name, planet)
        self.__alias = alias
        self.__loyalty = loyalty
        self.__status = status
        self.__imperium = imperium
        ##add this primarch to the imperium


        

    
