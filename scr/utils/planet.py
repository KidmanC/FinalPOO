from typing import List
from utils.chapter import Chapter
from utils.regiment import Regiment

class Planet:
    def __init__(self, name: str, type_: "PlanetType", chapter: "Chapter" = None, regiments: List["Regiment"] = None) -> None:
        self.__name = name
        self.__type_ = type_
        self.__chapter = chapter
        self.__regiments = [] if regiments is None else regiments
        if chapter is not None:
            self.__chapter.add_planet(self)
        for regiment in self.__regiments:
            regiment.add_planet(self)
        ##add this planet to the regiment n the chapter (done)
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def type_(self) -> "PlanetType":
        return self.__type_
    
    def add_regiment(self, regiment: "Regiment"):
        self.__regiments.append(regiment)
