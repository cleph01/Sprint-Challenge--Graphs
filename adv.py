from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk

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
        
        counter = 0
        
        # Create an empty stach and add the starting_room
        stack = Stack()
        
        stack.push([player.current_room])


        print("Initial Current Room ID: ", player.current_room.id)
        print("Adjacency List Before While: ", self.adjacency_list)
        print("Stack Size: ", stack.size())
        print("\n##### LOADED ROOM 0 #####\n")

        # while the stack is not empty:
        while stack.size() > 0:

            counter += 1

            print("Counter: ", counter)

            current_path = stack.pop()

            current_room_obj = current_path[-1]

            current_room_id = current_room_obj.id
            

            print("\n###TOP###\n\nCurrent Room form line 121: ", current_room_id)

            print("Stack Size Beginning of While: ", stack.size())

            
            # if the vertex has not been visited
            if current_room_id not in self.adjacency_list:

                print("Current Room Not in Adj List: ", current_room_id)

                print("Adjacency List: ", self.adjacency_list)

                # Get current_room_exits
                current_room_exits_list = current_room_obj.get_exits()

                print("Current Room Exits List: ", current_room_exits_list)

                # Add the room_id and converted exits list-to-dictionary to the adjacency_list
                self.adjacency_list[current_room_id] = self.convert_exit_list_to_dict(current_room_exits_list)

                # Select random exit from New adjacency_list entry
                selected_exit = self.select_random_exit(self.adjacency_list[current_room_id])

                next_room = current_room_obj.get_room_in_direction(selected_exit)

                # Print Selected Exit
                print("Selected Exit: ", selected_exit)

                # Print Next Room
                print("Next Room: ", next_room)

                # Assign Next Room to Adjacency List for Current Room Id
                self.adjacency_list[current_room_id][selected_exit] = next_room.id

        # Add Next Room Exits to Adjacency List
                 
                # Get Next Room Exits List
                next_room_exits_list = next_room.get_exits()

                print("Next Room Exits List: ", next_room_exits_list)

                # Add the room_id and converted exits list-to-dictionary to the adjacency_list
                self.adjacency_list[next_room.id] = self.convert_exit_list_to_dict(next_room_exits_list)

                # Update next_room adjacency_list to point to current Room
                # for opposite direction
                self.adjacency_list[next_room.id][self.get_opposite_direction(selected_exit)] = current_room_id

                print("Adjacency List with Next Room: ", self.adjacency_list)

                # copy the current path
                new_path = list(current_path)
                
                # add the next_room to it
                new_path.append(next_room)
                
                # Push New Path to Stack
                stack.push(new_path)

                print("New Path: ", new_path)

                # Travel to Next Room
                player.travel(selected_exit)

                # Append direction to traversal_path array
                traversal_path.append(selected_exit)

                print("Loop Traversal Path: ", traversal_path)

            # Current Room is in adjacency list    
            else:

                print("Current Room IS in Adj List: ", current_room_id)

                print("Adjacency List: ", self.adjacency_list)

                # Select random exit from adjacency_list
                selected_exit = self.select_random_exit(self.adjacency_list[current_room_id])

                print("Selected Exit: ", selected_exit)

                # Check if available exit exists
                if selected_exit is not None:

                    available_exit = True

                else:

                    available_exit = False

                print("Available Exit: ", available_exit)

                # If Available_Exit is True --> Go
                if available_exit == True:
    
                    print("Current Room Obj: ", current_room_obj)
                    print("Selected Exit: ", selected_exit )

                    print("Current Room Exits List: ", current_room_obj.get_exits())

                    next_room = current_room_obj.get_room_in_direction(selected_exit)

                    print("Next Room: ", next_room)

                    next_room_exits_list = next_room.get_exits()

                    print("Next Room Exits List: ", next_room_exits_list)

                    # Assign Next Room to Adjacency List for Current Room Id
                    self.adjacency_list[current_room_id][selected_exit] = next_room.id

    # Add the room_id and converted exits list-to-dictionary to the adjacency_list
                    self.adjacency_list[next_room.id] = self.convert_exit_list_to_dict(next_room_exits_list)

                    # Update next_room adjacency_list to point to current Room
                    # for opposite direction
                    self.adjacency_list[next_room.id][self.get_opposite_direction(selected_exit)] = current_room_id

                    print("Adjacency List with Next Room: ", self.adjacency_list)


                    # copy the current path
                    new_path = list(current_path)
                    
                    # add the next_room to it
                    new_path.append(next_room)
                    
                    # Push New Path to Stack
                    stack.push(new_path)

                    print("New Path: ", new_path)

                    # Travel to Next Room
                    player.travel(selected_exit)

                    # Append direction to traversal_path array
                    traversal_path.append(selected_exit)

                    print("Loop Traversal Path: ", traversal_path)

                # Else: Otherwise, backtrack... which would be the path array @ index -2
                else:

                    # copy the current path
                    new_path = list(current_path)

                    # Get previous room
                    backtrack_room = new_path[-2]
                    
                    if backtrack_room is not None:

                        print("Backtrack Room: ", backtrack_room)

                        # add the previous room to path
                        new_path.append(backtrack_room)
                        
                        # # Push New Path to Stack
                        stack.push(new_path)

                        print("New Path: ", new_path)

                        # Travel to Next Room
                        player.travel(self.get_opposite_direction(selected_exit))

                        # Append direction to traversal_path array
                        traversal_path.append(selected_exit)

                        print("Loop Traversal Path: ", traversal_path)


        # End of While Loop                
        print("Final Traversal Path: ", traversal_path)


## END ######## MY CODE


test_1 = Graph()

test_1.dft(player, 0)


#TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



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
