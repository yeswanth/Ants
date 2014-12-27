from Config import general_settings as config
from Tools import gameMechanics
from time import sleep
from graphics import Graphics
from playerStub import Player
import os
import sys

#Timer should be decoupled from loop and graphics (possibly delete class)
class Timer():
    def __init__(self):
        self.time = 0 

    def timer(self):
        print "Time: ", self.time
        print '==============\n'
        g = Graphics(config.MAP_PATH + config.MAP + '.json')
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
    map_path = config.MAP_PATH + config.MAP + '.json'
    game = gameMechanics.LayoutUtilities(map_path)
    print game.getRandomFreeCell()
    #timer = Timer()
    #timer.runloop()
