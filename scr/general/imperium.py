from typing import List
#from general.emperor import Emperor
from person.person import Primarch
from general.administratum import Administratum
from general.astra_militarum import AstraMilitarum
from general.adeptus_astartes import AdeptusAstartes
from general.segmentum import Segmentum
from utils.planet import Planet

class Imperium:

    __INSTANCE = None

    def __init__(self, emperor: "Emperor", name: str, planet: "Planet",segmentums: List["Segmentum"], 
                 primarchs: List["Primarch"]=None, adeptus_astartes: "AdeptusAstartes"=None, 
                 administratum: "Administratum"=None, astra_militarum: "AstraMilitarum"=None ) -> None:
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
        self.__primarchs.append(primarch)
        
    def segmentum(self, segmentum: "Segmentum") -> bool:
        bool = False
        for seg in self.__segmentums:
            if(seg.name == segmentum.name):
                bool = True
                return bool

        return bool
        