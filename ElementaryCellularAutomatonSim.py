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

def createNewGeneration(generationNumber):
    return True

def displayNewGeneration():
    return True


#Initialisation of the visualisation window
pygame.init();
window = pygame.display.set_mode((WINDOWHEIGHT, WINDOWWIDTH))
window.fill(BACKGROUNDCOLOUR)
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

#Displays the end result until the user exits by pressing escape
if finishedSimulation == True:
    while True:
        if checkExitConditions():
            end()
        
    
