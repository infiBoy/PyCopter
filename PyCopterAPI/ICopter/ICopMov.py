# FileName : ICopMov.py
# Date : 31.10.2013
# Developers : Maxim Arav

from abc import ABCMeta, abstractmethod

class ICopMov:
    __metaclass__ = ABCMeta
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def TakeOff(self):
        pass
    @abstractmethod
    def Land(self):
        pass
    @abstractmethod
    def CommandHover(self):
        pass
    @abstractmethod
    def MoveLeft(self):
        pass
    @abstractmethod
    def MoveRight(self):
        pass
    @abstractmethod
    def MoveUp(self):
        pass
    @abstractmethod
    def MoveDown(self):
        pass
    @abstractmethod
    def MoveForward(self):
        pass
    @abstractmethod
    def MoveBackword(self):
        pass
    @abstractmethod
    def TurnLeft(self):
        pass
    @abstractmethod
    def TurnRight(self):
        pass