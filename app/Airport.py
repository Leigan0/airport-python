class Airport:

    def __init__(self):
        self.hangar = []

    def land(self, plane):
        self.hangar.append(plane)
        plane.land()

    def take_off(self, plane):
        self.hangar.remove(plane)
