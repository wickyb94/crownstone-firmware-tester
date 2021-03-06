import RPi.GPIO as GPIO
import time
import math

''''Initializing the pins of the multiplexers these pins are S0,S1,S2,S3,EN of the multiplexers''''
mp1 = [6, 13, 19, 26, 21]
mp2 = [4, 17, 27, 22, 18]
GPIO.setmode (GPIO.BCM)

for setting in range (0, 5):
    GPIO.setup (mp1[setting], GPIO.OUT)
for setting in range (0, 5):
    GPIO.setup (mp2[setting], GPIO.OUT)

#with these variables you can decide how many different multiplexers and how many chanels these multiplexers have   
numOffChannels = 16
numOffMultiplexers = 2

''''The mclass allows make a multiplexer to switch between the different channels''''\
class Multiplexer:
  #List of the 16 channels 
  muxChannel = [
                 [0, 0, 0, 0],
                 [1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [1, 1, 0, 0],
                 [0, 0, 1, 0],
                 [1, 0, 1, 0],
                 [0, 1, 1, 0],
                 [1, 1, 1, 0],
                 [0, 0, 0, 1],
                 [1, 0, 0, 1],
                 [0, 1, 0, 1],
                 [1, 1, 0, 1],
                 [0, 0, 1, 1],
                 [1, 0, 1, 1],
                 [0, 1, 1, 1],
                 [1, 1, 1, 1],
                ]

  def __init__ (self, S0, S1, S2, S3, EN):
     self.S0 = S0
     self.S1 = S1
     self.S2 = S2
     self.S3 = S3
     self.EN = EN

  ''''function where you can decide wich channel is connected. It ranges from 0 to 15''''
  def switch (self, channel):
     channel = channel-1
     if 0 =< channel =< 15:
         controlPin = [self.S0, self.S1, self.S2, self.S3]
         #turning off the S0-S3 pins with the EN pin while the S0-S3 pins selects a channel 
         #else another channel can be selected for a second
         GPIO.output (self.EN, 1)
         for i in range (0, 4):
             GPIO.output (controlPin[i], muxChannel[channel][i])
         GPIO.output(self.EN, 0)
     else:
         raise Exception ('Channel number out of bounds, channel must be an integer from 0 to 15')

  ''''function to test all if all the channels of this multiplexer are still working''''
  def testMultiplexerOutputs (self):
    for channel in range (0, numOffChannels):
         self.switch (channel)
         #sleep is needed here because only 1 channel can be choosen on the same time
         time.sleep (0.1)
  
  
  ''''gets the max number of channels available''''
  def getmaxNumChannels():
    return numOffChannels 
