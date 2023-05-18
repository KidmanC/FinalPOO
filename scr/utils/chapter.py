from typing import List
from person.person import Primarch
from person.person import Astarte

class Chapter:
    def __init__(self, name: str, primarch: "Primarch", planet: "Planet", astartes: List["Astarte"], successor_chapters: List["Chapter"]) -> None:
        self.__name = name
        self.__primarch = primarch
        self.__planet = planet
        self.__astartes = [] if astartes is None else astartes
        self.__successor_chapters = [] if successor_chapters is None else successor_chapters
        ##add this chapter to the chapter