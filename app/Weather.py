import random

class Weather:

    def __init__(self):
        self.stormy = None

    def is_stormy(self):
         self.stormy = (self.check_weather() < 2)
         return self.stormy

    def check_weather(self):
        return random.randint(0,5)
