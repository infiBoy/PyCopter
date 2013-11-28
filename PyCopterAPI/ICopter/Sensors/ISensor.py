# FileName : ISensor.py
# Date : 09.11.2013
# Developers : Maxim Arav

from abc import ABCMeta, abstractmethod

class ISensor:

    __metaclass__ = ABCMeta

    def __init__(self):
        self.senHolder = None
        pass

    def setSensorsHolder(self, sensors):
        self.senHolder = sensors