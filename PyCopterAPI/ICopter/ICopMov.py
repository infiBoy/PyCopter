# FileName : ICopMov.py
# Date : 31.10.2013
# Developers : Maxim Arav

from abc import ABCMeta, abstractmethod

class ICopMov:
    __metaclass__ = ABCMeta
    def __init__(self):
        pass
    def TakeOff(self):
        pass
    def Land(self):
        pass
    def CommandHover(self):
        pass
    def MoveLeft(self):
        pass
    def MoveRight(self):
        pass
    def MoveUp(self):
        pass
    def MoveDown(self):
        pass
    def MoveForward(self):
        pass
    def MoveBackword(self):
        pass
    def TurnLeft(self):
        pass
    def TurnRight(self):
        pass