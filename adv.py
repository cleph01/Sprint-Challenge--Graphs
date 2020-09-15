from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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
        self.adjacency_list = {0:{'n': '?', 's': '?', 'w': '?', 'e': '?'}}

    
    def select_random_exit(self, exits):
    
        if '?' in exits.values():
        
            for k,v in exits.items():

                if v == '?':

                    return k

        else:

            return None



    def get_opposite_direction(self, direction):

        if direction == 'n':

            return 's'

        elif direction == 's':

            return 'n'
        
        elif direction == 'e':

            return 'w'

        elif direction == 'w':

            return 'e'

    def convert_exit_list_to_dict(self, list):

        exit_dict = {}
        
        for exit in list:

            exit_dict[exit] = '?'

        return exit_dict


    def dft(self, player, starting_room):
        
        current_room_obj = None
        
        # Create an empty stach and add the starting_room
        stack = Stack()
        
        stack.push({
            'current_room': player.current_room, 
            'direction': None
        })


        print("Initial Current Room ID: ", player.current_room.id)
        print("Adjacency List Before While: ", self.adjacency_list)
        print("Stack Size: ", stack.size())
        print("\n##### LOADED ROOM 0 #####\n")

        Current_Room_Match = True

        # while the stack is not empty:
        while stack.size() > 0 and Current_Room_Match:

            # current_room_obj = stack.pop()
            current_room_obj = stack.stack[-1]

            current_room = current_room_obj["current_room"]

            print("###TOP###\nCurrent Room form line 128: ", current_room.id)

            print("Stack Size Beginning of While: ", stack.size())

            
            # Check Current Room Object = Player.Current_Room.id 
            if player.current_room.id is not current_room.id:

                Current_Room_Match = False

                print("Player.Current_Room.id Not Matching With Current_Room_Obj")


            # Check if Curr_Room is in Adjacency List
            if current_room_obj['current_room'].id not in self.adjacency_list:

                self.adjacency_list[current_room_obj['current_room'].id] = self.convert_exit_list_to_dict(current_room_obj.get_exits())


            # Get all adjacent rooms of the popped room


            # Select Random Exit from Current Room Exit Dict
            selected_exit = self.select_random_exit(self.adjacency_list[current_room_obj['current_room'].id])

            print("Selected Exit: ", selected_exit)

            if selected_exit is not None:

                # Get next room
                next_room = player.current_room.get_room_in_direction(selected_exit)

                # Check if Next Room is in Adjacency List
                if next_room.id not in self.adjacency_list:
                    # Load next room exits to adjacency list
                    self.adjacency_list[next_room.id] = self.convert_exit_list_to_dict(next_room.get_exits())
                    print("Added Next Room to Adjacency List: ", self.adjacency_list[next_room.id])

                # Pair Current Room Exit with Next Room Entrance
                self.adjacency_list[current_room_obj['current_room'].id][selected_exit] = next_room.id
                print("Paired Current Exit with Next Entrance: ", self.adjacency_list[current_room_obj['current_room'].id])

                # Pair Next Room Entrance with Current Room Exit
                self.adjacency_list[next_room.id][self.get_opposite_direction(selected_exit)] = current_room_obj['current_room'].id
                print("Paired Next Entrance with Current Exit: ", self.adjacency_list[next_room.id])

                ## Add Next Room to Stack
                stack.push({
                    'current_room': next_room,
                    'direction': selected_exit
                })

                print("Pushed Next Room to Stack: ", next_room.id)

                ## Add Direction to Traversal Path
                traversal_path.append(selected_exit)

                ## Set New Current Room
                player.travel(selected_exit)

                print("Stack size after Push to Stack: ", stack.size())

            # if selected exit is None
            else:
                
                popped_room_obj = stack.pop()

                # Add WalkOut to Traversal Path
                traversal_path.append(self.get_opposite_direction(popped_room_obj["direction"]))

                player.travel(self.get_opposite_direction(popped_room_obj["direction"]))

                # push current room back on stack
                ## Add Next Room to Stack
                # stack.push({
                #     'current_room': current_room.get_room_in_direction(self.get_opposite_direction(popped_room_obj["direction"]),
                #     'direction': self.get_opposite_direction(popped_room_obj["direction"])
                # })

                print("Popped Direction: ", self.get_opposite_direction(popped_room_obj["direction"]))


        print("Final Traversal Path: ", traversal_path)


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
