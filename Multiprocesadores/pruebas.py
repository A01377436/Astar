import operator

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

def astar(maze,node,end):

    # Create start and end node
    current_node = node
    print(current_node.position)
    end_node = end

    adjacent_nodes=[]

    if (current_node.position == end_node.position):
        return current_node.position

    adjacent_nodes.append(Node(current_node,(current_node.position[0]+1,current_node.position[1])))
    adjacent_nodes.append(Node(current_node,(current_node.position[0]-1,current_node.position[1])))
    adjacent_nodes.append(Node(current_node,(current_node.position[0],current_node.position[1]-1)))
    adjacent_nodes.append(Node(current_node,(current_node.position[0],current_node.position[1]+1)))

    temp = []

    for object in adjacent_nodes:
        if( (object.position[0]>=0 and object.position[1]>=0) and (object.position[0]<len(maze) and object.position[1]<len(maze[0])) and (maze[object.position[0]][object.position[1]] != 1)):
            temp.append(object)

    adjacent_nodes=temp

    for object in adjacent_nodes:
        object.g=current_node.g+1
        object.h=((object.position[0]-end.position[0])**2)+((object.position[1]-end.position[1])**2)
        object.f=object.g+object.h

    adjacent_nodes.sort(key=operator.attrgetter('f'))

    for object in adjacent_nodes:
        result=astar(maze,object,end)
        if (result == True):
            print(object.position)
            return True
        else:
            break

def main():
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start_node=Node(None,(0,0))
    end_node=Node(None,(7,6))

    astar(maze,start_node,end_node)

    for line in maze:
        print(line)


if __name__ == '__main__':
    main()


