# FileName : ICopter.py
# Date : 31.10.2013
# Developers : Maxim Arav

from abc import ABCMeta, abstractmethod


# ICopter is abstract class that provides the basic parts of copter base
class ICopter:
  __metaclass__ = ABCMeta
  #constructor for basic properties
  def __init__(self):
      self.movement = None
      self.network = None
      self.sensors = None
  @abstractmethod
  def start(self): pass
  @abstractmethod
  def stop(self): pass


