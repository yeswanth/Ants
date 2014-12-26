from threading import Thread
import imp

class Player(Thread) :
    def __init__(self, startX, startY, player) :
	self.player = getattr(imp.load_source(player, "./Players/" + player + ".py"), "Supervisor")(startX, startY)
