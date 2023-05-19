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
from utils.enumeration import PlanetType


class Imperium:

    __INSTANCE = None
    roman =["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", 
            "XVII", "XVIII", "XIX", "XX"]

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

        print(f"{bureaucrat.name} started to work at Imperium")
        bureaucrat.dicc['Planetas'] = 0
    
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
                bureaucrat.dicc['Planetas'] += 1
                        
            
         
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
    
    def search_planet(self, info: dict) -> bool:
        for segmentum in self.__segmentums:
            for planet in segmentum.planets:
                if planet.name == info:
                    return True
        return False
    
    def get_planet(self, name: str) -> "Planet":
        for segmentum in self.__segmentums:
            for planet in segmentum.planets:
                if planet.name == name:
                    return planet
        return False
    
    def get_segmentum(self, name: str) -> "Segmentum":
        bool = False
        for segmentum in self.__segmentums:
            if(segmentum.name == name):
                return segmentum
        return bool
    
    def add_chapter(self, name: str, primarch: "Primarch", planet_name: str) -> None:

        planet= self.get_planet(planet_name)
        chapter= Chapter(name, primarch, planet)
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
        maxlist = [1,0]
        for bureaucrat in self.__administratum.bureaucrats:
            if bureaucrat.dicc['Planetas'] > max:
                max = bureaucrat.dicc['Planetas']
                maxlist[0] = bureaucrat
                maxlist[1] = max
        return maxlist
    
    def planet_type_quantity(self):
        dictio = {}
        for segmentum in self.__segmentums:
            for planet in segmentum.planets:
                if planet.type_ not in dictio:
                    dictio[planet.type_] = 1
                else:
                    dictio[planet.type_] += 1
        print(f'---------- Planet Type ----------')
        print(f'- Agri Planet Quantity = {dictio[PlanetType.AGRI]}')
        print(f'- Civilised Planet Quantity = {dictio[PlanetType.CIVILISED]}')
        print(f'- Daemon Planet Quantity = {dictio[PlanetType.DAEMON]}')
        print(f'- Dead Planet Quantity = {dictio[PlanetType.DEAD]}')
        print(f'- Death Planet Quantity = {dictio[PlanetType.DEATH]}')
        print(f'- Feral Planet Quantity = {dictio[PlanetType.FERAL]}')
        print(f'- Feudal Planet Quantity = {dictio[PlanetType.FEUDAL]}')
        print(f'- Forge Planet Quantity = {dictio[PlanetType.FORGE]}')
        print(f'- Frointer Planet Quantity = {dictio[PlanetType.FRONTIER]}')
        print(f'- Hive Planet Quantity = {dictio[PlanetType.HIVE]}\n')

    a=0
    def show_primarchs_summary(self):
        print(f'---------- Primarchs Summary ----------')
        for primarch in self.__primarchs:
            if primarch == None:
                print(f'- Primarch {Imperium.roman[Imperium.a]}')
                print(f' - Purged from Imperial Registry\n')
                Imperium.a += 1
            else:  

                print(f'- Primarch {Imperium.roman[Imperium.a]}')
                print(f' - ID: {primarch.id_string}')
                print(f' - Name: {primarch.name}')
                print(f' - Alias: {primarch.alias}')
                print(f' - Loyal: {primarch.loyal}')
                print(f' - Status: {primarch.status}')
                print(f' - Planet: {primarch.planet.name}')
                print(f'   - Astra Militarum Regiments Quantity: {primarch.planet.regiments_quantity()}')
                if primarch.planet.regiments_quantity() == 0:
                    print(f'   - Astra Militarum Total Soldiers: 0')
                else:
                    print(f'   - Astra Militarum Total Soldiers: {primarch.planet.astra_militarum_total_soldiers()}')
                print(f'   - Adeptus Astates Chapter: {primarch.planet.chapter.name}')
                if primarch.planet.chapter.successor_chapters == []:
                    print(f'     - Successor Chapters:\n')
                else:
                    print(f'     - Successor Chapters: ')
                    print(f'      -{primarch.planet.chapter.successor_chapters[-1].name}\n')
                
                Imperium.a += 1

        