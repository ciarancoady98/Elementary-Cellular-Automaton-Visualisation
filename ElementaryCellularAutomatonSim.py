import pygame
from pygame.locals import *


#Definition of constants
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOUR = (0, 0, 0)
GENERATIONCOUNT = 20

#Exits pygame
def end():
    pygame.quit()

#Checks are any of the exit conditions satisified
#Returns a boolean value
def checkExitConditions():
    #Pressing escape quits
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: 
                    return True
    return False




#Initialisation of the visualisation window
pygame.init();
window = pygame.display.set_mode((WINDOWHEIGHT, WINDOWWIDTH))


#Main display loop
while True:

    if checkExitConditions():
        end()
        break

    
    window.fill(BACKGROUNDCOLOUR)
    
    
    
