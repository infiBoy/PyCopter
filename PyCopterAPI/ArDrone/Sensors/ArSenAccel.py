from PyCopterAPI.ICopter.Sensors.ICopSenAccel import ICopSenAccel
from PyCopterAPI.ICopter.Sensors.AccelData import AccelData

class ArSenAccel(ICopSenAccel):
    def __init__(self):
        super(ArSenAccel, self).__init__()
    def start(self):
        self.gotAccelEvent(AccelData(1,1,1))
        pass
    def stop(self):
        pass