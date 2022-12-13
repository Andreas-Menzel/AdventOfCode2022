import sys
sys.setrecursionlimit(3000)


class Location:
    def __init__(self, _row, _col, _height, _is_start, _is_goal):
        self.row = _row
        self.col = _col
        self.is_start = _is_start
        self.is_goal = _is_goal
        # Convert height from char to int
        self.height = ord(_height)
        self.available_paths = []
    
    def connect_location(self, other_location):
        self.available_paths.append(other_location)



def get_location_map():
    # Read heightmap file
    heightmap = []
    with open('input.txt') as heightmap_file:
        heightmap = [ row.rstrip() for row in heightmap_file.readlines() ]
    
    # Create locations and add to location_map
    location_map = []
    for row in range(len(heightmap)):
        location_map.append([])
        for col in range(len(heightmap[row])):
            height = heightmap[row][col]
            is_start = False
            is_goal = False
            if height == 'S':
                is_start = True
                height = 'a'
            elif height == 'E':
                is_goal = True
                height = 'z'
            
            new_location = Location(row, col, height, is_start, is_goal)
            location_map[-1].append(new_location)
    
    # Connect locations
    for row in range(len(location_map)):
        for col in range(len(location_map[row])):
            # Connect left (maybe)
            if col > 0 and \
                    abs(location_map[row][col].height - location_map[row][col-1].height) <= 1:
                location_map[row][col].connect_location(location_map[row][col-1])
            # Connect right (maybe)
            if col < len(location_map[row]) - 1 and \
                    abs(location_map[row][col].height - location_map[row][col+1].height) <= 1:
                location_map[row][col].connect_location(location_map[row][col+1])
            # Connect up (maybe)
            if row > 0 and \
                    abs(location_map[row][col].height - location_map[row-1][col].height) <= 1:
                location_map[row][col].connect_location(location_map[row-1][col])
            # Connect down (maybe)
            if row < len(location_map) - 1 and \
                    abs(location_map[row][col].height - location_map[row+1][col].height) <= 1:
                location_map[row][col].connect_location(location_map[row+1][col])

    return location_map


def get_shortest_path(_location_map):
    return _get_shortest_path(0, _location_map, _location_map[0][0], [])

def _get_shortest_path(_path_length, _location_map, _current_location, _visited):
    if _current_location.is_goal:
        return _path_length

    next_locations = [ location for location
                        in _current_location.available_paths
                        if location not in _visited ]
    
    path_lengths = []
    for next_loc in next_locations:
        length = _get_shortest_path(_path_length + 1, _location_map, next_loc, _visited + [_current_location])
        if not length == None:
            path_lengths.append(length)
            #print(f'Path length of {next_loc.row},{next_loc.col} is {length}.')
    
    if not path_lengths == []:
        return min(path_lengths)
    else:
        return None


location_map = get_location_map()

print(f'Part one: The shortest path to the goal has {get_shortest_path(location_map)} steps')

#for location in location_map[1][2].available_paths:
#    print(f'{location.row},{location.col}')