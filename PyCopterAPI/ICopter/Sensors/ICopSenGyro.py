from abc import ABCMeta, abstractmethod

# Our imports
from PyCopterAPI.ICopter.Event import Event
from PyCopterAPI.ICopter.Sensors.ISensor import ISensor

class ICopSenGyro(ISensor):

    def __init__(self):
        super(ICopSenGyro, self).__init__()
        self.gotGyroEvent = Event()

    @abstractmethod
    def start(self): pass

    @abstractmethod
    def start(self): pass