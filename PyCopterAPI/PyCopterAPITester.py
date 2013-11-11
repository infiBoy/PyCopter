###
### This is API testing Area all written here is temporary
###

# Global imports
import sys

# Our imports
from PyCopterAPI.CopFactory import CopFactory

# Global test functions

# Logging accelerometer data
def log_accel_data(accelData):
    print "Accelerometer X:%f, Y:%f, Z:%f" % (accelData.VectorX, accelData.VectorY, accelData.VectorZ)

# Logging gyroscope data
def log_gyro_data(gyroData):
    print "Gyroscope theta:%f, phi:%f, psi:%f" % (gyroData.ThetaAngle, gyroData.PhiAngle, gyroData.PsiAngle)

##
##-------------------------- ArDrone Testing section-----------------------------------------
##
# Creating ArDrone class
ardrone = CopFactory.factory("ArDrone")

# Test if ArDrone class created good
if (ardrone == None):
    print 'Problem in initialization of ArDrone'
    sys.exit()

# Test if ArDrone connected good
if (ardrone.network.connect() == False):
    print 'Problem in connection to ArDrone'
    sys.exit()

# Test if ArDrone accelerometer sensor class is created
if (ardrone.sensors.getAccelSensor() == None):
    print 'Problem in accelerometer creation of ArDrone'
    sys.exit()

# Register to event to get accelerometer data
ardrone.sensors.getAccelSensor().gotAccelEvent += log_accel_data

# Test start of accelerometer
if (ardrone.sensors.getAccelSensor().start() == False):
    print 'Problem in accelerometer starting of ArDrone'
    sys.exit()

# Test if ArDrone gyroscope sensor class is created
if (ardrone.sensors.getGyroSensor() == None):
    print 'Problem in gyroscope creation of ArDrone'
    sys.exit()

# Register to event to get gyroscope data
ardrone.sensors.getGyroSensor().gotGyroEvent += log_gyro_data

# Test start of gyroscope
if (ardrone.sensors.getGyroSensor().start() == False):
    print 'Problem in gyroscope starting of ArDrone'
    sys.exit()

print 'All good'







