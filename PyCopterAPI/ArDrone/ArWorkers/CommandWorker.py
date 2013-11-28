import socket, threading,time
from PyCopterAPI.ArDrone.ArMessages.ControlMessage import ControlMessage

ARDRONE_COMMAND_PORT = 5556

class CommandWorker():
    def __init__(self):
        self.seq = 0
        self.keepAliveThread = threading.Thread(target=self.SendKeepAlive)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def StartWorker(self):
        self.keepAliveThread.start()
    def SendKeepAlive(self):
          while 1:
            watchDog = ControlMessage()
            watchDog.CommandWatchDog()
            self.SendCommand(watchDog)
            # Sleep for 2000 ms and then send an is alive message
            #time.sleep(2000.0/1000000.0)
            time.sleep(5000.0/1000000.0)
    def SendCommand(self, ControlMessage):
        self.seq += 1
        message = ControlMessage.Encode(self.seq)
        self.sock.sendto("\x01\x00\x00\x00", ("192.168.1.1", ARDRONE_COMMAND_PORT))
        self.sock.sendto(message, ("192.168.1.1", ARDRONE_COMMAND_PORT))

