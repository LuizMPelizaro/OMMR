from enum import Enum


class TypeTyre(Enum):
    ULTRASOFT = 'ultra_soft'
    SUPERSOFT = 'super_soft'
    SOFT = 'soft'
    MEDIUM = 'medium'
    HARD = 'hard'
    INTERMEDIATE = 'Intermediate'
    WET = 'wet'


class Tyre:
    def __init__(self, json, position):
        if isinstance(json['tyres'][position]['type'], TypeTyre):
            raise ValueError('The tire type must be a value from the TireType enum')
        self.__type_tyre = json['tyres'][position]['type']
        self.__condition = json['tyres'][position]['condition']
        self.__max_laps = json['tyres'][position]['max']
        self.__min_laps = json['tyres'][position]['min']

    @property
    def type_tyre(self):
        return self.__type_tyre

    @property
    def max_laps(self):
        return self.__max_laps

    @property
    def min_laps(self):
        return self.__min_laps
