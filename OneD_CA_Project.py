#Cellular Automata
#Class for 1 dim CA

"""""""""
Importing numpy for usefull functions such as the np.array, which we used to create the input list for the plot.
Importing matplotlib.pylot for the plot functions.
Importing SuperClass_CA_Project for nessecary variables.
""""""'"""
import numpy as np
import matplotlib.pyplot as plt
from SuperClass_CA_Project import CA




"""""""""
The class for the one-dimensional CA.
"""""""""

class OnedimCA(CA):

    """""""""
    The __init__ function contains all variabels for the OneD CA.
    These variables are in a speciffic order, which is also the order in which the user types 
    in the values they want for those variables.
    """""""""

    def __init__(self, start_pattern, apply_rule, layers_amount, boundary_con):
        # Uses variables written in the superclass
        super().__init__(start_pattern, apply_rule, layers_amount, boundary_con)

        # The amount of "cells" in the array, is useful for the for-loops
        self.cell_amount = len(self.cells)

        # This is going to be the list that gets plotted.
        self.configuration = []





    """""""""    
    This function derives an eight-digit binary number from the given rule number and puts those eight digits in a list. 
    Then it returns that list.
    """""""""

    def rule_to_bin(self):
        binary = bin(self.apply_rule)[2:].zfill(8)
        binary_list = list(binary)
        return binary_list
    


    """""""""
    Determines the state of the new cell based on the given rule, the state of itself and it's neighbors.
    """""""""

    def rule(self, new_cell, binary_list):
        # The eight digits of the binary list correnspond to the new state of the cell.
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
    This function creates the new generation of cells based on periodic boundaries.
    """""""""

    def newgeneration_periodic(self):
        # List of new cells.
        new_cells = []

        # For-loop that concatenates the cell with its neighbors.
        # The rule function derives the new state of the cell and puts it in the list of new cells.
        for i in range(1, self.cell_amount+1):
            new_cell = self.cells[i-2] + self.cells[i-1] + self.cells[i%self.cell_amount]
            new_cells.extend(self.rule(new_cell, self.rule_to_bin()))
        self.cells = new_cells

        # Puts the list of new cells, but now with integers in the list instead of strings.
        # It is also a np.array() which is useful for not getting errors while plotting self.configuration.
        self.configuration.append(np.array([int(x) for x in new_cells], dtype= int))
        
        


    """"""""" 
    This function creates the new generation of cells based on Dirichlet boundaries.
    The boundaries are chosen by the user and are either 1 or 0.
    """""""""

    def newgeneration_Dirichlet(self, condition):
        # List of new cells.
        new_cells = []
        
        # Determines the new state of the first cell with Dirichlet boundaries 1 or 0 and adds it
        # to the list of new cells.
        first_cell = str(condition) + self.cells[0] + self.cells[1]
        new_cells.extend(self.rule(first_cell, self.rule_to_bin()))

        # For-loop that determines the state of all cells except for the last cell.
        # Adds all those new cells to the list of new cells.
        for i in range(1, self.cell_amount-1):
            new_cell = self.cells[i-1] + self.cells[i] + self.cells[i+1]
            new_cells.extend(self.rule(new_cell, self.rule_to_bin()))
        
        # Determines the new state of the last cell with Dirichlet boundaries 1 or 0 and adds it
        # to the list of newcells.
        last_cell = self.cells[self.cell_amount-1] + self.cells[-1] + str(condition)
        new_cells.extend(self.rule(last_cell, self.rule_to_bin()))

        # Puts the list of new cells, but now with integers in the list instead of strings.
        # It is also a np.array() which is useful for not getting errors while plotting self.configuration.
        self.cells = new_cells
        self.configuration.append(np.array([int(x) for x in new_cells], dtype= int))

        



    """"""""" 
    This function creates the new generation of cells based on periodic boundaries.
    The boundaries are derived from the state of the first/last cells.
    The boundary on the left is the same as the state of the first cell.
    The boundary on the right is the same as the state of the last cell.
    """""""""

    def newgeneration_Neumann(self):
        # List of new cells
        new_cells = []

        # Determines state of the first cell and adds it to the list of new cells.
        first_cell = self.cells[0] + self.cells[0] + self.cells[1]
        new_cells.extend(self.rule(first_cell, self.rule_to_bin()))

        # For-loop that determines the state of all cells except for the last cell.
        # Adds all those new cells to the list of new cells.
        for i in range(1, self.cell_amount-1):
            new_cell = self.cells[i-1] + self.cells[i] + self.cells[i+1]
            new_cells.extend(self.rule(new_cell, self.rule_to_bin()))
        
        # Determines state of the last cell and adds it to the list of new cells.
        last_cell = self.cells[self.cell_amount-1] + self.cells[-1] + self.cells[-1]
        new_cells.extend(self.rule(last_cell, self.rule_to_bin()))
        
        # Puts the list of newcells, but now with integers in the list instead of strings.
        # It is also a np.array() which is useful for not getting errors while plotting self.configuration.
        self.cells = new_cells
        self.configuration.append(np.array([int(x) for x in new_cells], dtype= int))
        

        
    
    """""""""
    This function first determines which boundary was given.
    Then it calls a specific function corresponding to that boundary and repeats that an x amount of times,
    where x is the value of the number of layers the user wants on top of the given start pattern.
    """""""""

    def update(self):
        # Puts the start pattern of cells, but now with integers in the list instead of strings.
        # It is also a np.array() which is useful for not getting errors while plotting self.configuration.
        self.configuration.append(np.array([int(x) for x in self.cells], dtype= int))

        # Determines which boundary was given and calls that function an x amount of times.
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
    This function plots the list containing the start pattern and all lists of new cells.
    """""""""

    def plot(self):
        plt.imshow(self.configuration, cmap='Greys', interpolation='nearest')
        plt.axis('off')
        plt.show()

   

# Makes p an instance of the class with the values of the variables that are necessary for the program to run.
# Could be changed to accept inputs for a more interactive style.
p = OnedimCA("00000000000010000000000000", 60, 20, "periodic")

# Calls the functions update() and plot() with the values of the variables from above.
# This makes sure that the program runs and that the result is plotted.
p.update()
p.plot()


