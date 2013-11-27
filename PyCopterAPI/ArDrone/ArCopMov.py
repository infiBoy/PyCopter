from PyCopterAPI.ICopter.ICopMov import ICopMov
from PyCopterAPI.ArDrone.ArMessages.ControlMessage import ControlMessage
from PyCopterAPI.ICopter.Event import Event

class ArCopMov(ICopMov):
    def __init__(self):
        super(ArCopMov, self).__init__()
        self.makeCommand = Event()

    def TakeOff(self):
        # Create Messages
        trim = ControlMessage()
        trim.CommandFtrim()
        config = ControlMessage()
        config.CommandConfig("control:altitude_max", "20000")
        ref_msg = ControlMessage()
        ref_msg.CommandDroneState(True)

        # Doing command
        self.makeCommand(trim)
        self.makeCommand(config)
        self.makeCommand(ref_msg)

    def Land(self):
        ref_msg = ControlMessage()
        ref_msg.CommandDroneState(False)
        self.makeCommand(ref_msg)

    def CommandHover(self):
        msg = ControlMessage()
        msg.CommandHover()
        self.makeCommand(msg)

    def MoveLeft(self):
        msg = ControlMessage()
        msg.CommandMoveLeft()
        self.makeCommand(msg)

    def MoveRight(self):
        msg = ControlMessage()
        msg.CommandMoveRight()
        self.makeCommand(msg)

    def MoveUp(self):
        msg = ControlMessage()
        msg.CommandMoveUp()
        self.makeCommand(msg)

    def MoveDown(self):
        msg = ControlMessage()
        msg.CommandMoveDown()
        self.makeCommand(msg)

    def MoveForward(self):
        msg = ControlMessage()
        msg.CommandMoveForward()
        self.makeCommand(msg)

    def MoveBackword(self):
        msg = ControlMessage()
        msg.CommandMoveBackword()
        self.makeCommand(msg)

    def TurnLeft(self):
        msg = ControlMessage()
        msg.CommandTurnLeft()
        self.makeCommand(msg)

    def TurnRight(self):
        msg = ControlMessage()
        msg.CommandTurnRight()
        self.makeCommand(msg)