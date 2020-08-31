from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



## START ######## MY CODE

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.adjacency_list = {}

    
    def select_random_exit(self, exits):

        index = random.randint(0, len(exits)-1)
        
        direction = list(exits)[index]
        
        if exits.get(direction) == '?':

            return direction

        else:

            self.select_random_exit(exits)


    def dft(self, player, starting_room):
        
        
        # Create an empty stach and add the starting_room
        stack = Stack()
        stack.push({
            'current_room': 0,
            'exits': {'n': '?', 's': '?', 'w': '?', 'e': '?'},
            'last_direction': None
        })

        # while the stack is not empty:
        while stack.size() > 0:
            # get current vertex PATH (pop from stack)
            current_obj = stack.pop()
            current_room = current_obj['current_room']
            current_exits = current_obj['exits']
            last_direction = current_obj['last_direction']

            # IF UNexplored path exists in current_exits:
            if current_room not in self.adjacency_list:

                self.adjacency_list[current_room] = current_exits

            else:
                
                exits = self.adjacency_list[current_room]

                print("in: ", exits)            
                # next_direction = next((room_id for room_id, exits in mydict.items() if age == search_age), None)
                
                # # Randomly select an unexplored exit recursively
                # # Returns 'string' (ie. 'n')
                # selected_exit = self.select_random_exit(current_exits)

                # # If exit has NOT been explored,
                # # travel through and get Room Info for Stack Load
                # if current_exits.get(selected_exit) == '?':

                #     # Travel through the exit
                #     player.travel(selected_exit)

                #     # Get the Next Room ID
                #     next_room_id = player.current_room.id

                #     # Get Next Room Exits List
                #     next_room_exits_list = player.current_room.get_exits()

                #     # Set empty dict to hold next_room_exits
                #     next_room_exits_dict = {}

                #     # Convert Next Room Exits List to Dictionary
                #     for direction in next_room_exits_list:
                #         next_room_exits_dict[direction] = '?'
                    
                #     # # Add Next Room to Stack
                #     # stack.push({
                #     #     'current_room': next_room_id,
                #     #     'exits': next_room_exits_dict,
                #     #     'last_direction': selected_exit   
                #     # })

                #     print(stack.size())
          

            # Line 93 - IF    
            # IF UNexplored path DOES NOT exist in current_exits:
            # Need to walk back and try another exit
            # else: 

            #     if last_direction == 'n':

            #         walk_back_direction = 's'

            #     elif last_direction == 's':

            #         walk_back_direction = 'n'
                
            #     elif last_direction == 'e':

            #         walk_back_direction = 'w'

            #     elif last_direction == 'w':

            #         walk_back_direction = 'e'

        
                # player.travel(walk_back_direction)

        print("looping")


## END ######## MY CODE


test_1 = Graph()

test_1.dft(player, 0)

# TRAVERSAL TEST - DO NOT MODIFY
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
