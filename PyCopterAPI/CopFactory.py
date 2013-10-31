# The implementation imports
from PyCopterAPI.CrazyFlie.CrazyCopter import CrazyCopter
from PyCopterAPI.ArDrone.ArCopter import ArCopter

class CopFactory(object):
    def factory(type):
        if type == "ArDrone": return ArCopter()
        elif type == "CrazyFlie" : return CrazyCopter()
        else: return  None
    factory = staticmethod(factory)
