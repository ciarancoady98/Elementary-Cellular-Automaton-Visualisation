import pygame
from pygame.locals import *


#Definition of constants
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOUR = (0, 0, 0)
GENERATIONCOUNT = 20

#Exits when the simulation is complete
def end():
    pygame.quit()

#Checks are any of the exit conditions satisified
def checkExitConditions(currentGeneration):
    #Pressing escape quits
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: 
                    end()
    #Reaching the GENERATIONCOUNT quits
    if currentGeneration == GENERATIONCOUNT:
        end()




#Initialisation of the visualisation window
pygame.init();
window = pygame.display.set_mode((WINDOWHEIGHT, WINDOWWIDTH))


#Main display loop
while True:
    window.fill(BACKGROUNDCOLOUR)
    checkExitConditions(1)
    
    
