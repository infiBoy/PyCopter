# FileName : ICopter.py
# Date : 31.10.2013
# Developers : Maxim Arav

# Python imports
from abc import ABCMeta, abstractmethod

# our imports
from PyCopterAPI.ICopter.CopSensors import CopSensors
from PyCopterAPI.ICopter.CopterThreadPool import CopterThreadPool

# ICopter is abstract class that provides the basic parts of copter base
class ICopter:
  __metaclass__ = ABCMeta
  #constructor for basic properties
  def __init__(self):
      self.copterThreads = CopterThreadPool()
      self.movement = None
      self.network = None
      self.sensors = CopSensors(self)
  @abstractmethod
  def start(self): pass
  @abstractmethod
  def stop(self): pass


