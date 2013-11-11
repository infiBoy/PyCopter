from abc import ABCMeta, abstractmethod

from PyCopterAPI.ICopter.Sensors.ISensor import ISensor

class ICopSenCam(ISensor):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(ICopSenCam, self).__init__()
        pass
