from enum import Enum


class Risk(Enum):
    HIGH = 'high'
    MEDIUM = 'medium'


class ErrorRisk:
    def __init__(self, json):
        if isinstance(json['risk_of_pilot'], Risk):
            raise ValueError('Category of race is invalid !!')
        self.__risk_of_pilot = json['risk_of_pilot']

    @property
    def risk_of_pilot(self):
        return self.__risk_of_pilot
