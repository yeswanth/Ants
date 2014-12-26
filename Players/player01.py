class Supervisor :
    def __init__(self, startX, startY, fileStore) :
	self.homeX = startX
	self.homeY = startY
	self.fileStore = fileStore
	self.ants = []

class Ant :
    def __init__(self) :
	print "initializing ant"
