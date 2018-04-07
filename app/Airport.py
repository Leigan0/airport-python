from Weather import Weather

class Airport:

    def __init__(self, weather):
        self.hangar = []
        self.weather = weather()
        self.DEFAULT_CAPACITY = 20

    def land(self, plane):
        self.__check_weather_status()
        self.__at_capacity()
        self.__add_plane_to_hangar(plane)

    def take_off(self, plane):
        self.__check_weather_status()
        self.hangar.remove(plane)
        plane.take_off()

    def __add_plane_to_hangar(self,plane):
        self.hangar.append(plane)
        plane.land()

    def __check_weather_status(self):
        if self.weather.is_stormy():
            raise Exception("Weather Stormy")

    def __at_capacity(self):
        if len(self.hangar) == self.DEFAULT_CAPACITY:
            raise Exception("Airport Full")
