import pygame
from colors import *


# how to write pyi files

class Node:

    def __init__(self,row,col,size,win):
        self.row=row
        self.col=col
        self.win=win
        self.size=size
        self.x=row*self.size
        self.y=col*self.size
        self.color=WHITE
        self.neighbors=[]

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


#creating all grid blocks in the screen
def make_blocks(rows,cols,win_size,win)->list[2]:

    size=win_size//rows
    block=[]
    for row in range(rows):
        block.append([])
        for col in range(cols):
            node=Node(row,col,size,win)
            block[row].append(node)

    return block      

# calculate block row and col
def find_node(x,y,size,grid_block):
    row=x//size
    col=y//size
    return grid_block[row][col]