from general.imperium import Imperium
from general.segmentum import Segmentum
from utils.planet import Planet
from person.person import Primarch

class SingletonError(Exception):
    pass

class Emperor:
    __INSTANCE = None



    def __init__(self, imperium: "Imperium"= None) -> None:
        if not Emperor.__INSTANCE is None:
            raise SingletonError('There can only be one Emperor of Mankind')
        else:
            Emperor.__INSTANCE = self
            self.__imperium = imperium
            print("The Emperor of Mankind has arisen")
        ##add this emperor to the imperium (done)

    @property
    def imperium(self) -> "Imperium":
        return self.__imperium
    
    def create_imperium(self, name: str, info: dict) -> None:

        planet = Planet(info['planet_name'], info['planet_type'])
        segmentum = Segmentum(info['segmentum_name'], info['segmentum_location'])
        imperium = Imperium(self, name, planet, None )
        segmentum.add_planet(planet)
        
        print(f"The emperor created The Imperium of Mankind at planet {planet.name}")
        self.__imperium = imperium
        imperium.add_segmentum(segmentum)
        
        

    def create_primarch(self, name: str, alias: str = None, info: dict = None) -> None:

        if( info is None):
            print(f"The emperor created Primarch *****")
            self.__imperium.add_primarch(None)
        else:
            if self.__imperium.search_segmentum(info['segmentum_name']) == False:
                segmentum = Segmentum(info['segmentum_name'], info['segmentum_location'])
                self.__imperium.add_segmentum(segmentum)

                if self.__imperium.search_planet(info['planet_name']) == True:
                    planet= Planet(info['planet_name'], info['planet_type'])
                    primarch = Primarch(name= name, alias= alias, planet= planet)
                    self.__imperium.add_primarch(primarch)
                    return
                else:
                    planet= Planet(info['planet_name'], info['planet_type']) 
                    segmentum.add_planet(planet)
                    primarch = Primarch(name= name, alias= alias, planet= planet)
                    self.__imperium.add_primarch(primarch)
            else:
                segmentum = self.__imperium.get_segmentum(info['segmentum_name'])
                if self.__imperium.search_planet(info['planet_name']) == True:
                    planet= Planet(info['planet_name'], info['planet_type'])
                    primarch = Primarch(name= name, alias= alias, planet= planet)
                    self.__imperium.add_primarch(primarch)
                    return
                else:
                    planet= Planet(info['planet_name'], info['planet_type'])
                    segmentum.add_planet(planet)
                    primarch = Primarch(name= name, alias= alias, planet= planet)
                    self.__imperium.add_primarch(primarch)
            

    
    

