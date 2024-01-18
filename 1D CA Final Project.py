#Cellular Automata
#Class for 1 dim CA
#Opmerkingen:
#1.Ik heb cell_amount wegelaten als argument van innit, cell_amount is namelijk de lengte van self.cells.
#2. Regel_30,110,184 werkt, het argument apply_rule moet je de waarde van de rule aan meegeven.
# ook werken de boundaries periodic, Dirichlet en Neumann deze namen moet je meegeven aan boundary_con.
#4 Idk wat we met cells_print moeten, omdat het al eigl verwerkt zit in layers().
#5 Miss is het een goed idee om de rules(30 enz) in een aparte file te zetten, miss ook de verschillende
#boundaries in een andere file.
#6 We zouden extra rules kunnen toevoegen, kost niet al te veel tijd omdat ze allemaal op elkaar lijken.
#7 Nu print het programma de nextgenerations cells, miss later veranderen in return voor het visuele aspect.
#8 Miss eerst checken welke boundary dan welke rule en dan de nieuwe generatie bepalen, miss onodig veel checks
# nu met if elif.
#9 Vraag over Dirichlet of beide zijden 1 of 0 zijn of dat het per zijde kan verschillen.
#8 Als je online bent dan kan je appen als je iets niet snapt ofz of wat anders ofz idk. groeten Ruben.
class CA:

    def __init__(self, start_pattern, apply_rule, layers_amount, boundary_con):
        # The pattern of one's and zero's the 1 dimensional array
        self.start_patern = start_pattern
        # The rule that is applied to a given array
        self.apply_rule = apply_rule  
        # The amount of array's(layers) of nextgeneration cells.
        self.layers_amount = layers_amount 
        # Putting the start_pattern in a list
        self.cells = list(self.start_patern)
        # The amount of "cells" in the array, is useful for the for-loops
        self.cell_amount = len(self.cells)
        # The boundary conditions for the firs/last cell of the array.
        self.boundary_con = boundary_con

class OnedimCA(CA):

    def __init__(self, start_pattern, apply_rule, layers_amount, boundary_con):
        super().__init__(start_pattern, apply_rule, layers_amount, boundary_con)


    # Willen we dit de cellprinter maken?
    # Heeft niet echt een doel nu, aangezien het al in layer() verwerkt zit.
    def rule_to_bin(self):
        binary = bin(self.apply_rule)[2:].zfill(8)
        binary_list = list(binary)
        return binary_list

    # Determines the new cell based on rule 30
    def rule(self, new_cell, binary_list):
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


    #creërt nieuwe generatie cellen op basis periodieke boundaries
    def newgeneration_periodic(self):
        new_cells = []
        #voegt iedere nieuwe cell op basis van een rule toe aan de lijst van nieuwe cellen
        # Miss doen zoals bij Dirichlet want nu checkt die vgm wel heel vaak welke rule die moet toepassen
        for i in range(1, self.cell_amount+1):
            new_cell = self.cells[i-2] + self.cells[i-1] + self.cells[i%self.cell_amount]
            new_cells.extend(self.rule(new_cell, self.rule_to_bin()))
        self.cells = new_cells
        delimiter = ' '
        cells_configuration = delimiter.join(new_cells)
        print(cells_configuration) #return
        
        

    #creërt nieuwe generatie cellen met Dirichlet boundaries gekozen door user,(1 of 0)
    def newgeneration_Dirichlet(self, condition):
        new_cells = []
        # Zelfde idee als bij periodic, alleen eerst checken welke rule
        # Eerst de nieuwe eerste cel bepalen en dan als laatst de laatste cel, komt door boundary
        # de linker/rechter buurman van de eerste/laatse cel is of wel 1 of 0
        
        first_cell = str(condition) + self.cells[0] + self.cells[1]
        new_cells.extend(self.rule(first_cell, self.rule_to_bin()))
        for i in range(1, self.cell_amount-1):
            new_cell = self.cells[i-1] + self.cells[i] + self.cells[i+1]
            new_cells.extend(self.rule(new_cell, self.rule_to_bin()))
        last_cell = self.cells[self.cell_amount-1] + self.cells[-1] + str(condition)
        new_cells.extend(self.rule(last_cell, self.rule_to_bin()))

        self.cells = new_cells
        delimiter = ' '
        cells_configuration = delimiter.join(new_cells)
        print(cells_configuration) #return

        

    #creërt nieuwe generatie cellen met Neumann boundaries
    def newgeneration_Neumann(self):
        #Zelfde idee als bij Dirichletm maar nu heeft de linker/rechter buurman van de eerste/laatste cel
        # de zelfde staat als de eerste/laatse cel
        new_cells = []
        first_cell = self.cells[0] + self.cells[0] + self.cells[1]
        new_cells.extend(self.rule(first_cell, self.rule_to_bin()))
        for i in range(1, self.cell_amount-1):
            new_cell = self.cells[i-1] + self.cells[i] + self.cells[i+1]
            new_cells.extend(self.rule(new_cell, self.rule_to_bin))
        last_cell = self.cells[self.cell_amount-1] + self.cells[-1] + self.cells[-1]
        new_cells.extend(self.rule(last_cell, self.rule_to_bin))

        self.cells = new_cells
        delimiter = ' '
        cells_configuration = delimiter.join(new_cells)
        print(cells_configuration) #return

        
    
    #Zorgt ervoor dat de nieuwe generatie x aantal keer geprint wordt en bepaalt met welke boundaries.
    def layers(self):
        # Start patroon in juiste print wijze zetten
        delimiter = ' '
        first_layer = delimiter.join(self.cells)
        print(first_layer)
        if self.boundary_con == "periodic":
            for i in range(1, self.layers_amount+1):
                self.newgeneration_periodic()
        elif self.boundary_con == "Dirichlet":
            condition = int(input("Kies tussen 0 of 1. ")) #1 or 0
            for i in range(1, self.layers_amount+1):
                self.newgeneration_Dirichlet(condition)
        elif self.boundary_con == "Neumann":
            for i in range(1, self.layers_amount+1):
                self.newgeneration_Neumann()


p = OnedimCA("000010000", 90, 20, "periodic")
p.layers()

    

        

