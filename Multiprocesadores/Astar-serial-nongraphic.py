# A* Algorithm Code in Python
# Tested, Optimized and Commented
# A* implementation details:
#       Our implementation will evaluate adjacent nodes always in this order: North, South, West, East
#       It will always choose the node with the smallest F value to evaluate adjacents
#       If various nodes with the same F value are found, H is chosen as the tiebreaker

#       Using this tiebraker law we can try and fin the optimal path a tiny bit faster
#       Hopefully resulting in a better run time and less opened nodes

import copy #Used for a deepcopy of variables
import time #Used for delay only for graphical purposes
import math #Used for square root
from storeMaze import returnMaze #Support file with different mazes and coordinates

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


def partition(array,low,high):
    #Used in the quick sort recursive algorithm
    pivot = array[high] #Pivot is chosen as the right most value

    i = low - 1

    #Parallel
    for j in range(low, high): #Iterates through array
        if array[j].f <= pivot.f: #If an element with a smaller value of f is found it will move it to the beginning of the array
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array,low,high):
    #Recursive quicksort algorithm with pivot in the right most value
    if low < high:#Repeats until both indicators intersect or cross to the other side

        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


def astar(maze,start,end,screen,delay):
    #Main A* Algorithm

    opened=[]
    closed=[]
    #Open first node
    opened.append(start)

    while (len(opened)>0):#Iterate while there are open nodes or the end node is found

        quickSort(opened,0,len(opened)-1) #Using non library based sorting algorithm

        #Until line 134, used as a tiebraker, choosing the smalles H value if there are ties in F values
        selectedNode=0
        hValue=opened[0].h
        fValue=opened[0].f
        
        
        #Parallel
        for i in range(1,len(opened)):
            if opened[i].f == fValue:
                if opened[i].h < hValue:
                    hValue=opened[i].h
                    selectedNode=i
            else:
                break

        #After a node has been selected as the next to be opened
        currentNode=opened[selectedNode]
        currentIndex=selectedNode

        #print(currentNode.f)

        #We mark the node as closed and proceed to inspect its neightboars
        opened.pop(currentIndex)
        closed.append(currentNode)

        #If our current node is the end node, we iterate back through node parents, append them to path and return 3 lists:
        #   The optimal path found, the closed nodes, any pending opened nodes and False for errors
        if (currentNode.position==end.position):
            path=[]
            current=currentNode
            while (current is not None):
                path.append(current.position)
                current=current.parent
            return path,closed,opened,False

        children=[]
        #We now take a look at neighbouring nodes, in the order defined at the top of this file
        for new_position in [(-1,0),(1,0),(0,-1),(0,1)]:
            #Declearing a new node with the postion given by the current node and the for loop above
            node_position=((currentNode.position[0]+new_position[0]),(currentNode.position[1]+new_position[1]))
            #Conditionals to ensure new node is inside maze and its a non-wall cell
            if not(node_position[0] < len(maze)):
                #print("Out of range")
                continue
            if not(node_position[1]<len(maze[0])):
                #print("Out of range")
                continue
            if (node_position[0] < 0):
                #print("Negative Value")
                continue
            if (node_position[1] < 0):
                #print("Negative Value")
                continue
            if (maze[node_position[0]][node_position[1]] != 0):
                continue
            #After validated, a new node is created and appended to childrens list, this are the children of the parent current node
            new_node = Node(currentNode,node_position)
            children.append(new_node)


        for child in children:
            #We iterate through the child nodes and check two main things:
            #If child position is equal to a closed node, we skip it as it has already been through
            #If child position is equal to an oppened node, we check how efficiently we arrived there
            #   If we findout we arrived with a better path, we replace opened node with child
            #If both of the conditionals return False, we append the child to the oppened nodes
            notInOpened,notInClosed=True,True

            for closed_child in closed:
                if child.position == closed_child.position:
                    notInClosed=False

            #Creating child node
            child.g = currentNode.g+1
            child.h = math.sqrt(((child.position[0] - end.position[0]) ** 2) + ((child.position[1] - end.position[1]) ** 2))
            child.f = child.g + child.h

            #Checking if opened
            for opened_node in opened:
                if child==opened_node:
                    notInOpened=False

            if (notInOpened and notInClosed):
                opened.append(child)
                continue

            #If children is equal to an existing one but with lower G, we replace it
            if notInClosed == True:
                for i in range(0,len(opened)):
                    if child==opened[i]:
                        if child.g < opened[i].g:
                            opened[i]=child
                            continue
                        elif child.f < opened[i].f:
                            opened[i]=child
                            continue

    path=[]
    return path,closed,opened,False



def main():
    mazeName=int(input("Maze: "))
    print("ok")
    maze,coords = returnMaze(mazeName)

    start_node=Node(None,coords[0])
    end_node=Node(None,coords[1])

    path,closed,opened,error=astar(maze,start_node,end_node,None,0)

    if error:
        print("Error: Program Closed")
        return

    """Debugging Prints"""

    print(path)

    #print("-----------")
    #for closedNode in closed:
    #    print("x:"+str(closedNode.position[1])+" y:"+str(closedNode.position[0])+" g:"+str(closedNode.g)+" h:"+str(closedNode.h)+" f:"+str(closedNode.f))
    #print("-----------")

    #for line in maze:
        #print(line)
    for node in closed:
        maze[node.position[0]][node.position[1]]=5
    for node in opened:
        maze[node.position[0]][node.position[1]]=6
    for coord in path:
        maze[coord[0]][coord[1]]=2
    maze[end_node.position[0]][end_node.position[1]]=3
    maze[start_node.position[0]][start_node.position[1]]=4
    #print("-------------")
    #for line in maze:
    #print(line)
    #print(len(path))

    print("end")


if __name__ == '__main__':
    main()