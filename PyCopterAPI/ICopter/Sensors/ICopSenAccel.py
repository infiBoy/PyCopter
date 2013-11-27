from abc import ABCMeta, abstractmethod

# Our imports
from PyCopterAPI.ICopter.Sensors.ISensor import ISensor
from PyCopterAPI.ICopter.Event import Event

class ICopSenAccel(ISensor):
    def __init__(self):
        super(ICopSenAccel, self).__init__()
        self.gotAccelEvent = Event()

    @abstractmethod
    def start(self): pass

    @abstractmethod
    def start(self): pass
