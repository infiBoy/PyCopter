from abc import ABCMeta, abstractmethod

# Our imports
from PyCopterAPI.ICopter.Event import Event

class ICopSenGyro:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.gotGyroEvent = Event()

    @abstractmethod
    def start(self): pass

    @abstractmethod
    def start(self): pass