###
### This is API testing Area all written here is temporary
###

# Global imports
import sys

# Our imports
from PyCopterAPI.CopFactory import CopFactory

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

print 'All good'







