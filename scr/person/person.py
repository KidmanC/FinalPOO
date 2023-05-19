from abc import ABC, abstractmethod
from utils.enumeration import Status

class Person(ABC): # Abstract class
    id = 0
    def __init__(self, name:str , planet: "Planet") -> None:
        idHex = hex(Person.id)
        id_string = idHex[2:]
        id_string = id_string.zfill(6)
        self._id_string = id_string
        
        Person.id += 1
        self._name = name
        self._planet = planet


class Astarte (Person):
    def __init__(self, name:str , founding: int, planet: "Planet") -> None:
        super().__init__(name, planet)
        self.__founding = founding

class Bureaucrat(Person):
    def __init__(self, name:str, department: str, planet: "Planet") -> None:
        super().__init__(name, planet)
        self.__department = department
        self.__dicc = {}

    @property
    def name(self) -> str:
        return self._name+" "+self._id_string
    
    @property
    def dicc(self) -> str:
        return self.__dicc
    
    @property
    def id_string (self) -> str:
        return self._id_string

class Soldier(Person):
    def __init__(self, name:str, age: int, planet: "Planet") -> None:
        super().__init__(name, planet)
        self._age = age

class Primarch(Person):
    def __init__(self, name: str ,alias: str, planet: "Planet", loyalty: bool= True, 
                 status: "Status" = Status.ALIVE.value , imperium:"Imperium"= None) -> None:
        
        super().__init__(name, planet)
        self.__alias = alias
        self.__loyalty = loyalty
        self.__status = status
        self.__imperium = imperium
        if self.__imperium is not None:
            self.__imperium.add_primarch(self)
        ##add this primarch to the imperium(done)

    def betray(self):
        print(f"Primach {self._name} betrays the Emperor")
        self.__loyalty = False

    def change_status(self, status:"Status"):
        self.__status = status.value

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def alias(self) -> str:
        return self.__alias

    @property
    def loyal(self) -> str:
        return self.__loyalty
    
    @property
    def status(self) -> str:
        return self.__status
    
    @property
    def planet(self) -> str:
        return self._planet
    
    @property
    def id_string(self) -> str:
        return self._id_string
    
    @property
    def imperium(self) -> "Imperium":
        return self.__imperium

        

    
