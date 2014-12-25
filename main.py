from Config import general_settings as config
from time import sleep
from graphics import Graphics

class Timer():
    def __init__(self):
        self.time = 0 

    def timer(self):
        print "Time: ", self.time
        print '==============\n'
        g = Graphics('map_101')
        g.print_grid()
        sleep(config.SLEEP_TIME)
        self.time += 1

    def runloop(self):
        looper = 0
        while looper < config.MAX_TURNS:
            self.timer()
            looper += 1
 

if __name__ == '__main__':      
    timer = Timer()
    timer.runloop()
