import math, pygame
from math import pi

# This is the Wall-E class
class WallE:
    def turn(self, angle):
        x = self.direction[0]
        y = self.direction[1]
        self.direction = [int(x*math.cos(angle)-y*math.sin(angle)),
                            int(x*math.sin(angle)+y*math.cos(angle))]
        self.image = self.imageDict[str(self.direction)]


    #Function that turns Wall-E 90 degrees to the right
    def turn_right(self):
        self.turn(0.5*pi)

    #Function that turns Wall-E 90 degrees to the left
    def turn_left(self):
        self.turn(-0.5*pi)

    #Function that returns true if Wall-E stands on a box
    def check_on_box(self):
        if self.board[self.position[0]][self.position[1]] == 2:
            return True
        else:
            return False

    #Function that returns true if Wall-E stands in front of a wall
    def check_wall(self):
        x = self.position[0] + self.direction[0]
        y = self.position[1] + self.direction[1]
        if -1 < x < len(self.board) and -1 < y < len(self.board[0]):
            if self.board[x][y]==1:
                return True
            return False
        else:
            return True

    #Function that picks up a box - it breaks Wall-E if you try to pick up a box
    #that isn't there!
    def pick_up_box(self):
        if self.board[self.position[0]][self.position[1]] == 2:
            self.board[self.position[0]][self.position[1]] = 0
        else:
            self.broken = True

    #Function that drops a box - it breaks Wall-E if you try to drop a box on top
    #of another box!
    def drop_box(self):
        if self.board[self.position[0]][self.position[1]] == 0:
            self.board[self.position[0]][self.position[1]] = 2
        else:
            self.broken = True

    #Function that makes Wall-E takes one step forward. It breaks Wall-E if you
    #try to take 2 steps at once!
    def move(self):
        if not self.action:
            self.position[0] += self.direction[0]
            self.position[1] += self.direction[1]
            if -1 < self.position[0] < len(self.board) and -1 < self.position[1] < len(self.board[0]):
                if self.board[self.position[0]][self.position[1]]==1:
                    self.broken = true
            else:
                self.broken = True
            self.action = True
        else:
            self.broken = True

    # Initialisation function of Wall-E Class
    def __init__(self, position, board, image):
        self.position = position
        self.board = board
        self.direction = [1,0]
        self.image = image
        il = pygame.transform.flip(self.image, True, False)
        ir = pygame.transform.rotate(self.image, 0)
        id = pygame.transform.rotate(self.image, -90)
        iu = pygame.transform.rotate(self.image, 90)
        self.imageDict = {'[1, 0]':ir, '[-1, 0]':il, '[0, 1]':id, '[0, -1]':iu}
        self.action = False
        self.broken = False

        # DO NOT CHANGE ANYTHING ABOVE THIS LINE!!!!!
        #-----------------------------------------------------------------------
        # Declare variables you need here (Please formulate these variables
        # in ALL CAPS to avoid clashes with existing variable!!!)
        # and make sure they are at this indent level

        self.EXAMPLE = 0

    # Declare any help functions here (also use all caps for these!!), it has to include self in the argument.
    # and make sure they are at this indent level
    def EXAMPLE_FUNCTION(self):
        pass


# These are the 5 functions you have to fill in
    def walk_back_and_forth(self):
        if not self.check_wall():
           self.move()
        else:
           self.turn_right()
           self.turn_right()
        
     
        
     
        
     
        
     
        

        
 

   

        

    def walk_a_lap(self):
        if self.check_wall():
           self.turn_right()
        else:
           self.move() 

        

    def find_the_box(self):
        while not self.check_on_box():  # 当不在箱子上时
            if self.check_wall():  # 如果碰到墙，转向
                self.turn_left()
            else:
                self.move()  # 向前移动直到找到箱子

        

    def swap_all_boxes(self):
        new_position = self.position[:]  # 记录初始位置
        boxes = []  # 用于存储箱子的位置
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                if self.board[x][y] == 2:  # 如果当前位置有箱子
                    boxes.append([x, y])  # 保存箱子的位置
        if len(boxes) >= 2:
            first_box = boxes[0]
            last_box = boxes[-1]
            # 交换两个箱子
            self.board[first_box[0]][first_box[1]] = 0  # 清除第一个箱子
            self.board[last_box[0]][last_box[1]] = 2  # 在第二个位置放置箱子
            
        while self.position != new_position:
            self.move()


    def CHECK_ON_WALL(self):
    
        return self.check_wall()

    def walk_around_obstacle(self):
        while self.check_wall():  # 如果前方是墙
            self.turn_left()  # 转弯绕过墙
        self.move()  # 然后继续移动
