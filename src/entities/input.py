from pilot import Pilots
from src.math.math_functions import *
from track_Info import TrackInfo
from car_info import CarInfo
from type_of_race import TypeOfRace
from src.utils.utils import get_json
from tyres import Tyre
from risk import ErrorRisk


class Input:
    def __init__(self,
                 type_of_race: TypeOfRace,
                 risk: ErrorRisk,
                 list_of_pilot: Pilots,
                 track_infos: TrackInfo = None,
                 tyre: Tyre = None,
                 car_info: CarInfo = None):
        self.__type_of_race = type_of_race
        self.__risk = risk
        self.__pilots = list_of_pilot
        self.__track_infos = track_infos
        self.__tyre = tyre
        self.__car_info = car_info

    @property
    def type_of_race(self):
        return self.__type_of_race

    @property
    def risk(self):
        return self.__risk

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
    error = ErrorRisk(data)
    pilots = Pilots(data)
    track_info = TrackInfo(data)
    dry_tyres = Tyre(data, 0)
    car_info = CarInfo(data)
    Race = Input(type_of_race,error, pilots, track_info, dry_tyres, car_info)
    print(pilot_time(Race.risk.risk_of_pilot, Race.pilots.pilot_1))

