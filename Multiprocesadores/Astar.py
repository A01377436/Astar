#Este no sirve, grax

import operator
import time

class Node():
    """A node class for A* Pathfinding"""

    # Object Initializer
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    # Compares Object to Other Object and return True or False (Python drawback)
    def __eq__(self, other):
        return self.position == other.position

def astar(maze,node,end,path,prev):

    # Create start and end node
    current_node = node
    print(current_node.position)
    end_node = end

    adjacent_nodes=[]

    # You reached target position, or your target position is the same as source
    if (current_node.position == end_node.position):
        return True,path

    adjacent_nodes.append(Node(current_node,(current_node.position[0]+1,current_node.position[1]))) #Up
    adjacent_nodes.append(Node(current_node,(current_node.position[0]-1,current_node.position[1]))) #Down
    adjacent_nodes.append(Node(current_node,(current_node.position[0],current_node.position[1]-1))) #Left
    adjacent_nodes.append(Node(current_node,(current_node.position[0],current_node.position[1]+1))) #Right

    temp = []

    #Validate nodes
    for object in adjacent_nodes:
        if( (object.position[0]>=0 and object.position[1]>=0) and (object.position[0]<len(maze) and object.position[1]<len(maze[0])) and (maze[object.position[0]][object.position[1]] != 1)):
            if(object.position != prev):
                temp.append(object)

    adjacent_nodes=temp

    #Calculate cost
    for object in adjacent_nodes:
        object.g=current_node.g+1
        object.h=((object.position[0]-end.position[0])**2)+((object.position[1]-end.position[1])**2) #Pythagoras theorem to calculate heuristic
        object.f=object.g+object.h #Calculate final value for each node

    adjacent_nodes.sort(key=operator.attrgetter('f'))

    #Determine 
    for object in adjacent_nodes:
        result,path=astar(maze,object,end,path,current_node.position)
        if (result == True):
            #print(object.position)
            path.append(object.position) #Shortest position list
            return True,path
    return False,path

def main():
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
            [0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 1, 0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start_node=Node(None,(0,0))
    end_node=Node(None,(7,6))

    path=[]


    start = time.time()
    _,path=astar(maze,start_node,end_node,path,(-1,-1))
    end = time.time()
    print(start-end)
    path.append(start_node.position)

    path=path[::-1]

    for line in maze:
        print(line)

    for coord in path:
        maze[coord[0]][coord[1]]=2
    maze[end_node.position[0]][end_node.position[1]]=3
    print("-------------")
    for line in maze:
        print(line)
    print(path)

if __name__ == '__main__':
    main()