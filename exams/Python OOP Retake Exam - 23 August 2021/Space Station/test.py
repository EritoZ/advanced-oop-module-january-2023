from project.astronaut.biologist import Biologist
from project.planet.planet import Planet
from project.space_station import SpaceStation

space_station = SpaceStation()

print(space_station.add_astronaut('Biologist', '???'))

print(space_station.add_planet('planet', 'adas, asdasd, asdag'))

print(space_station.send_on_mission('planet'))

