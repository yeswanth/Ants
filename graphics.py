from Config import general_settings as config
import json

class Graphics(object):
    def __init__(self,map_name):
        self._extract_contents(map_name)

    def _extract_contents(self, map_name):
        map_contents = json.loads(open(config.MAP_PATH + map_name + '.json').read())
        self.height = map_contents['height'] 
        self.width = map_contents['width'] 
        self.hills = map_contents['hills']
        self.walls = map_contents['walls']

    def print_grid(self):
        for i in range(self.height):
            print '\n'
            for j in range(self.width):
                if [i,j] in self.hills:
                    print 'o',
                elif [i,j] in self.walls:
                    print '|',
                else:
                    print '-',
        print '\n'


if __name__ == '__main__':
    g = Graphics('map_101')
    g.print_grid()
    
    
