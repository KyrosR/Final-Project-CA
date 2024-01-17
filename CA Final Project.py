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
class OnedimCA:
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

    # Willen we dit de cellprinter maken?
    # Heeft niet echt een doel nu, aangezien het al in layer() verwerkt zit.
    def cells_print(self):
        return self.cells

    # Determines the new cell based on rule 30
    def rule_30(self, new_cell):
        if new_cell == "111":
            return "0"
        elif new_cell == "110":
            return "0"
        elif new_cell == "101":
            return "0"
        elif new_cell == "100":
            return "1"
        elif new_cell == "011":
            return "1"
        elif new_cell == "010":
            return "1"
        elif new_cell == "001":
            return "1"
        else:
            return "0"


    # Determines the new cell based on rule 110
    def rule_110(self, new_cell):
        if new_cell == "111":
            return "0"
        elif new_cell == "110":
            return "1"
        elif new_cell == "101":
            return "1"
        elif new_cell == "100":
            return "0"
        elif new_cell == "011":
            return "1"
        elif new_cell == "010":
            return "1"
        elif new_cell == "001":
            return "1"
        else:
            return "0"

    #Determines the new cell based on rule 184
    def rule_184(self, new_cell):
        if new_cell == "111":
            return "1"
        elif new_cell == "110":
            return "0"
        elif new_cell == "101":
            return "1"
        elif new_cell == "100":
            return "1"
        elif new_cell == "011":
            return "1"
        elif new_cell == "010":
            return "0"
        elif new_cell == "001":
            return "0"
        else:
            return "0"

    #creërt nieuwe generatie cellen op basis periodieke boundaries
    def newgeneration_periodic(self):
        new_cells = []
        #voegt iedere nieuwe cell op basis van een rule toe aan de lijst van nieuwe cellen
        # Miss doen zoals bij Dirichlet want nu checkt die vgm wel heel vaak welke rule die moet toepassen
        for i in range(1, self.cell_amount+1):
            new_cell = self.cells[i-2] + self.cells[i-1] + self.cells[i%self.cell_amount]
            if self.apply_rule == 30:
                new_cells.extend(self.rule_30(new_cell))
            elif self.apply_rule == 110:
                new_cells.extend(self.rule_110(new_cell))
            elif self.apply_rule == 184:
                new_cells.extend(self.rule_184(new_cell))

        #zorgt er voor dat de nieuwe cellen op de juiste manier geprint worden, kunnen we later
        # nog aanpassen naar return als dat nodig is.
        # Ook wordt self.cells geasigned aan de niewe cellen zodat die daarna de goede nieuwe
        # generatie kan bepalen.
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
        if self.apply_rule == 30:
            first_cel = str(condition) + self.cells[0] + self.cells[1]
            new_cells.extend(self.rule_30(first_cel))
            for i in range(1, self.cell_amount-1):
                new_cell = self.cells[i-1] + self.cells[i] + self.cells[i+1]
                new_cells.extend(self.rule_30(new_cell))
            last_cel = self.cells[self.cell_amount-1] + self.cells[-1] + str(condition)
            new_cells.extend(self.rule_30(last_cel))

            self.cells = new_cells
            delimiter = ' '
            cells_configuration = delimiter.join(new_cells)
            print(cells_configuration) #return

        elif self.apply_rule == 110:
            first_cel = str(condition) + self.cells[0] + self.cells[1]
            new_cells.extend(self.rule_110(first_cel))
            for i in range(1, self.cell_amount-1):
                new_cell = self.cells[i-1] + self.cells[i] + self.cells[i+1]
                new_cells.extend(self.rule_110(new_cell))
            last_cel = self.cells[self.cell_amount-1] + self.cells[-1] + str(condition)
            new_cells.extend(self.rule_110(last_cel))

            self.cells = new_cells
            delimiter = ' '
            cells_configuration = delimiter.join(new_cells)
            print(cells_configuration) #return

        elif self.apply_rule == 184:
            first_cel = str(condition) + self.cells[0] + self.cells[1]
            new_cells.extend(self.rule_184(first_cel))
            for i in range(1, self.cell_amount-1):
                new_cell = self.cells[i-1] + self.cells[i] + self.cells[i+1]
                new_cells.extend(self.rule_184(new_cell))
            last_cel = self.cells[self.cell_amount-1] + self.cells[-1] + str(condition)
            new_cells.extend(self.rule_184(last_cel))

            self.cells = new_cells
            delimiter = ' '
            cells_configuration = delimiter.join(new_cells)
            print(cells_configuration) #return

    #creërt nieuwe generatie cellen met Neumann boundaries
    def newgeneration_Neumann(self):
        #Zelfde idee als bij Dirichletm maar nu heeft de linker/rechter buurman van de eerste/laatste cel
        # de zelfde staat als de eerste/laatse cel
        new_cells = []
        if self.apply_rule == 30:
            first_cel = self.cells[0] + self.cells[0] + self.cells[1]
            new_cells.extend(self.rule_30(first_cel))
            for i in range(1, self.cell_amount-1):
                new_cell = self.cells[i-1] + self.cells[i] + self.cells[i+1]
                new_cells.extend(self.rule_30(new_cell))
            last_cel = self.cells[self.cell_amount-1] + self.cells[-1] + self.cells[-1]
            new_cells.extend(self.rule_30(last_cel))

            self.cells = new_cells
            delimiter = ' '
            cells_configuration = delimiter.join(new_cells)
            print(cells_configuration) #return

        elif self.apply_rule == 110:
            first_cel = self.cel[0] + self.cells[0] + self.cells[1]
            new_cells.extend(self.rule_110(first_cel))
            for i in range(1, self.cell_amount-1):
                new_cell = self.cells[i-1] + self.cells[i] + self.cells[i+1]
                new_cells.extend(self.rule_110(new_cell))
            last_cel = self.cells[self.cell_amount-1] + self.cells[-1] + self.cells[-1]
            new_cells.extend(self.rule_110(last_cel))

            self.cells = new_cells
            delimiter = ' '
            cells_configuration = delimiter.join(new_cells)
            print(cells_configuration) #return

        elif self.apply_rule == 184:
            first_cel = self.cells[0] + self.cells[0] + self.cells[1]
            new_cells.extend(self.rule_184(first_cel))
            for i in range(1, self.cell_amount-1):
                new_cell = self.cells[i-1] + self.cells[i] + self.cells[i+1]
                new_cells.extend(self.rule_184(new_cell))
            last_cel = self.cells[self.cell_amount-1] + self.cells[-1] + self.cells[-1]
            new_cells.extend(self.rule_184(last_cel))

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


p = OnedimCA("000010000", 30, 1, "Neumann")
p.layers()

    

        

