from typing import List
#from general.emperor import Emperor
from person.person import Primarch
from general.administratum import Administratum
from general.astra_militarum import AstraMilitarum
from general.adeptus_astartes import AdeptusAstartes
from general.segmentum import Segmentum
from utils.planet import Planet

planetas = []
i=0
class Imperium:

    __INSTANCE = None
    

    def __init__(self, emperor: "Emperor", name: str, planet: "Planet",segmentums: List["Segmentum"], 
                 primarchs: List["Primarch"] = None, adeptus_astartes: "AdeptusAstartes"=None, 
                 administratum: "Administratum"= None, astra_militarum: "AstraMilitarum"=None ) -> None:
        self.__emperor = emperor
        self.__name = name
        self.__primarchs =  [] if primarchs is None else primarchs
        self.__adeptus_astartes = adeptus_astartes
        self.__administratum = administratum
        self.__astra_militarum = astra_militarum
        self.__segmentums = [] if segmentums is None else segmentums
        self.__planet = planet
        Imperium.__INSTANCE = self
        ##add this imperium to the emperor

    def add_segmentum(self, segmentum: "Segmentum") -> None:
        self.__segmentums.append(segmentum)
        print(f"Added segmentum {segmentum.name} to Imperium" )
        #Added Segmentum Solar to the Imperium

    def get_instance() -> "Imperium":
        return Imperium.__INSTANCE
    
    def add_primarch(self, primarch: "Primarch") -> None:
        if len(self.__primarchs) == 20:
            print("RuntimeError: There can only be 20 Primarchs")
            return
        
        self.__primarchs.append(primarch)
        if primarch is not None:
            print(f"The emperor created Primarch {primarch.name}")
    
    @property
    def primarchs(self) -> List["Primarch"]:
        return self.__primarchs
    
    def add_bureaucrat(self, bureaucrat: "Bureaucrat") -> None:
        planet_registry=[]
        planet_registry.append(i)
        administratum = Administratum (planet_registry, bureaucrat)
        self.__administratum = administratum
        print(f"{bureaucrat.name} {bureaucrat.id_string} started to work at Imperium")
        i+=1
    
    def get_bureaucrat(self, index: int) -> "Bureaucrat":
        return self.__administratum.bureaucrats[index]

    def register_planet(self, bureaucrat: "Bureaucrat", info: dict):
        if planetas == []:
            self.__administratum.planet_registry.append(i)
            planetas.append(Planet(info['planet_name'], info['planet_type']))
        
        else:
            for planeta in planetas:
                if (planeta.name == info['planet_name']):
                    print(f"RuntimeError: Planet already registered")
                    return
            self.__administratum.planet_registry.append(i)
            planetas.append(Planet(info['planet_name'], info['planet_type']))
            

        



 
    def segmentum(self, segmentum: "Segmentum") -> bool:
        bool = False
        for seg in self.__segmentums:
            if(seg.name == segmentum.name):
                bool = True
                return bool
        return bool
        