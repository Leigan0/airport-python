class Plane:

    def __init__(self):
        self.flying = None

    def land(self):
        self.flying = False

    def take_off(self):
        self.flying = True
