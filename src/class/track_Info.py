class TrackInfo:
    def __init__(self, json):
        self.__name = json['track_infos']['name']
        self.__lap_time = json['track_infos']['lap_time']

    @property
    def name(self):
        return self.__name

    @property
    def lap_time(self):
        return self.__lap_time
