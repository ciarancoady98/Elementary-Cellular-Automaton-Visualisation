# Elementary-Cellular-Automaton-Visualisation

A small Python program that visualises Elementary Cellular Automaton http://mathworld.wolfram.com/ElementaryCellularAutomaton.html

Dependencies: Pygame https://www.pygame.org/

When ran the program will ask for the ruleset that is to be used when creating the next generation of cells. A ruleset is an 8-bit binary value e.g. 01111110.

After this a pygame window will open displaying the simulated Automaton. To exit the program simply press escape key when the simulation is complete.

By default the program will calculate 64 generations but this can be changed by altering the GENERATIONCOUNT variable.

If the pygame window is too big or too small it can be scaled by changing the RESOLUTIONSCALE variable.
