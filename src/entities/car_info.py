class CarInfo:
    def __init__(self, json):
        self.__fuel_capacity = json['car_info']['fuel_capacity']

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
