from PyCopterAPI.ICopter.Sensors.ICopSenGyro import ICopSenGyro

from PyCopterAPI.ICopter.Sensors.GyroData import GyroData

class ArSenGyro(ICopSenGyro):
    def __init__(self):
        super(ArSenGyro, self).__init__()
        pass
    def start(self):
        # TODO : think how to do it better
        self.senHolder.copter.network.navData.gotNavdataMessage += self.processNavMessage
        pass
    def stop(self):
        # TODO : think how to do it better
        self.senHolder.copter.network.navData.gotNavdataMessage -= self.processNavMessage
        pass
    def processNavMessage(self, navdata):
        self.gotGyroEvent(navdata.Gyro())