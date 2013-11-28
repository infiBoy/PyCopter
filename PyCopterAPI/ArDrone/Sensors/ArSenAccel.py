from PyCopterAPI.ICopter.Sensors.ICopSenAccel import ICopSenAccel
from PyCopterAPI.ICopter.Sensors.AccelData import AccelData

class ArSenAccel(ICopSenAccel):
    def __init__(self):
        super(ArSenAccel, self).__init__()
    def start(self):
        # TODO : think how to do it better
        self.senHolder.copter.network.navData.gotNavdataMessage += self.processNavMessage
    def stop(self):
         # TODO : think how to do it better
        self.senHolder.copter.network.navData.gotNavdataMessage -= self.processNavMessage
    def processNavMessage(self, navdata):
        if navdata.Accel != None:
            self.gotAccelEvent(navdata.Accel)