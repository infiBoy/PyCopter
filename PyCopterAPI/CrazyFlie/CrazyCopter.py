


# import the abstract class
from PyCopterAPI.ICopter.ICopter import ICopter

# importing the network and movement
from PyCopterAPI.CrazyFlie.CrazyCopNet import CrazyCopNet
from PyCopterAPI.CrazyFlie.CrazyCopMov import CrazyCopMov

# Importing crazyflie sensors
from PyCopterAPI.CrazyFlie.Sensors.CrazySenAccel import CrazySenAccel
from PyCopterAPI.CrazyFlie.Sensors.CrazySenGyro import CrazySenGyro

class CrazyCopter(ICopter):
    def __init__(self):
        super(CrazyCopter, self).__init__()

        # Add the network
        self.network = CrazyCopNet()

        # Add the movement
        self.movement = CrazyCopMov()

        # Add the sensors
        self.sensors.setAccelSensor(CrazySenAccel())
        self.sensors.setGyroSensor(CrazySenGyro())
    def start(self): pass
    def stop(self): pass

