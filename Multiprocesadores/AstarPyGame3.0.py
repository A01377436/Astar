import copy
import operator
import pygame

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

def astar(maze,start,end):

    mazedraw = copy.deepcopy(maze)

    opened=[]
    closed=[]

    opened.append(start)

    res = 600
    pygame.init()
    screen = pygame.display.set_mode([res, res])
    screen.fill((255, 255, 255))

    a=0

    while (len(opened)>0):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for i in range(0,1000000):
            a=0

        for node in closed:
            mazedraw[node.position[0]][node.position[1]] = 5
        for node in opened:
            mazedraw[node.position[0]][node.position[1]] = 6
        screen.fill((255, 255, 255))

        x = 0
        y = 0
        w = res / len(mazedraw)
        color = (0, 0, 0)
        for row in mazedraw:
            for col in row:
                if (col == 0):
                    color = (255, 255, 255)
                elif (col == 1):
                    color = (0, 0, 0)
                elif (col == 2):
                    color = (10, 150, 10)
                elif (col == 3):
                    color = (255, 10, 10)
                elif (col == 4):
                    color = (255, 255, 0)
                elif (col == 5):
                    color = (180, 180, 180)
                elif (col == 6):
                    color=(0,255,255)
                box = pygame.Rect(x, y, w, w)
                pygame.draw.rect(screen, (0, 0, 0), box, 2)
                pygame.draw.rect(screen, color, box)
                x = x + w
            y = y + w
            x = 0

        pygame.display.flip()


##########################################################################3
        opened.sort(key=operator.attrgetter('g'))

        currentNode=opened[0]
        currentIndex=0

        #print(currentNode.position)


        opened.pop(currentIndex)
        closed.append(currentNode)

        if (currentNode.position==end.position):
            path=[]
            current=currentNode
            while (current is not None):
                path.append(current.position)
                current=current.parent
            return path,closed,opened

        children=[]

        for new_position in [(-1,0),(1,0),(0,-1),(0,1)]:
            node_position=((currentNode.position[0]+new_position[0]),(currentNode.position[1]+new_position[1]))

            if not(node_position[0] < len(maze)):
                print("Out of range")
                continue
            if (node_position[0] < 0):
                print("Negative Value")
                continue
            if not(node_position[1]<len(maze[0])):
                print("Out of range")
                continue
            if (node_position[1] < 0):
                print("Negative Value")
                continue
            if (maze[node_position[0]][node_position[1]] != 0):
                continue

            new_node = Node(currentNode,node_position)
            children.append(new_node)


        for child in children:
            coinc=0
            clsed=False
            for closed_child in closed:
                if child.position == closed_child.position:
                    clsed=True

            child.g = currentNode.g + 1
            child.h = ((child.position[0] - end.position[0]) ** 2) + ((child.position[1] - end.position[1]) ** 2)
            child.f = child.g + child.h

            for opened_node in opened:
                if child==opened_node:
                    coinc+=1

            for i in range(0,len(opened)):
                if clsed == False:
                    if child==opened[i]:
                        if child.g < opened[i].g:
                            opened[i]=child
                            continue
                        elif child.f < opened[i].f:
                            opened[i]=child
                            continue

            """for opened_node in opened:
                if clsed == False:
                    if child==opened_node:
                        if child.g < opened_node.g:
                            index=opened.index(opened_node)
                            opened[index]=child
                            continue
                        elif child.f < opened_node.f:
                            index = opened.index(opened_node)
                            opened[index] = child
                            continue
                        continue"""

            if coinc == 0 and clsed == False:
                opened.append(child)



    path=[]
    return path,closed,opened





def main():
    maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

    start_node=Node(None,(3,5))
    end_node=Node(None,(16,18))

    path,closed,opened=astar(maze,start_node,end_node)

    print(path)

    #print("-----------")
    #for closedNode in closed:
    #    print("x:"+str(closedNode.position[1])+" y:"+str(closedNode.position[0])+" g:"+str(closedNode.g)+" h:"+str(closedNode.h)+" f:"+str(closedNode.f))
    #print("-----------")

    for line in maze:
        print(line)
    for node in closed:
        maze[node.position[0]][node.position[1]]=5
    for node in opened:
        maze[node.position[0]][node.position[1]]=5
    for coord in path:
        maze[coord[0]][coord[1]]=2
    maze[end_node.position[0]][end_node.position[1]]=3
    maze[start_node.position[0]][start_node.position[1]]=4
    print("-------------")
    for line in maze:
        print(line)

    res=600
    pygame.init()
    screen = pygame.display.set_mode([res, res])

    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        x = 0
        y = 0
        w = res / len(maze)
        color = (0, 0, 0)
        for row in maze:
            for col in row:
                if (col == 0):
                    color = (255, 255, 255)
                elif (col == 1):
                    color = (0, 0, 0)
                elif (col == 2):
                    color = (10, 255, 10)
                elif (col == 3):
                    color = (255, 10, 10)
                elif (col == 4):
                    color = (255, 255, 0)
                elif (col == 5):
                    color = (180,180,180)
                box = pygame.Rect(x, y, w, w)
                pygame.draw.rect(screen, (0, 0, 0), box, 2)
                pygame.draw.rect(screen, color, box)
                x = x + w
            y = y + w
            x = 0

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()