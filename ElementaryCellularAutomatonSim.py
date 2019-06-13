import pygame
from pygame.locals import *

#generate number of cells in next generation 2i+1
GENERATIONCOUNT = 32
GENERATIONWIDTH = (2*GENERATIONCOUNT) + 1


#Definition of constants
#Display values and scaling
RESOLUTIONSCALE = 10
WINDOWWIDTH = GENERATIONWIDTH*RESOLUTIONSCALE
WINDOWHEIGHT = GENERATIONCOUNT*RESOLUTIONSCALE
SQUAREDIMENSIONS = 2*RESOLUTIONSCALE
SCREENCENTRE = WINDOWWIDTH/2 - SQUAREDIMENSIONS
#RGB values
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOUR = (0, 0, 0)




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

def createNewGeneration(generationNumber):
    
    return True

def displayNewGeneration():
    pygame.draw.rect(window,TEXTCOLOR,(SCREENCENTRE,0,SQUAREDIMENSIONS,SQUAREDIMENSIONS))
    return True


#Initialisation of the visualisation window
pygame.init();
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
window.fill(BACKGROUNDCOLOUR)
pygame.display.set_caption("1D Cellular Automata Simulation")
currentGeneration = 0
lastGeneration = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
finishedSimulation = False

#Main display loop
while finishedSimulation == False:

    #Allows the user to exit before the simulation is finished
    if checkExitConditions():
        end()
        break
    createNewGeneration(currentGeneration)
    displayNewGeneration()
    currentGeneration = currentGeneration + 1
    pygame.display.update()

#Displays the end result until the user exits by pressing escape
if finishedSimulation == True:
    while True:
        if checkExitConditions():
            end()
        
    
