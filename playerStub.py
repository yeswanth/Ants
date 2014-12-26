from threading import Thread
import imp
import mmap

class Player(Thread) :
    def __init__(self, startX, startY, player) :
	self.fd = open("./PlayerStash/" + player + "stash.txt", "r+")
	self.playerStash = mmap.mmap(self.fd.fileno(), 0)
	self.player = getattr(imp.load_source(player, "./Players/" + player + ".py"), "Supervisor")(startX, startY, self.playerStash)
	self.fd.close()
