import struct

class ControlMessage():
    def __init__(self):
        self.command = ""
        self.params = []
        self.speed = 0.2

    def f2i(self, f):
        """Interpret IEEE-754 floating-point value as signed integer.
        Arguments:
        f -- floating point value
        """
        return struct.unpack('i', struct.pack('f', f))[0]

    def CommandConfig(self, option, value):
        """Set configuration parameters of the drone."""
        self.command = "CONFIG"
        self.params =  [str(option), str(value)]

    def CommandHover(self):
        """Make the drone hover."""
        self.CommandMove(False, 0, 0, 0, 0)

    def CommandMoveLeft(self):
        """Make the drone move left."""
        self.CommandMove(True, -self.speed, 0, 0, 0)

    def CommandMoveRight(self):
        """Make the drone move right."""
        self.CommandMove(True, self.speed, 0, 0, 0)

    def CommandMoveUp(self):
        """Make the drone rise upwards."""
        self.CommandMove(True, 0, 0, self.speed, 0)

    def CommandMoveDown(self):
        """Make the drone decent downwards."""
        self.CommandMove(True, 0, 0, -self.speed, 0)

    def CommandMoveForward(self):
        """Make the drone move forward."""
        self.CommandMove(True, 0, -self.speed, 0, 0)

    def CommandMoveBackword(self):
        """Make the drone move backwards."""
        self.CommandMove(True, 0, self.speed, 0, 0)

    def CommandTurnLeft(self):
        """Make the drone rotate left."""
        self.CommandMove(True, 0, 0, 0, -self.speed)

    def CommandTurnRight(self):
        """Make the drone rotate right."""
        self.CommandMove(True, 0, 0, 0, self.speed)

    def CommandTrimm(self):
        """Flat trim the drone."""
        self.command = "FTRIM"
        self.params = []

    def CommandSetSpeed(self, speed):
        """Set the drone's speed.

        Valid values are floats from [0..1]
        """
        self.speed = speed

    def CommandFtrim(self):
        self.command = "FTRIM"
        self.params = []

    def CommandDroneState(self, takeoff, emergency=False):
        p = 0b10001010101000000000000000000
        if takeoff:
            p += 0b1000000000
        if emergency:
            p += 0b0100000000
        self.command = "REF"
        self.params = [p]

    def CommandWatchDog(self):
        self.command = "COMWDG"
        self.params = []

    def CommandMove(self, progressive, lr, fb, vv, va):
     p = 1 if progressive else 0
     self.command = "PCMD"
     self.params = [p, float(lr), float(fb), float(vv), float(va)]

    def Encode(self, seq):
        """
        Parameters:
        command -- the command
        seq -- the sequence number
        params -- a list of elements which can be either int, float or string
        """
        param_str = ''
        for p in self.params:
            if type(p) == int:
                param_str += ",%d" % p
            elif type(p) == float:
                param_str += ",%d" % self.f2i(p)
            elif type(p) == str:
                param_str += ',"'+p+'"'
        return "AT*%s=%i%s\r" % (self.command, seq, param_str)

