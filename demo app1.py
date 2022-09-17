#!/usr/bin/env python
import time
import argparse
from flyt_python import api

drone = api.navigation(timeout=120000) # instance of flyt droneigation class

#at least 3sec sleep time for the drone interface to initialize properly
time.sleep(3)

## parsing command line arguments
parser = argparse.ArgumentParser(description='Process a float value.')
parser.add_argument('side', metavar='side_length', type=float, help='side length of the square')
args = parser.parse_args()

## lets fly
side_length = args.side

print 'taking off'
drone.take_off(5.0)

print ' going along the setpoints'
drone.position_set(6.5,0,5,relative=True)
drone.position_set(6.5,6.5,5,relative=True)
drone.position_set(0,6.5,5,relative=True)
drone.position_set(0,0,5,relative=True)

print 'Landing'
drone.land(async=False)

#shutdown the instance
drone.disconnect()