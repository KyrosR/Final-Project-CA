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
class TwodimCA:
    def __init__(self, start_pattern, apply_rule, generations_amount, boundary_con):
        
        # The pattern of one's and zero's the 1 dimensional array
        self.start_patern = start_pattern
        # The rule that is applied to a given array
        self.apply_rule = apply_rule  
        # The amount of array's(layers) of nextgeneration cells.
        self.generations_amount = generations_amount
        # Putting the start_pattern in a list
        self.cells = list(self.start_patern)
        # The boundary conditions for the firs/last cell of the array.
        self.boundary_con = boundary_con

    

    

        

