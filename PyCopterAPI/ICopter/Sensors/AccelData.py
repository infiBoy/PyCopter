# FileName : AccelData.py
# Date : 09.11.2013
# Developers : Maxim Arav

class AccelData():
    def __init__(self, vx, vy, vz):
        self.vx = vx
        self.vy = vy
        self.vz = vz
    @property
    def VectorX(self):
        return self.vx
    @VectorX.setter
    def VectorX(self, value):
        self.vx = value

    @property
    def VectorY(self):
        return self.vy
    @VectorY.setter
    def VectorY(self, value):
        self.vy = value

    @property
    def VectorZ(self):
        return self.vz
    @VectorZ.setter
    def VectorZ(self,value):
        self.vz = value

