import pygame
from models import make_blocks
from colors import *
from utils import Key

width=800

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





#main func
def main() ->None :
    run=True
    rows=cols=50
    size=width//rows

    # creating and storing every block in the screen
    grid_blocks=make_blocks(rows,cols,win_size=width,win=win)

    # initial and final node
    start_node=None
    end_node=None

    started=False

    while run:        
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run=False
                continue
            x,y=pygame.mouse.get_pos()  
            mouse=pygame.mouse.get_pressed()

            ###### MOUSE BTN ########

            # left btn
            if mouse[Key["LEFT"].value] :
                node=find_node(x,y,size,grid_blocks)
                if event.type == pygame.MOUSEBUTTONDOWN and not end_node:
                    if not start_node:
                        start_node=node
                        node.set_start()
                        continue

                    elif not end_node and node!=start_node:
                        end_node=node
                        node.set_end() 
                        continue

                else:
                    if node != start_node and node!=end_node and start_node and end_node:
                        node.set_barrier()   
                        continue

            # right btn
            elif mouse[Key["RIGHT"].value]:
                node=find_node(x,y,size,grid_blocks)
                if node ==start_node:
                    start_node=None
                elif node ==end_node:
                    end_node=None
                node.reset()

            # #### KEYBOARD BTN  ######
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE and not started:
                    # algorithm()
                    pass


        for blocks in grid_blocks:
            for block in blocks:
                block.draw()

        draw_grid(rows,cols,size)

        pygame.display.flip()


    pygame.quit()


if __name__=="__main__":
    main()    
