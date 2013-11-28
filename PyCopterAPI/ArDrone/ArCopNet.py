
# Our includes
from PyCopterAPI.ICopter.ICopNet import ICopNet
from PyCopterAPI.ArDrone.ArWorkers.NavdataWorker import NavdataWorker
from PyCopterAPI.ArDrone.ArWorkers.CommandWorker import CommandWorker

class ArCopNet(ICopNet):
    def __init__(self, copter):
        super(ArCopNet, self).__init__(copter)
        self.navData = NavdataWorker()
        self.commandWork = CommandWorker()
        self.copter.copterThreads.addThread(self.navData.gettingMessagesThread)
        self.copter.copterThreads.addThread(self.navData.sendIsAliveThread)
        self.navData.sendCommand += self.commandWork.SendCommand

    def connect(self):
        # TODO : some sort of ping to know if drone is good and if not return False
        self.commandWork.StartWorker()
        self.navData.startGettingNavData()
        return True

    def disconnect(self):
        self.navData.stopGettingNavData()