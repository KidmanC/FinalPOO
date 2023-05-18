from typing import List
from general.emperor import Emperor
from general.primarch import Primarch
from general.administratum import Administratum

class Imperium:
    def __init__(self, emperor: "Emperor", name: str, primarchs: List["Primarch"], adeptus_astartes: "AdeptusAstartes", 
                 administratum: "Administratum", astra_militarum: "AstraMilitarum", segmentums: List["Segmentum"], 
                 planet: "PLanet") -> None:
        self.__emperor = emperor
        self.__name = name
        self.__primarchs = primarchs
        self.__adeptus_astartes = adeptus_astartes
        self.__administratum = administratum
        self.__astra_militarum = astra_militarum
        self.__segmentums = segmentums
        self.__planet = planet
        ##add this imperium to the emperor
        