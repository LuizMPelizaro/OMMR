from enum import Enum


class RaceCategory(Enum):
    ENDURANCE = 'endurance'
    FORMULA = 'formula'
    GT = 'gt'


class TypeOfRace:
    def __init__(self, json):
        if isinstance(json['type_of_race'], RaceCategory):
            raise ValueError('Category of race is invalid !!')
        self.__type_of_race = json['type_of_race']

    @property
    def type_of_race(self):
        return self.__type_of_race
