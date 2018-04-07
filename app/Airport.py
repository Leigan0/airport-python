from Weather import Weather

class Airport:

    def __init__(self, weather):
        self.hangar = []
        self.weather = weather()

    def land(self, plane):
        self.__check_weather_status()
        self.hangar.append(plane)
        plane.land()

    def take_off(self, plane):
        self.hangar.remove(plane)
        plane.take_off()

    def __check_weather_status(self):
        if self.weather.is_stormy():
            raise Exception("Weather Stormy")
