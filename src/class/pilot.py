class Pilots:
    def __init__(self, json):
        self.__pilot_1 = json['pilots'][0]['stamina']
        self.__pilot_2 = json['pilots'][1]['stamina']
        self.__pilot_3 = json['pilots'][2]['stamina']

    @property
    def pilot_1(self):
        return self.__pilot_1

    @property
    def pilot_2(self):
        return self.__pilot_2

    @property
    def pilot_3(self):
        return self.__pilot_3
