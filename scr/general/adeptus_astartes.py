from typing import List
from utils.chapter import Chapter

class AdeptusAstartes:
    def __init__(self, chapters: List["Chapter"]) -> None:
        self.__chapters = [] if chapters is None else chapters