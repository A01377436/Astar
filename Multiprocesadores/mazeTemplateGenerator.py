import random

size=7
maze=[]

for i in range(0,size):
    temp=[]
    for j in range(0,size):
        temp.append(0)
    maze.append(temp)

for row in maze:
    print(str(row)+",")
