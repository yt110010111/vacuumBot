import csv
from tkinter import *
import time
import random

direction = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1),
             5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}
dirtPos = set()


class Robot:

    def __init__(self, start, list_map):
        self.np = start.copy()
        self.road = list_map

    def garbage_detection(self):
        if(self.np[0] == 0):
            if(self.np[1] == 0):
                if(self.road[self.np[0]][self.np[1]+1] == 2):
                    return 5
                elif(self.road[self.np[0]+1][self.np[1]+1] == 2):
                    return 6
                elif(self.road[self.np[0]+1][self.np[1]] == 2):
                    return 7
                else:
                    return 9
            elif(self.np[1] == 9):
                if(self.road[self.np[0]][self.np[1]-1] == 2):
                    return 1
                elif(self.road[self.np[0]+1][self.np[1]] == 2):
                    return 7
                elif(self.road[self.np[0]+1][self.np[1]-1] == 2):
                    return 8
                else:
                    return 9
            else:
                if(self.road[self.np[0]][self.np[1]-1] == 2):
                    return 1
                if(self.road[self.np[0]][self.np[1]+1] == 2):
                    return 5
                elif(self.road[self.np[0]+1][self.np[1]+1] == 2):
                    return 6
                elif(self.road[self.np[0]+1][self.np[1]] == 2):
                    return 7
                elif(self.road[self.np[0]+1][self.np[1]-1] == 2):
                    return 8
                else:
                    return 9
        elif(self.np[0] == 9):
            if(self.np[1] == 0):
                if(self.road[self.np[0]-1][self.np[1]] == 2):
                    return 3
                elif(self.road[self.np[0]-1][self.np[1]+1] == 2):
                    return 4
                elif(self.road[self.np[0]][self.np[1]+1] == 2):
                    return 5
                else:
                    return 9
            elif(self.np[1] == 9):
                if(self.road[self.np[0]][self.np[1]-1] == 2):
                    return 1
                elif(self.road[self.np[0]-1][self.np[1]-1] == 2):
                    return 2
                elif(self.road[self.np[0]-1][self.np[1]] == 2):
                    return 3
                else:
                    return 9
            else:
                if(self.road[self.np[0]][self.np[1]-1] == 2):
                    return 1
                elif(self.road[self.np[0]-1][self.np[1]-1] == 2):
                    return 2
                elif(self.road[self.np[0]-1][self.np[1]] == 2):
                    return 3
                elif(self.road[self.np[0]-1][self.np[1]+1] == 2):
                    return 4
                elif(self.road[self.np[0]][self.np[1]+1] == 2):
                    return 5
                else:
                    return 9
        elif(self.np[1] == 0):
            if(self.road[self.np[0]-1][self.np[1]] == 2):
                return 3
            elif(self.road[self.np[0]-1][self.np[1]+1] == 2):
                return 4
            elif(self.road[self.np[0]][self.np[1]+1] == 2):
                return 5
            elif(self.road[self.np[0]+1][self.np[1]+1] == 2):
                return 6
            elif(self.road[self.np[0]+1][self.np[1]] == 2):
                return 7
            else:
                return 9
        elif(self.np[1] == 9):
            if(self.road[self.np[0]][self.np[1]-1] == 2):
                return 1
            elif(self.road[self.np[0]-1][self.np[1]-1] == 2):
                return 2
            elif(self.road[self.np[0]-1][self.np[1]] == 2):
                return 3
            elif(self.road[self.np[0]+1][self.np[1]] == 2):
                return 7
            elif(self.road[self.np[0]+1][self.np[1]-1] == 2):
                return 8
            else:
                return 9
        else:
            if(self.road[self.np[0]][self.np[1]-1] == 2):
                return 1
            elif(self.road[self.np[0]-1][self.np[1]-1] == 2):
                return 2
            elif(self.road[self.np[0]-1][self.np[1]] == 2):
                return 3
            elif(self.road[self.np[0]-1][self.np[1]+1] == 2):
                return 4
            elif(self.road[self.np[0]][self.np[1]+1] == 2):
                return 5
            elif(self.road[self.np[0]+1][self.np[1]+1] == 2):
                return 6
            elif(self.road[self.np[0]+1][self.np[1]] == 2):
                return 7
            elif(self.road[self.np[0]+1][self.np[1]-1] == 2):
                return 8
            else:
                return 9

    def road_find(self):
        if(self.np[0] == 0):
            if(self.np[1] == 0):
                while self.np[0] != 9 and self.np[1] != 9:
                    gardet = self.garbage_detection()
                    if(gardet != 9):
                        temp = gardet
                    else:
                        temp = random.randint(5, 7)
                    self.forward(temp)
                    roadList.append(temp)
                return 0
            elif(self.np[1] == 9):
                while self.np[0] != 9 and self.np[1] != 0:
                    n = [1, 7, 8]
                    gardet = self.garbage_detection()
                    if(gardet != 9):
                        temp = gardet
                    else:
                        temp = n[random.randint(0, 2)]
                    self.forward(temp)
                    roadList.append(temp)
                return 0
            else:
                n = [1, 5, 6, 8]
                temp = n[random.randint(0, 3)]
                self.forward(temp)
                roadList.append(temp)
                if(temp == 1 or temp == 8):
                    n = [1, 7, 8]
                    while self.np[0] != 9 and self.np[1] != 0:
                        gardet = self.garbage_detection()
                        if(gardet != 9):
                            temp = gardet
                        else:
                            temp = n[random.randint(0, 2)]
                        self.forward(temp)
                        roadList.append(temp)
                    return 0
                elif(temp == 5 or temp == 6):
                    n = [5, 6, 7]
                    while self.np[0] != 9 and self.np[1] != 9:
                        gardet = self.garbage_detection()
                        if(gardet != 9):
                            temp = gardet
                        else:
                            temp = n[random.randint(0, 2)]
                        self.forward(temp)
                        roadList.append(temp)
                    return 0
        elif(self.np[0] == 9):
            if(self.np[1] == 0):
                while self.np[0] != 0 and self.np[1] != 9:
                    gardet = self.garbage_detection()
                    if(gardet != 9):
                        temp = gardet
                    else:
                        temp = random.randint(3, 5)
                    self.forward(temp)
                    roadList.append(temp)
                return 0
            elif(self.np[1] == 9):
                while self.np[0] != 0 and self.np[1] != 0:
                    gardet = self.garbage_detection()
                    if(gardet != 9):
                        temp = gardet
                    else:
                        temp = random.randint(1, 3)
                    self.forward(temp)
                    roadList.append(temp)
                return 0
            else:
                n = [1, 2, 4, 5]
                temp = n[random.randint(0, 3)]
                self.forward(temp)
                roadList.append(temp)
                if(temp == 1 or temp == 2):
                    while self.np[0] != 0 and self.np[1] != 0:
                        gardet = self.garbage_detection()
                        if(gardet != 9):
                            temp = gardet
                        else:
                            temp = random.randint(1, 3)
                        self.forward(temp)
                        roadList.append(temp)
                    return 0
                elif(temp == 4 or temp == 5):
                    while self.np[0] != 0 and self.np[1] != 9:
                        gardet = self.garbage_detection()
                        if(gardet != 9):
                            temp = gardet
                        else:
                            temp = random.randint(3, 5)
                        self.forward(temp)
                        roadList.append(temp)
                    return 0
        elif(self.np[1] == 0):
            n = [3, 4, 6, 7]
            temp = n[random.randint(0, 3)]
            self.forward(temp)
            roadList.append(temp)
            if(temp == 3 or temp == 4):
                while self.np[0] != 0 and self.np[1] != 9:
                    gardet = self.garbage_detection()
                    if(gardet != 9):
                        temp = gardet
                    else:
                        temp = random.randint(3, 5)
                    self.forward(temp)
                    roadList.append(temp)
                return 0
            elif(temp == 6 or temp == 7):
                while self.np[0] != 9 and self.np[1] != 9:
                    gardet = self.garbage_detection()
                    if(gardet != 9):
                        temp = gardet
                    else:
                        temp = random.randint(5, 7)
                    self.forward(temp)
                    roadList.append(temp)
                return 0
        elif(self.np[1] == 9):
            n = [2, 3, 7, 8]
            temp = n[random.randint(0, 3)]
            self.forward(temp)
            roadList.append(temp)
            if(temp == 3 or temp == 2):
                while self.np[0] != 0 and self.np[1] != 0:
                    gardet = self.garbage_detection()
                    if(gardet != 9):
                        temp = gardet
                    else:
                        temp = random.randint(1, 3)
                    self.forward(temp)
                    roadList.append(temp)
                return 0
            elif(temp == 8 or temp == 7):
                n = [1, 7, 8]
                while self.np[0] != 9 and self.np[1] != 0:
                    gardet = self.garbage_detection()
                    if(gardet != 9):
                        temp = gardet
                    else:
                        temp = n[random.randint(0, 2)]
                    self.forward(temp)
                    roadList.append(temp)
                return 0
        else:
            while self.np[0] != 0 and self.np[1] != 9:
                gardet = self.garbage_detection()
                if(gardet != 9):
                    temp = gardet
                    print('1')
                else:
                    temp = random.randint(3, 5)
                    print('2')
                print(temp)
                self.forward(temp)
                roadList.append(temp)

    def forward(self, num):
        self.np[0] += direction[num][0]
        self.np[1] += direction[num][1]
        print(self.np)
        if(self.road[self.np[0]][self.np[1]]) == 2:
            dirtPos.add(tuple(self.np))
            self.road[self.np[0]][self.np[1]] = 1


vmap = 'map.csv'
with open(vmap) as csvFile:
    imap = csv.reader(csvFile)
    listReport = list(imap)
listMap = []
for i in range(10):
    listMap.append(list(map(int, listReport[i])))
print(listMap)

tk = Tk()
ground = Canvas(tk, width=600, height=600)
ground.pack()
ground.create_rectangle(0, 0, 600, 600, fill='white')
y_position = 0
dirt = {}
for i in range(10):
    x_position = 0
    for j in range(10):
        if listMap[i][j] == 1:
            ground.create_rectangle(
                x_position, y_position, x_position+60, y_position+60, fill='gray')
        elif listMap[i][j] == 2:
            temp = ground.create_rectangle(
                x_position, y_position, x_position+60, y_position+60, fill='red')
            dirt[(i, j)] = temp
        x_position += 60
    y_position += 60


def block(x, y):
    return ground.create_rectangle(y*60, x*60, (y+1)*60, (x+1)*60)


def road_dot(x, y):
    centerX = (2*y+1)*60/2
    centerY = (2*x+1)*60/2
    return ground.create_oval(centerX-5, centerY-5, centerX+5, centerY+5, fill='white')


st = [2, 8]
smartVacuum = Robot(st, listMap)
robot_pos = st.copy()
robot = ground.create_rectangle(
    robot_pos[1]*60, robot_pos[0]*60, robot_pos[1]*60+60, robot_pos[0]*60+60, fill='green')
roadList = []
for i in range(200):
    smartVacuum.road_find()

for i in roadList:
    temp1 = (robot_pos[0], robot_pos[1])
    robot_pos[0] += direction[i][0]
    robot_pos[1] += direction[i][1]
    print(robot_pos)

    for j in range(0, 10):
        if temp1 in dirtPos:
            ground.delete(dirt[temp1])
        block(temp1[0], temp1[1])
        road_dot(temp1[0], temp1[1])
        ground.move(robot, 6*direction[i][1], 6*direction[i][0])
        tk.update()
        time.sleep(0.05)
