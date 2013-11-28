from PyCopterAPI.ICopter.ICopMov import ICopMov

class CrazyCopMov(ICopMov):
    def MoveDown(self):
        super(CrazyCopMov, self).MoveDown()

    def MoveRight(self):
        super(CrazyCopMov, self).MoveRight()

    def TakeOff(self):
        super(CrazyCopMov, self).TakeOff()

    def MoveUp(self):
        super(CrazyCopMov, self).MoveUp()

    def TurnLeft(self):
        super(CrazyCopMov, self).TurnLeft()

    def MoveLeft(self):
        super(CrazyCopMov, self).MoveLeft()

    def MoveForward(self):
        super(CrazyCopMov, self).MoveForward()

    def CommandHover(self):
        super(CrazyCopMov, self).CommandHover()

    def Land(self):
        super(CrazyCopMov, self).Land()

    def TurnRight(self):
        super(CrazyCopMov, self).TurnRight()

    def MoveBackword(self):
        super(CrazyCopMov, self).MoveBackword()

    def __init__(self):
        super(CrazyCopMov, self).__init__()
        pass