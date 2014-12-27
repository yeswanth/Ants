from Config import general_settings as config
from threading import Thread
from mmap import mmap
import imp

class Player(Thread) :
    def __init__(self, startX, startY, player) :
	self.fd = open(config.STASH_PATH + player + "stash.txt", "r+")
	self.playerStash = mmap.mmap(self.fd.fileno(), 0)
	self.player = getattr(imp.load_source(player, config.PLAYER_PATH + player + ".py"), "Supervisor")(startX, startY, self.playerStash)
	self.fd.close()
