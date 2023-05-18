from typing import List
from utils.chapter import Chapter
from utils.regiment import Regiment

class Planet:
    def __init__(self, name: str, type_: "PlanetType", chapter: "Chapter" = None, regiments: List["Regiment"] = None) -> None:
        self.__name = name
        self.__type_ = type_
        self.__chapter = chapter
        self.__regiments = [] if regiments is None else regiments
        ##add this planet to the regiment n the chapter
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def type_(self) -> "PlanetType":
        return self.__type_
