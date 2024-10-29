from enum import Enum
from queue import PriorityQueue
class Key(Enum):
    LEFT=0
    MIDDLE=1
    RIGHT=2


def h(pos1,pos2):
    x1,y1=pos1
    x2,y2=pos2
    return abs(x1-x2) + abs(y1-y2)

def algorithm(start,end,game_nodes):

    # defining sets
    frontier=PriorityQueue() # open set
    interior=[]  # closed set

    frontier_hash=[]

    # came_from={}



    #  format : (f_score , node)
    g_score={node : float("inf") for row in game_nodes for node in row}
    g_score[start]=0
    f_score={node : float("inf") for row in game_nodes for node in row}
    f_score[start]=h(start.get_pos(),end.get_pos())

    if start not in frontier_hash:
        frontier.put((0,start))
        frontier_hash.append(start)

    while not frontier.empty() : 
        current=frontier.get()[1]
        
        for neighbor in  current.neighbors:
            print(neighbors)