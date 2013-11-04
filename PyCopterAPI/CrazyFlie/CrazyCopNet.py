from json import scanner
from PyCopterAPI.CrazyFlie.cflib.crtp import init_drivers, scan_interfaces
from PyCopterAPI.ICopter.ICopNet import ICopNet
from PyCopterAPI.CrazyFlie.cflib.crazyflie import  Crazyflie

class CrazyCopNet(ICopNet):
    def __init__(self):
        super(CrazyCopNet, self).__init__()
        pass
    def connect(self):

        pass
    def disconnect(self):
        pass