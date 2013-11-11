from abc import ABCMeta, abstractmethod
from PyCopterAPI.ICopter.Sensors.ISensor import ISensor

class ICopSenGps(ISensor):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(ICopSenGps, self).__init__()
        pass