# FileName : NavdataWorker.py
# Date : 09.11.2013
# Developers : Maxim Arav

# Python imports
import threading, socket, time, struct

# Our imports
from PyCopterAPI.ICopter.Event import Event
from PyCopterAPI.ArDrone.ArMessages.NavdataMessage import NavdataMessage
from PyCopterAPI.ArDrone.ArMessages.ControlMessage import ControlMessage
from PyCopterAPI.ICopter.Sensors.GyroData import GyroData

# Define consts
ARDRONE_NAVDATA_PORT = 5554
ARDRONE_NAVDATA_SIZE = 65535

# TODO : remove from here  for separate implementation
ARDRONE_COMMAND_PORT = 5556

class NavdataWorker():
    def __init__(self):
        self.gotNavdataMessage = Event()
        self.sendCommand = Event()
        self.gettingMessagesThread = threading.Thread(target=self.__receiveNavMessages)
        self.sendIsAliveThread = threading.Thread(target=self.__sendIsAlive)

        # Creating a udp socket
        self.nav_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def startGettingNavData(self):
        self.sendIsAliveThread.start()
        self.gettingMessagesThread.start()

    def stopGettingNavData(self):
        pass

    def __sendIsAlive(self):
        # Infinite loop for sending is alive
        while 1:
            self.nav_socket.sendto("\x01\x00\x00\x00", ('192.168.1.1', ARDRONE_NAVDATA_PORT))
            # Sleep for 2000 ms and then send an is alive message
            #time.sleep(2000.0/1000000.0)
            time.sleep(5000.0/1000000.0)

    def __receiveNavMessages(self):
        self.nav_socket.sendto("\x01\x00\x00\x00", ('192.168.1.1', ARDRONE_NAVDATA_PORT))
        configure = ControlMessage()
        configure.CommandConfig("general:navdata_demo", "TRUE")
        self.sendCommand(configure)

        print 'start get nav messages'

        while 1:
            try:
                is_good_data = True
                data = self.nav_socket.recv(ARDRONE_NAVDATA_SIZE)
            except IOError as e:
            # we consumed every packet from the socket and
            # continue with the last one
                time.sleep(1)
                is_good_data = False
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
            if is_good_data:
                navdata = NavdataMessage()
                navdata.decode(data)
                self.gotNavdataMessage(navdata)