#!/usr/bin/env python
import pygame.midi
import time



def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use


    rollimg = pygame.image.load("piano2.png")

    surface_sz = 480   # Desired physical surface size, in pixels.

    main_surface = pygame.display.set_mode((rollimg.get_width(),rollimg.get_height()))

    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(80)





    offset=0;
    
    
    notes_status = [0]*400
    
    
    firstframe = True;

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        main_surface.fill((255, 200, 255))
        
        
        main_surface.blit(rollimg,[-offset,0])
        offset+=3
        
        
        # draw red dots
        for idx in range(0,66):
            y = int( idx*4.85+87-1 )
            
            col1 = main_surface.get_at((0,y))
            col2 = main_surface.get_at((0,y+1))
            col3 = main_surface.get_at((0,y-1))
            
            pygame.draw.line(main_surface,[128,128,0],[0,y],[main_surface.get_width(),y],1)
            main_surface.set_at((0, y), [255,0,0])
            
            br = sum(col1[0:2]+col2[0:2]+col3[0:2])/9
            
            note_tr = idx+64-14
            if br<128:
                if notes_status[note_tr]==0:
                    player.note_on(note_tr,127)
                    notes_status[note_tr]=1
                else:
                    pass
            else:
                player.note_off(note_tr,127)
                notes_status[note_tr]=0


        #player.note_on(64, 127)
        time.sleep(0.03)
        #player.note_off(64, 127)
        

        pygame.display.flip()
        
        if firstframe:
            firstframe=False
            time.sleep(5);

    for i in range(0,200):
        player.note_off(i,0)
    del player
    pygame.midi.quit()
    pygame.quit()     # Once we leave the loop, close the window.

main()
