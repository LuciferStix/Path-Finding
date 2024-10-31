import pygame
from colors import *


# how to write pyi files

class Node:
    # class variable
    (win_H := 0),(win_W :=0)
    total_rows=0
    total_cols=0

    def __init__(self,row,col,size,win):
        self.row=row
        self.col=col
        self.win=win
        self.size=size
        self.x=row*self.size
        self.y=col*self.size
        self.color=WHITE
        self.neighbors=[]

    def fix_win_dim(self):
        Node.win_H=self.win.get_height()
        Node.win_W=self.win.get_width()
        

    def draw(self):
        pygame.draw.rect(self.win,self.color,(self.x,self.y,self.size,self.size))

    def get_pos(self):
        return self.x,self.y

    def is_visited(self):
        return self.color==RED
    
    def is_open(self):
        return self.color==GREEN
    
    def is_start(self):
        return self.color==PURPLE

    def is_end(self):
        return self.color==ORANGE
    
    def is_barrier(self):
        return self.color==BLACK

    def set_visited(self):
        self.color=RED

    def set_open(self):
        self.color=GREEN

    def set_barrier(self):
        self.color=BLACK

    def set_start(self):
        self.color=PURPLE

    def set_end(self):
        self.color=ORANGE
        
    def reset(self):
        self.color=WHITE

    def make_path(self):
        self.color=BLUE
    def __lt__(self,other):
        return False

    def update_neighbors(self,grid):

        # this is done to prevent adding same nodes multiple times
        #  otherwise it appends the same node multiple time if pressed the play btn (space bar)
        self.neighbors=[]



        # getting nodes from top, bottom ,left ,right
        top=grid[self.row-1][self.col] if self.row-1 >= 0 else 0
        bottom=grid[self.row+1][self.col] if self.row+1 < Node.total_rows else 0
        left=grid[self.row][self.col-1] if self.col-1 >=0 else 0 
        right=grid[self.row][self.col+1] if self.col+1 < Node.total_cols else 0

        # using short circuiting (thats why else has 0 in above code)

        if top and not top.is_barrier():
            self.neighbors.append(top)
        if bottom and not bottom.is_barrier():
            self.neighbors.append(bottom)
        if left and not left.is_barrier():
            self.neighbors.append(left)
        if right and not right.is_barrier():
            self.neighbors.append(right)
        




#creating all grid blocks in the screen
def make_blocks(rows,cols,win)->list[2]:
    win_size=win.get_height()
    size=win_size//rows
    block=[]
    for row in range(rows):
        block.append([])
        for col in range(cols):
            node=Node(row,col,size,win)
            block[row].append(node)

    return block      

# calculate node from row and col
def find_node(x,y,size,grid_block):
    row=x//size
    col=y//size
    return grid_block[row][col]


