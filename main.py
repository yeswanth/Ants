from Config import general_settings as config
from Tools import gameMechanics
from time import sleep
from graphics import Graphics
from playerStub import Player
import os
import sys

class Timer():
    def __init__(self):
        self.time = 0 

    def timer(self):
        print "Time: ", self.time
        print '==============\n'
        g = Graphics(config.MAP)
        g.print_grid()
        sleep(config.SLEEP_TIME)
        self.time += 1

    def runloop(self):
        looper = 0
	#player1 = Player(0, 0, "player01")
        while looper < config.MAX_TURNS:
            self.timer()
            looper += 1
 

if __name__ == '__main__':      
    sys.path.append(os.getcwd())
    game = gameMechanics.LayoutUtilities(config.MAP_PATH + config.MAP + '.json')
    print game.getRandomFreeCell()
    timer = Timer()
    timer.runloop()
