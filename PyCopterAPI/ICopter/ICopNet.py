# FileName : ICopNet.py
# Date : 31.10.2013
# Developers : Maxim Arav

from abc import ABCMeta, abstractmethod

class ICopNet:
    __metaclass__ = ABCMeta
    def __init__(self, copter):
        self.copter = copter
    @abstractmethod
    def connect(self): pass
    @abstractmethod
    def disconnect(self): pass
    @abstractmethod
    def sendMessage(self,message): pass
