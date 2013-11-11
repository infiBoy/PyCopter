# FileName : CopSensors.py
# Date : 31.10.2013
# Developers : Maxim Arav

from PyCopterAPI.ICopter.Sensors.ICopSenAccel import ICopSenAccel

class CopSensors:
    def __init__(self, copter):
        self.copter = copter
        self.accelSensor = None
        self.gyroSensor = None
        self.gpsSensor = None
        self.cameras = {}

    def setAccelSensor(self, accel):
        accel.setSensorsHolder(self)
        self.accelSensor = accel
    def setGyroSensor(self, gyro):
        gyro.setSensorsHolder(self)
        self.gyroSensor = gyro
    def setGpsSensor(self, gps):
        gps.setSensorsHolder(self)
        self.gpsSensor = gps
    def addCamera(self, camera):
        camera.setSensorsHolder(self)
        self.cameras.items().append(camera)

    def getAccelSensor(self):
        return self.accelSensor
    def getGyroSensor(self):
        return self.gyroSensor
    def getGpsSensor(self):
        return self.gpsSensor
    def getCameras(self):
        return self.cameras

