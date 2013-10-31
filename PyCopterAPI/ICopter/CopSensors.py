# FileName : CopSensors.py
# Date : 31.10.2013
# Developers : Maxim Arav

class CopSensors:
    def __init__(self):
        self.accelSensor = None
        self.gyroSensor = None
        self.gpsSensor = None
        self.cameras = {}
    def setAccelSensor(self, accel):
        self.accelSensor = accel
    def setGyroSensor(self, gyro):
        self.gyroSensor = gyro
    def setGpsSensor(self, gps):
        self.gpsSensor = gps
    def addCamera(self, camera):
        self.cameras.items().append(camera)
    def getAccelSensor(self):
        return self.accelSensor
    def getGyroSensor(self):
        return self.gyroSensor
    def getGpsSensor(self):
        return self.gpsSensor
    def getCameras(self):
        return self.cameras
