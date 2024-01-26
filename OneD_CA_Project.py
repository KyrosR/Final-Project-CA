#Cellular Automata
#Class for 1 dim CA

"""""""""
Importing numpy for usefull functions such as the np.array wich we used to make the input list for the plot.
Importing matplotlib.pylot for the plot functions.
Importing SuperClass_CA_Project for nessecary variables.
""""""'"""
import numpy as np
import matplotlib.pyplot as plt
from SuperClass_CA_Project import CA




"""""""""
The class for the 1 dimensional CA.
"""""""""

class OnedimCA(CA):

    """""""""
    The __init__ functions wich contains all variabels for the OneD CA.
    These variables stand in a speciffic order, that is also the order in wich the user types 
    in what the want values of those variables need to be.
    """""""""

    def __init__(self, start_pattern, apply_rule, layers_amount, boundary_con):
        # Uses variables written in the superclass
        super().__init__(start_pattern, apply_rule, layers_amount, boundary_con)

        # The amount of "cells" in the array, is useful for the for-loops
        self.cell_amount = len(self.cells)

        # This is going to be the list wich get plotted.
        self.configuration = []





    """""""""    
    Functions wich from the given rule derives a certain eightdiget binary number and puts those 
    eight digets in a list. Then it returns that list.
    """""""""

    def rule_to_bin(self):
        binary = bin(self.apply_rule)[2:].zfill(8)
        binary_list = list(binary)
        return binary_list
    


    """""""""
    Determines the stat of the new cell based on the given rule, the state of itself and it's neighbours.
    """""""""

    def rule(self, new_cell, binary_list):
        # The eight digets of the binary list corrensponds with the new state of the cell.
        if new_cell == "111":
            return binary_list[0]
        elif new_cell == "110":
            return binary_list[1]
        elif new_cell == "101":
            return binary_list[2]
        elif new_cell == "100":
            return binary_list[3]
        elif new_cell == "011":
            return binary_list[4]
        elif new_cell == "010":
            return binary_list[5]
        elif new_cell == "001":
            return binary_list[6]
        else:
            return binary_list[7]




    """"""""" 
    This function creates the newgeneration of cells based on periodic boundaries.
    """""""""

    def newgeneration_periodic(self):
        # List of newcells.
        new_cells = []

        # For loop wich concatenates the cell wich it's neighbours, the through the rule function
        # derives the new state of the cell and put it in the list of newcells.
        for i in range(1, self.cell_amount+1):
            new_cell = self.cells[i-2] + self.cells[i-1] + self.cells[i%self.cell_amount]
            new_cells.extend(self.rule(new_cell, self.rule_to_bin()))
        self.cells = new_cells

        # Puts the list of newcells, but now with intergers in the list instead of strings.
        # It is also a np.array() wich is usefull for not getting errors while plotting self.configuration.
        self.configuration.append(np.array([int(x) for x in new_cells], dtype= int))
        
        


    """"""""" 
    This function creates the newgeneration of cells based on Dirichlet boundaries.
    The boundaries are chosen by the user and are either 1 or 0.
    """""""""

    def newgeneration_Dirichlet(self, condition):
        # List of newcells.
        new_cells = []
        
        # Determens the new state of the first cell with Dirichlet boundary 1 or 0 and puts it
        # in the list of newcells.
        first_cell = str(condition) + self.cells[0] + self.cells[1]
        new_cells.extend(self.rule(first_cell, self.rule_to_bin()))

        # For loop that determens the state of all the other cells exept for the last cell.
        # Puts all those newcells in the list of newcells.
        for i in range(1, self.cell_amount-1):
            new_cell = self.cells[i-1] + self.cells[i] + self.cells[i+1]
            new_cells.extend(self.rule(new_cell, self.rule_to_bin()))
        
        # Determens the new state of the last cell with Dirichlet boundary 1 or 0 and puts it
        # in the list of newcells.
        last_cell = self.cells[self.cell_amount-1] + self.cells[-1] + str(condition)
        new_cells.extend(self.rule(last_cell, self.rule_to_bin()))

        # Puts the list of newcells, but now with intergers in the list instead of strings.
        # It is also a np.array() wich is usefull for not getting errors while plotting self.configuration.
        self.cells = new_cells
        self.configuration.append(np.array([int(x) for x in new_cells], dtype= int))

        



    """"""""" 
    This function creates the newgeneration of cells based on periodic boundaries.
    The boundaries are derived from the state of the first/last cells.
    The boundary on the left is the same as the state of the first cell.
    The boundary on the right is the same as the state of the last cell.
    """""""""

    def newgeneration_Neumann(self):
        # List of newcells
        new_cells = []

        # Determens state of the first cell and puts it in the list of newcells.
        first_cell = self.cells[0] + self.cells[0] + self.cells[1]
        new_cells.extend(self.rule(first_cell, self.rule_to_bin()))

        # For loop that determens the state of all the other cells exept for the last cell.
        # Puts all those newcells in the list of newcells.
        for i in range(1, self.cell_amount-1):
            new_cell = self.cells[i-1] + self.cells[i] + self.cells[i+1]
            new_cells.extend(self.rule(new_cell, self.rule_to_bin()))
        
        # Determens state of the last cell and puts it in the list of newcells.
        last_cell = self.cells[self.cell_amount-1] + self.cells[-1] + self.cells[-1]
        new_cells.extend(self.rule(last_cell, self.rule_to_bin()))
        
        # Puts the list of newcells, but now with intergers in the list instead of strings.
        # It is also a np.array() wich is usefull for not getting errors while plotting self.configuration.
        self.cells = new_cells
        self.configuration.append(np.array([int(x) for x in new_cells], dtype= int))
        

        
    
    """""""""
    This function fisrst determens wich boundary was given.
    Then it calls a speciffic function corresponding with that boundary and repeats that an x amounts,
    with x being the value of the amount of layers the user wants on top of the given start pattern.
    """""""""

    def update(self):
        # Puts the start pattern of cells, but now with intergers in the list instead of strings.
        # It is also a np.array() wich is usefull for not getting errors while plotting self.configuration.
        self.configuration.append(np.array([int(x) for x in self.cells], dtype= int))

        # Determens wich boundary was given and calls that function an x amount of times.
        if self.boundary_con == "periodic":
            for i in range(1, self.layers_amount+1):
                self.newgeneration_periodic()
        elif self.boundary_con == "Dirichlet":
            condition = int(input("Choose between 0 of 1. ")) #1 or 0
            for i in range(1, self.layers_amount+1):
                self.newgeneration_Dirichlet(condition)
        elif self.boundary_con == "Neumann":
            for i in range(1, self.layers_amount+1):
                self.newgeneration_Neumann()





    """""""""
    This function plots the list containing the start pattern and all lists of newcells.
    """""""""

    def plot(self):
        plt.imshow(self.configuration, cmap='Greys', interpolation='nearest')
        plt.axis('off')
        plt.show()

   

# Makes p an ... of the class with the values of the variables nessecary for the program to run.
# Could be changed to inputs for a more interactive style.
p = OnedimCA("00000000000010000000000000", 60, 20, "periodic")

# Calls the functions update() and plot() with the values of the variables from above.
# This makes sure thet the program is run and that the result is plotted.
p.update()
p.plot()


