from typing import List

class Planet:
    def __init__(self, name: str, type_: "PlanetType", chapter: "Chapter", regiments: List["Regiment"]) -> None:
        self.__name = name
        self.__type_ = type_
        self.__chapter = chapter
        self.__regiments = regiments
        ##add this planet to the regiment n the chapter
