from typing import List
from person.person import Primarch
from person.person import Astarte

class Chapter:
    def __init__(self, name: str, primarch: "Primarch", planet: "Planet", astartes: List["Astarte"] = None, 
                 successor_chapters: List["Chapter"] = None) -> None:
        self.__name = name
        self.__primarch = primarch
        self.__planet = planet
        self.__astartes = [] if astartes is None else astartes
        self.__successor_chapters = [] if successor_chapters is None else successor_chapters
        ##add this chapter to the chapter(done)
        self.__planet.add_chapter(self)

    @property
    def name(self):
        return self.__name
    
    @property
    def successor_chapters(self):
        return self.__successor_chapters
    
    def add_successor_chapter (self, chapter: "Chapter"):
        self.__successor_chapters.append(chapter)
        print(f'Added Successor Chapter {chapter.name} to Chapter {self.name}')

    def add_astarte(self, astarte: "Astarte"):
        if len(self.__astartes)<1000:
            self.__astartes.append(astarte)
            #print(f'Added Astarte {astarte.name} to Chapter {self.name}')
        else:
            print(f'Chapter {self.name} is full')
            print(f'RuntimeError: There can only be 1000 Astartes per Chapter')

    def add_planet(self, planet: "Planet"):
        self.__planet = planet
        
