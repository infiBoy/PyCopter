# FileName : GyroData.py
# Date : 09.11.2013
# Developers : Maxim Arav

class GyroData():
    def __init__(self, theta, phi, psi):
        self.theta = theta
        self.phi = phi
        self.psi = psi

    @property
    def ThetaAngle(self):
        return self.theta

    @ThetaAngle.setter
    def ThetaAngle(self, value):
        self.theta = value

    @property
    def PhiAngle(self):
        return  self.phi

    @PhiAngle.setter
    def PhiAngle(self, value):
        self.phi = value

    @property
    def PsiAngle(self):
        return self.psi

    @PsiAngle.setter
    def PsiAngle(self, value):
        self.psi = value

