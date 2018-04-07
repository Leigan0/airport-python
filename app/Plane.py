class Plane:

    def __init__(self):
        self.flying = None

    def land(self):
        if self.flying == False:
            raise Exception("Plane already landed")
        self.flying = False

    def take_off(self):
        if self.flying:
            raise Exception("Plane already in air")
        self.flying = True
