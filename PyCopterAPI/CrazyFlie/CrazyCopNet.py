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
        super(CrazyCopNet, self).__init__()

    def connect(self):
        # The os.setsid() is passed in the argument preexec_fn so
        # it's run after the fork() and before  exec() to run the shell.
        context = zmq.Context()

        #create this node as publisher
        self.socket = context.socket(zmq.PUB)
        self.socket.bind("tcp://*:25647")

        #try:
        #    self.process = subprocess.Popen("crazyflie-pc-client/bin/cfclient", stdout=subprocess.PIPE,
        #                           shell=True, preexec_fn=os.setsid)
        #except Exception:
        #    pass


    def disconnect(self):
        os.system("kill -KILL " + str(self.process.pid))

    def sendMessage(self, message):
        self.socket.send(message)

#temp test code
crazy = CrazyCopNet()
crazy.connect()


pygame.init()
pygame.display.set_mode((300,200))
pygame.display.set_caption("crazyflie controller")
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_w:
                crazy.sendMessage("1")
                sleep(0.1)
                crazy.sendMessage("3")
            elif event.key == K_s:
                crazy.sendMessage("2")
                sleep(0.1)
                crazy.sendMessage("3")
            elif event.key == K_a:
                crazy.sendMessage("4")
                sleep(0.1)
                crazy.sendMessage("3")
            elif event.key == K_d:
                crazy.sendMessage("5")
                sleep(0.1)
                crazy.sendMessage("3")
            elif event.key == K_p:
                crazy.sendMessage("6")
                sleep(0.1)
                crazy.sendMessage("3")

pygame.display.quit()
crazy.disconnect()