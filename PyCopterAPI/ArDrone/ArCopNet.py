
# Our includes
from PyCopterAPI.ICopter.ICopNet import ICopNet
from PyCopterAPI.ArDrone.ArWorkers.NavdataWorker import NavdataWorker

class ArCopNet(ICopNet):
    def __init__(self):
        super(ArCopNet, self).__init__()
        self.navData = NavdataWorker()

    def connect(self):
        # TODO : some sort of ping to know if drone is good and if not return False
        self.navData.startGettingNavData()
        return True

    def disconnect(self):
        self.navData.stopGettingNavData()