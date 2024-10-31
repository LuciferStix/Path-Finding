import pygame
from models import *
from colors import *
from utils import *

width=900

#screen setup
win=pygame.display.set_mode((width,width))
pygame.display.set_caption("Path finder")


#func to draw the grid lines
def draw_grid(rows,cols,gap):
    for row in range(rows):
        pygame.draw.line(win,BLACK,(0,row*gap),(width,row*gap))
    for col in range(cols):
        pygame.draw.line(win,BLACK,(col*gap,0),(col*gap,width))

#a clock object (purpose :  fixed fps)
clock=pygame.time.Clock()


def draw(rows,cols,gap,game_nodes):
    win.fill(WHITE)

    #  drawing each nodes on the surface
    for blocks in game_nodes:
            for block in blocks:
                block.draw()


    draw_grid(rows,cols,gap)    
    pygame.display.update()        


#main func
def main() ->None :
    run=True
    rows=cols=50
    Node.total_rows=rows
    Node.total_cols=cols
    size=width//rows

    # creating and storing every block in the screen
    game_nodes=make_blocks(rows,cols,win=win)

    # initial and final node
    start_node=None
    end_node=None

    started=False

    while run:
        clock.tick(30)
        for event in pygame.event.get():

            if event.type == pygame.QUIT :
                run=False
                continue

            x,y=pygame.mouse.get_pos()
            mouse=pygame.mouse.get_pressed() # output : (left btn,middle btn,right btn) ->(false,false,false)

            ###### MOUSE BTN ########

            # left btn
            if mouse[Key["LEFT"].value] :
                node=find_node(x,y,size,game_nodes)

                #  check for single mouse click (purpose : to mark start and end node)
                if event.type == pygame.MOUSEBUTTONDOWN and not end_node:
                    if not start_node:
                        start_node=node
                        node.set_start()
                        continue

                    elif not end_node and node!=start_node:
                        end_node=node
                        node.set_end() 
                        continue

                # check for mouse btn hold (purpose : to draw barriers )
                else:
                    if node != start_node and node!=end_node and start_node and end_node:
                        node.set_barrier()   
                        continue

            # right btn
            elif mouse[Key["RIGHT"].value]:
                node=find_node(x,y,size,game_nodes)
                if node ==start_node:
                    start_node=None
                elif node ==end_node:
                    end_node=None
                node.reset()

            # #### KEYBOARD BTN  ######
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE and not started:
                    # algorithm()
                    count=0
                    for row_node in game_nodes:
                        for col_node in row_node:
                            if not col_node.is_barrier():
                                col_node.update_neighbors(game_nodes)

                    print("complete")
                    algorithm(lambda:draw(rows,cols,size,game_nodes),start_node,end_node,game_nodes,)
                    continue
                    

       
        draw(rows,cols,size,game_nodes)
        

    pygame.quit()


if __name__=="__main__":
    main()  
