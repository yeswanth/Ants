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
	self.freeCells = Set()
	for i in range(self.height) :
	    for j in range(self.width) :
		if (i, j) not in self.hills and (i, j) not in self.walls :
		    self.freeCells.add((i, j))
	self.ants = {}
	for player in config.PLAYERS :
	    self.ants.update({player:[]})

    def getRandomFreeCell(self) :
	return random.sample(self.freeCells, 1)[0]

def tuple_hook(obj) :
    modified_obj = {}
    for key in obj :
	if key in ["hills", "walls"] :
	    val = [tuple(l) for l in obj[key]]
	    modified_obj[key] = val
	else :
	    modified_obj[key] = obj[key]
    return modified_obj
