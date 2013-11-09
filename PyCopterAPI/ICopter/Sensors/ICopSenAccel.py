# Python imports
from abc import ABCMeta, abstractmethod

# Our imports
from PyCopterAPI.ICopter.Event import Event

class ICopSenAccel:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.gotAccelEvent = Event()

    @abstractmethod
    def start(self): pass

    @abstractmethod
    def start(self): pass
