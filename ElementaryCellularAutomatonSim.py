import pygame
from pygame.locals import *

#generate number of cells in next generation 2i+1
GENERATIONCOUNT = 32
GENERATIONWIDTH = (2*GENERATIONCOUNT) + 1


#Definition of constants
#Display values and scaling
RESOLUTIONSCALE = 10
SQUAREDIMENSIONS = 2*RESOLUTIONSCALE
WINDOWWIDTH = GENERATIONWIDTH*SQUAREDIMENSIONS
WINDOWHEIGHT = GENERATIONCOUNT*SQUAREDIMENSIONS
SCREENCENTRE = WINDOWWIDTH/2 - SQUAREDIMENSIONS
#RGB values
SQUARECOLOUR = (255, 255, 255)
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

def applyRule(left, middle, right):
    return 1

def createNewGeneration():
    for x in range(1, (GENERATIONWIDTH-1)):
        currentGeneration[x] = applyRule(lastGeneration[x-1],lastGeneration[x],lastGeneration[x+1])
    return True

def displayNewGeneration():
    rowNumber = currentGenerationCount
    columnNumber = 0
    for x in currentGeneration:
        if x == 1:
            pygame.draw.rect(window,SQUARECOLOUR,(columnNumber*SQUAREDIMENSIONS,rowNumber*SQUAREDIMENSIONS,SQUAREDIMENSIONS,SQUAREDIMENSIONS))
        columnNumber = columnNumber+1



#set up the cellular automata rule for the prev 3 cells
ruleNumber = input("Please enter 1 or 0 for each of the 8 switches e.g 01111110 : ")
if len(ruleNumber) != 8 :
    ruleNumber = "01111110"
cellAutoRule = list(ruleNumber)    #convert string to list
cellAutoRule.reverse()             #reverse the list for easier use in the algorithm
#print("cell rules : ", cellAutoRule)
        
#Initialisation of the visualisation window
pygame.init();
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
window.fill(BACKGROUNDCOLOUR)
pygame.display.set_caption("1D Cellular Automata Simulation")

currentGenerationCount = 0
ruleSet = [
#Setup the list containing the first generation
firstGeneration = []
for x in range(GENERATIONWIDTH):
    if(x == GENERATIONCOUNT):
        firstGeneration.append(1)
    else:  
        firstGeneration.append(0)
currentGeneration = firstGeneration

finishedSimulation = False

#Main display loop
while finishedSimulation == False:

    #Allows the user to exit before the simulation is finished
    if checkExitConditions():
        end()
        break
    lastGeneration = currentGeneration
    createNewGeneration()
    displayNewGeneration()
    currentGenerationCount = currentGenerationCount + 1
    pygame.display.update()

#Displays the end result until the user exits by pressing escape
if finishedSimulation == True:
    while True:
        if checkExitConditions():
            end()
        
    
