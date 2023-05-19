from typing import List
from utils.regiment import Regiment

class AstraMilitarum:
    def __init__(self, regiments: List["Regiment"] = None) -> None:
        self.__regiments = [] if regiments is None else regiments

    @property
    def regiments(self):
        return self.__regiments
    
    @property
    def class_name(self) -> str:
        return  "Astra Militarum"