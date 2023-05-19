from typing import List
#from general.emperor import Emperor
from person.person import Primarch
from general.administratum import Administratum
from general.astra_militarum import AstraMilitarum
from general.adeptus_astartes import AdeptusAstartes
from general.segmentum import Segmentum
from utils.planet import Planet
from utils.chapter import Chapter
from utils.regiment import Regiment


class Imperium:

    __INSTANCE = None

    def __init__(self, emperor: "Emperor", name: str, planet: "Planet",segmentums: List["Segmentum"], 
                 primarchs: List["Primarch"] = None, adeptus_astartes: "AdeptusAstartes"= None, 
                 astra_militarum: "AstraMilitarum"=None ) -> None:
        self.__emperor = emperor
        self.__name = name
        self.__primarchs =  [] if primarchs is None else primarchs
        self.__adeptus_astartes = AdeptusAstartes()
        self.__administratum = Administratum()
        self.__astra_militarum = AstraMilitarum()
        self.__segmentums = [] if segmentums is None else segmentums
        self.__planet = planet
        Imperium.__INSTANCE = self
        
        ##add this imperium to the emperor (done)

    def add_segmentum(self, segmentum: "Segmentum") -> None:
        self.__segmentums.append(segmentum)
        print(f"Added Segmentum {segmentum.name} to Imperium" )

    def get_instance() -> "Imperium":
        return Imperium.__INSTANCE
    
    def add_primarch(self, primarch: "Primarch") -> None:
        if len(self.__primarchs) == 20:
            print("RuntimeError: There can only be 20 Primarchs")
            return
        
        self.__primarchs.append(primarch)
        if primarch is not None:
            print(f"The Emperor created Primarch {primarch.name}")
    
    @property
    def primarchs(self) -> List["Primarch"]:
        return self.__primarchs
    
    def add_bureaucrat(self, bureaucrat: "Bureaucrat") -> None:
        self.__administratum.bureaucrats.append(bureaucrat)
        self.__administratum.planet_registry.append(0)

        print(f"{bureaucrat.name} {bureaucrat.id_string} started to work at Imperium")
    
    def get_bureaucrat(self, index: int) -> "Bureaucrat":
        return self.__administratum.bureaucrats[index]

    def register_planet(self, bureaucrat: "Bureaucrat", info: dict) -> None:
        planet = Planet(info["planet_name"], info['planet_type'])
        segmentu = info["segmentum_name"]
        for segmentum in self.__segmentums:
            if segmentum.name == segmentu:
                for planeta in segmentum.planets:
                    if planeta.name == info["planet_name"]:
                        print("RuntimeError: Planet already registered")
                        return
                segmentum.add_planet(planet)
                return
         
    @property
    def segmentums(self) -> str:
        return self.__segmentums

    def search_segmentum(self, name: str) -> bool:
        bool = False
        for segmentum in self.__segmentums:
            if(segmentum.name == name):
                bool = True
                return bool
        return bool
    
    def get_segmentum(self, name: str) -> "Segmentum":
        bool = False
        for segmentum in self.__segmentums:
            if(segmentum.name == name):
                return segmentum
        return bool
    
    def add_chapter(self, name: str, primarch: "Primarch", planet_name: str) -> None:

        chapter= Chapter(name, primarch, planet_name)
        self.__adeptus_astartes.chapters.append(chapter)
        print(f"Created Chapter {chapter.name} of {self.__adeptus_astartes.class_name}")

    def get_chapter(self, index: int) -> "Chapter":
        return self.__adeptus_astartes.chapters[index]
    
    def add_regiment(self, name: str, planet_name: str) -> None:
        for segmentum in self.__segmentums:
            planet= segmentum.get_planet(planet_name)
            if planet is not False:
                break
        regiment= Regiment(name, planet)
        self.__astra_militarum.regiments.append(regiment)
        print(f'Created Regiment {regiment.name} of {self.__astra_militarum.class_name}')

    def get_regiment(self, index: int) -> "Regiment":
        return self.__astra_militarum.regiments[index]
    
    def bureaucrat_max_registry(self):
        max = 0
        for bureaucrat in self.__administratum.bureaucrats:
            if bureaucrat.registry > max:
                max = bureaucrat.registry
        return max
        