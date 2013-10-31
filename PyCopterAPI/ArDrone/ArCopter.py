from PyCopterAPI.ICopter.ICopter import ICopter
from PyCopterAPI.ArDrone.Sensors.ArSenAccel import ArSenAccel
from PyCopterAPI.ArDrone.ArCopNet import ArCopNet
from PyCopterAPI.ArDrone.ArCopMov import ArCopMov
from PyCopterAPI.ArDrone.Sensors.ArSenFrontCam import ArSenFrontCam
from PyCopterAPI.ArDrone.Sensors.ArSenGyro import ArSenGyro
from PyCopterAPI.ArDrone.Sensors.ArSenBottomCam import ArSenBottomCam

class ArCopter(ICopter):
    def __init__(self):
        super(ArCopter, self).__init__()

        # Adds the network
        self.network = ArCopNet()

        # Adds the movement
        self.movement = ArCopMov()

        # Add the sensors of ArDrone
        self.sensors.setAccelSensor(ArSenAccel())
        self.sensors.setGyroSensor(ArSenGyro())
        self.sensors.addCamera(ArSenBottomCam())
        self.sensors.addCamera(ArSenFrontCam())
    def start(self): pass
    def stop(self): pass
