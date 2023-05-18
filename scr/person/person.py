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

class Bureaucrat(Person):
    def __init__(self, id_string: str, name:str , planet: "Planet", department: str) -> None:
        super().__init__(id_string, name, planet)
        self._department = department

class Soldier(Person):
    def __init__(self, id_string: str, name:str , planet: "Planet", age: int) -> None:
        super().__init__(id_string, name, planet)
        self._age = age

class Primarch(Person):
    id = 0
    def __init__(self, name: str ,alias: str, planet: "Planet", loyalty: bool= False, status: "Status" = None, imperium:"Imperium"= None) -> None:
        
        
        idHex = hex(Primarch.id)
        if Primarch.id <= 15:
            id_string = "00000" + idHex[2:]
            self.__id = id_string
        else:
            id_string = "0000" + idHex[2:]
            self.__id = id_string
        super().__init__(id_string, name, planet)
        Primarch.id += 1
        self.__alias = alias
        self.__loyalty = loyalty
        self.__status = status
        self.__imperium = imperium
        ##add this primarch to the imperium

    @property
    def name(self) -> str:
        return self._name


        

    
