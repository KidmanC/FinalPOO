from abc import ABC, abstractmethod

class Person(ABC): # Abstract class
    id = 0
    def __init__(self, name:str , planet: "Planet") -> None:
        idHex = hex(Person.id)
        if Person.id <= 15:
            id_string = "00000" + idHex[2:]
            self._id_string = id_string
        else:
            id_string = "0000" + idHex[2:]
            self._id_string = id_string
        Person.id += 1
        self._name = name
        self._planet = planet


class Astarte (Person):
    def __init__(self, name:str , planet: "Planet", founding: int) -> None:
        super().__init__(name, planet)
        self.__founding = founding

class Bureaucrat(Person):
    def __init__(self, name:str, department: str, planet: "Planet") -> None:
        super().__init__(name, planet)
        self._department = department

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def id_string (self) -> str:
        return self._id_string

class Soldier(Person):
    def __init__(self, id_string: str, name:str , planet: "Planet", age: int) -> None:
        super().__init__(id_string, name, planet)
        self._age = age

class Primarch(Person):
    def __init__(self, name: str ,alias: str, planet: "Planet", loyalty: bool= False, 
                 status: "Status" = None, imperium:"Imperium"= None) -> None:
        
        super().__init__(name, planet)
        self.__alias = alias
        self.__loyalty = loyalty
        self.__status = status
        self.__imperium = imperium
        ##add this primarch to the imperium

    def betray(self):
        print(f"Primach {self._name} betrays the Emperor")

    def change_status(self, status:"Status"):
        self.__status = status

    @property
    def name(self) -> str:
        return self._name


        

    
