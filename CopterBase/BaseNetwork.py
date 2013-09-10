from abc import ABCMeta, abstractmethod

class BaseNetwork():
    
   @abstractmethod
   def connect(self):
       pass
   @abstractmethod
   def disconnect(self):
       pass