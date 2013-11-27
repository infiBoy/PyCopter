import socket
from PyCopterAPI.ArDrone.ArMessages.ControlMessage import ControlMessage

ARDRONE_COMMAND_PORT = 5556

class CommandWorker():
    def __init__(self):
        self.seq = 0
    def SendCommand(self, ControlMessage):
        self.seq += 1
        message = ControlMessage.Encode(self.seq)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message, ("192.168.1.1", ARDRONE_COMMAND_PORT))

