from json import scanner
from time import sleep
import pygame
import zmq
from PyCopterAPI.ICopter.ICopNet import ICopNet
import os
import signal
import subprocess
from pygame.locals import *

class CrazyCopNet(ICopNet):
    def __init__(self):
        super(CrazyCopNet, self)

    def connect(self):
        # The os.setsid() is passed in the argument preexec_fn so
        # it's run after the fork() and before  exec() to run the shell.
        context = zmq.Context()

        #create this node as publisher
        self.socket = context.socket(zmq.PUB)
        self.socket.bind("tcp://*:25647")

        try:
            self.process = subprocess.Popen("crazyflie-pc-client/bin/cfclient", stdout=subprocess.PIPE,
                                   shell=True, preexec_fn=os.setsid)
        except Exception:
            pass


    def disconnect(self):
        os.system("kill -KILL " + str(self.process.pid))

    def sendMessage(self, message):
        self.socket.send(message)