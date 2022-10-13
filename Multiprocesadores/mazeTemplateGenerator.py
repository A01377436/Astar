import random

size=5
maze=[]

for i in range(0,size):
    temp=[]
    for j in range(0,size):
        temp.append(1)
    maze.append(temp)

for row in maze:
    print(str(row)+",")
