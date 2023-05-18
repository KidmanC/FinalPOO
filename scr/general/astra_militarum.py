from typing import List
from utils.regiment import Regiment

class AstraMilitarum:
    def __init__(self, regiments: List["Regiment"]) -> None:
        self.__regiments = [] if regiments is None else regiments