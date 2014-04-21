from time import sleep
from graphics import Graphics

SLEEP_TIME = 0.5
MAX_LOOP_CYCLES = 10

class Timer():
    def __init__(self):
        self.time = 0 

    def timer(self):
        print "Time: ", self.time
        print '==============\n'
        g = Graphics('map_101')
        g.print_grid()
        sleep(SLEEP_TIME)
        self.time += 1

    def runloop(self):
        looper = 0
        while looper < MAX_LOOP_CYCLES:
            self.timer()
            looper += 1
 

if __name__ == '__main__':      
    timer = Timer()
    timer.runloop()
