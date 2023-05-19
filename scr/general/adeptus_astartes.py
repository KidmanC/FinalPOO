from typing import List
from utils.chapter import Chapter

class AdeptusAstartes:
    def __init__(self, chapters: List["Chapter"] = None) -> None:
        self.__chapters = [] if chapters is None else chapters

    @property
    def chapters(self) -> List["Chapter"]:
        return self.__chapters
    
    @property
    def class_name(self) -> str:
        return  "Adeptus Astartes"