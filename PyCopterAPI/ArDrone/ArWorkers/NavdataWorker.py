# FileName : NavdataWorker.py
# Date : 09.11.2013
# Developers : Maxim Arav

# Python imports
import thread, socket, time, struct

# Our imports
from PyCopterAPI.ICopter import Event
from PyCopterAPI.ArDrone.ArMessages.NavdataMessage import NavdataMessage

# Define consts
ARDRONE_NAVDATA_PORT = 5554
ARDRONE_NAVDATA_PORT_RECEIVE = 65535

# TODO : remove from here  for separate implementation
ARDRONE_COMMAND_PORT = 5556

class NavdataWorker():
    def __init__(self):
        self.gotNavdataMessage = Event()

    def startGettingNavData(self):
        self.__startGettingData()
        self.__startSendIsAlive()

    def stopGettingNavData(self):
        pass

    def __startSendIsAlive(self):
        thread.start_new_thread(self.__sendIsAlive())

    def __startGettingData(self):
        thread.start_new_thread(self.__receiveNavMessages())

    def __sendIsAlive(self):
        # Creating a udp socket
        nav_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Infinite loop for sending is alive
        while 1:
            # Sleep for 2000 ms and then send an is alive message
            time.sleep(2000.0/1000000.0)
            nav_socket.sendto("\x01\x00\x00\x00", ('192.168.1.1', ARDRONE_NAVDATA_PORT))


    # TODO : remove from here  for separate implementation
    def f2i(self, f):
        """Interpret IEEE-754 floating-point value as signed integer.

        Arguments:
        f -- floating point value
        """
        return struct.unpack('i', struct.pack('f', f))[0]

    # TODO : remove from here  for separate implementation
    def at_config(self, seq, option, value):
        """Set configuration parameters of the drone."""
        self.at("CONFIG", seq, [str(option), str(value)])

    # TODO : remove from here  for separate implementation
    def at(self,command, seq, params):
        """
        Parameters:
        command -- the command
        seq -- the sequence number
        params -- a list of elements which can be either int, float or string
        """
        param_str = ''
        for p in params:
            if type(p) == int:
                param_str += ",%d" % p
            elif type(p) == float:
                param_str += ",%d" % self.f2i(p)
            elif type(p) == str:
                param_str += ',"'+p+'"'
        msg = "AT*%s=%i%s\r" % (command, seq, param_str)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto("\x01\x00\x00\x00", ("192.168.1.1", ARDRONE_COMMAND_PORT))
        sock.sendto(msg, ("192.168.1.1", ARDRONE_COMMAND_PORT))

    def __receiveNavMessages(self):
        # TODO : Implement separate from that code
        self.at_config(1, "general:navdata_demo", "TRUE")

        # Creating a udp socket
        nav_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        while 1:
            try:
                data = nav_socket.recv(ARDRONE_NAVDATA_PORT_RECEIVE)
            except IOError:
            # we consumed every packet from the socket and
            # continue with the last one
                    break
            navdata = NavdataMessage()
            navdata.decode(data)
            self.gotNavdataMessage(navdata)