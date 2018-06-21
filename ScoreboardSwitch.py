from MCP23017 import MCP23017
from time import sleep     # this lets us have a time delay (see line 12)

class ScoreboardSwitch(object):
    name = None
    chipAddress = None
    switchPin = None
    mcp = None
    def __init__(self, name,chipAddress,switchPin):
        self.chipAddress = chipAddress
        self.name = name
        self.switchPin = switchPin
        self.mcp = MCP23017(address = chipAddress, num_gpios = 16) # MCP23017
        self.mcp.pinMode(switchPin,self.mcp.INPUT)
    def getState(self):
        #print "Switch : "  + self.name + " testing sate : " + str(self.mcp.input(self.switchPin))
        if self.mcp.input(self.switchPin) == 1:
            return 1
        else:
            return 0

