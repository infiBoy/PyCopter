#Todo: use abstract class using abc
#for more info at abc , goto : http://docs.python.org/2/library/abc.html
class BaseInfo(object):  
  #constructor for basic properties
  def __init__(self):
    self.name = None
    self.id = None
    self.type = None #the type of the drone
    
    #dimension of the drone
    self.height = None
    self.width  = None
    self.depth  = None
    
    self.connectivityType = None # i.e : Wifi, 5GHZ and etc..
    
  
  
    def Move(): 
        pass