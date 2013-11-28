


# import the abstract class
import pygame
from pygame.locals import *
from time import sleep
from PyCopterAPI.ICopter.ICopter import ICopter

# importing the network and movement
from PyCopterAPI.CrazyFlie.CrazyCopNet import CrazyCopNet
from PyCopterAPI.CrazyFlie.CrazyCopMov import CrazyCopMov

# Importing crazyflie sensors
from PyCopterAPI.CrazyFlie.Sensors.CrazySenAccel import CrazySenAccel
from PyCopterAPI.CrazyFlie.Sensors.CrazySenGyro import CrazySenGyro

class CrazyCopter(ICopter):
    def __init__(self):
        super(CrazyCopter, self).__init__()

        # Add the network
        self.network = CrazyCopNet()

        # Add the movement
        self.movement = CrazyCopMov(self.network)

        # Add the sensors
        self.sensors.setAccelSensor(CrazySenAccel())
        self.sensors.setGyroSensor(CrazySenGyro())
    def start(self):
        self.network.connect()
    def stop(self):
        self.network.disconnect()


crazy = CrazyCopter()
crazy.start()

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
            elif event.key == K_q:
                crazy.movement.MoveUp()
            elif event.key == K_e:
                crazy.movement.MoveDown()
            elif event.key == K_w:
                crazy.movement.MoveForward()
            elif event.key == K_s:
                crazy.movement.MoveBackword()
            elif event.key == K_k:
                crazy.movement.MoveLeft()
            elif event.key == K_l:
                crazy.movement.MoveRight()
            elif event.key == K_a:
                crazy.movement.TurnLeft()
            elif event.key == K_d:
                crazy.movement.TurnRight()
            elif event.key == K_p:
                crazy.movement.CommandHover()

pygame.display.quit()
crazy.stop()

crazy.stop()