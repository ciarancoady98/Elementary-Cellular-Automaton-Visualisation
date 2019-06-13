import pygame
from pygame.locals import *

#Generate number of cells in next generation 2i+1
GENERATIONCOUNT = 64
GENERATIONWIDTH = (2*GENERATIONCOUNT) + 1


#Definition of constants
#Display values and scaling
RESOLUTIONSCALE = 2
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

#Sets a single bit of an integer number at a passed index
def setBit(number, index):
    mask = 1 << index
    number |= mask
    return number

#Applies the corresponding rule from the ruleset
#Based on the 3 cells from the previous generation
def applyRule(ruleSet, left, middle, right):
    ruleToApply = 0
    if right == 1:
        ruleToApply = setBit(ruleToApply, 0)
    if middle == 1:
        ruleToApply = setBit(ruleToApply, 1)
    if left == 1:
        ruleToApply = setBit(ruleToApply, 2)
    return int(ruleSet[ruleToApply])

#Calculates the next row in based on the rules and previous row
def createNewGeneration(ruleSet, currentGeneration, newGeneration):
    newGeneration.append(0)
    for x in range(1, (GENERATIONWIDTH-1)):
        newGeneration.append(applyRule(ruleSet,currentGeneration[x-1],currentGeneration[x],currentGeneration[x+1]))
    newGeneration.append(0)
    return newGeneration

#Iterates through the new row and prints it to the pygame canvas
def displayNewGeneration(newGeneration, currentGenerationCount):
    rowNumber = currentGenerationCount
    columnNumber = 0
    for x in newGeneration:
        if x == 1:
            pygame.draw.rect(window,SQUARECOLOUR,(columnNumber*SQUAREDIMENSIONS,rowNumber*SQUAREDIMENSIONS,SQUAREDIMENSIONS,SQUAREDIMENSIONS))
        columnNumber = columnNumber+1



#Set up the Cellular Automata rule for the prev 3 cells
ruleString = input("Please enter 1 or 0 for each of the 8 switches e.g 01111110 : ")
if len(ruleString) != 8 :
    ruleString = "01111110"
ruleSet = list(ruleString)    #convert string to list
ruleSet.reverse()             #reverse the list for easier use in the algorithm
        
#Initialisation of the visualisation window
pygame.init();
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
window.fill(BACKGROUNDCOLOUR)
pygame.display.set_caption("1D Cellular Automata Simulation")

#Runtime variables
finishedSimulation = False
currentGenerationCount = 0

#Setup the list containing the first generation
#I have picked a single cell in the centre to be turned on
currentGeneration = []
for x in range(GENERATIONWIDTH):
    if(x == GENERATIONCOUNT):
        currentGeneration.append(1)
    else:  
        currentGeneration.append(0)
displayNewGeneration(currentGeneration, currentGenerationCount)
currentGenerationCount += 1
pygame.display.update()


#Main display loop
while finishedSimulation == False:
    #If the simulation has moved off the screen stop displaying
    if currentGenerationCount == GENERATIONCOUNT:
        finishedSimulation = True
        break
    #Create the new generation
    newGeneration = []
    newGeneration = createNewGeneration(ruleSet, currentGeneration, newGeneration)
    #Add it to the canvas
    displayNewGeneration(newGeneration, currentGenerationCount)
    currentGenerationCount += 1
    currentGeneration = newGeneration.copy()
    #Update the display to show the changes
    pygame.display.update()

#Displays the end result until the user exits by pressing escape
print("done")
if finishedSimulation == True:
    while True:
        if checkExitConditions():
            end()
        
    
