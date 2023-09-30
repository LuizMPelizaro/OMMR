class TrackInfo:
    def __init__(self, json):
        self.__name = json['track_infos']['name']
        self.__lap_time = json['track_infos']['lap_time']
        self.__race_time = json['track_infos']['race_time']

    @property
    def name(self):
        return self.__name

    @property
    def lap_time(self):
        return self.__lap_time

    @property
    def race_time(self):
        return self.__race_time
