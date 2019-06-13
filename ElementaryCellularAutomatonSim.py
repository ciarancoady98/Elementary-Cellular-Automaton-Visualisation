import pygame
from pygame.locals import *


#Definition of constants
WINDOWWIDTH = 620
WINDOWHEIGHT = 320
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOUR = (0, 0, 0)
GENERATIONCOUNT = 16
SQUAREDIMENSIONS = 20

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
    pygame.draw.rect(window,TEXTCOLOR,(300,0,SQUAREDIMENSIONS,SQUAREDIMENSIONS))
    return True


#Initialisation of the visualisation window
pygame.init();
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
window.fill(BACKGROUNDCOLOUR)
pygame.display.set_caption("1D Cellular Automata Simulation")
currentGeneration = 0
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
        
    
