import json
from pilot import Pilots
from track_Info import TrackInfo
from car_info import CarInfo
from type_of_race import TypeOfRace
from src.utils.utils import get_json
from tyres import Tyre


class Input:
    def __init__(self,
                 type_of_race: TypeOfRace,
                 list_of_pilot: Pilots,
                 track_infos: TrackInfo = None,
                 tyre: Tyre = None,
                 car_info: CarInfo = None):
        self.__type_of_race = type_of_race
        self.__pilots = list_of_pilot
        self.__track_infos = track_infos
        self.__tyre = tyre
        self.__car_info = car_info

    @property
    def type_of_race(self):
        return self.__type_of_race

    @property
    def pilots(self):
        return self.__pilots

    @property
    def track_infos(self):
        return self.__track_infos

    @property
    def tyres(self):
        return self.__tyre

    @property
    def car_info(self):
        return self.__car_info


if __name__ == '__main__':
    data = get_json('test')
    type_of_race = TypeOfRace(data)
    pilots = Pilots(data)
    track_info = TrackInfo(data)
    dry_tyres = Tyre(data, 0)
    car_info = CarInfo(data)
    Race = Input(type_of_race, pilots, track_info, dry_tyres, car_info)
    print(Race.type_of_race.type_of_race)
    print(Race.pilots.pilot_1)
    print(Race.pilots.pilot_2)
    print(Race.pilots.pilot_3)
    print(Race.track_infos.name)
    print(Race.track_infos.lap_time)
    print(Race.tyres.type_tyre)
    print(Race.car_info.fuel_capacity)
