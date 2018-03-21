class Airport:

    def __init__(self):
        self.hangar = []

    def land(self, plane):
        self.hangar.append(plane)
        print self.hangar
