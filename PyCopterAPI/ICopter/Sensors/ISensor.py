# FileName : ISensor.py
# Date : 09.11.2013
# Developers : Maxim Arav

class ISensor:
    def __init__(self):
        self.senHolder = None
        pass

    def setSensorsHolder(self, sensors):
        self.senHolder = sensors