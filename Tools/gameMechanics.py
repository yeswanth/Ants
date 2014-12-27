from Config import general_settings as config
from Tools import Utilities
from sets import Set
import random
import json

class LayoutUtilities :
    def __init__(self, path) :
	map_contents = json.loads(open(path).read(), object_hook=Utilities.ant_map_tuple_conversion_hook)
	self.height = map_contents['height']
	self.width = map_contents['width']
	self.hills = map_contents['hills']
	self.walls = map_contents['walls']
	self.freeCells = []
	for i in range(self.height) :
	    for j in range(self.width) :
		if (i, j) not in self.hills and (i, j) not in self.walls :
		    self.freeCells.append((i, j))
	self.ants = {}
	for player in config.PLAYERS :
	    self.ants.update({player:[]})

    def getRandomFreeCell(self) :
	try :
	    return random.choice(self.freeCells)
	except IndexError :
	    return None
