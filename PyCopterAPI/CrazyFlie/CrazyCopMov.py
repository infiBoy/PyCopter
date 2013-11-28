from time import sleep
from PyCopterAPI.CrazyFlie.CrazyCopNet import CrazyCopNet
from PyCopterAPI.ICopter.ICopMov import ICopMov

class CrazyCopMov(ICopMov):
    def MoveDown(self):
        self.network.sendMessage("2")
        sleep(0.1)
        self.network.sendMessage("3")

    def MoveRight(self):
        self.network.sendMessage("7")
        sleep(0.1)
        self.network.sendMessage("3")

    def TakeOff(self):
        super(CrazyCopMov, self).TakeOff()

    def MoveUp(self):
        self.network.sendMessage("1")
        sleep(0.1)
        self.network.sendMessage("3")

    def TurnLeft(self):
        self.network.sendMessage("5")
        sleep(0.1)
        self.network.sendMessage("3")

    def MoveLeft(self):
        self.network.sendMessage("8")
        sleep(0.1)
        self.network.sendMessage("3")

    def MoveForward(self):
        self.network.sendMessage("9")
        sleep(0.1)
        self.network.sendMessage("3")

    def CommandHover(self):
        self.network.sendMessage("6")
        sleep(0.1)
        self.network.sendMessage("3")

    def Land(self):
        super(CrazyCopMov, self).Land()

    def TurnRight(self):
        self.network.sendMessage("4")
        sleep(0.1)
        self.network.sendMessage("3")

    def MoveBackword(self):
        self.network.sendMessage("0")
        sleep(0.1)
        self.network.sendMessage("3")

    def __init__(self, network):
        super(CrazyCopMov, self).__init__()
        self.network = network