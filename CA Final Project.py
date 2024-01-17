#Cellular Automata
#Class for 1 dim CA
#Opmerkingen:
#1. Ik denk dat we cell_amount niet echt nodig hebben, is namelijk de lengte van self.cells.
#2. Regel_30 werkt, ik ga nu verder met Regel_110. Daarbij moet ik alleen ff kijken hoe ik zorg,
# dat die aangeroepen wordt ipv Regel_30.
#3 Als je online bent dan kan je appen als je iets niet snapt ofz of wat anders ofz. gr Ruben.
class OnedimCA:
    def __init__(self, cell_amount, start_pattern, apply_rule, layers_amount):
        self.cell_amount = cell_amount
        self.start_patern = start_pattern
        self.apply_rule = apply_rule
        self.layers_amount = layers_amount
        self.cells = list(self.start_patern)
    #willen we dit de cellprinter maken?
    def cells_print(self):
        return self.cells

    # de nieuwe cell op basis van rule_30
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


    #creërt nieuwe generatie cellen
    def newgeneration(self):
        new_cells = []
        #voegt iedere nieuwe cell op basis van rule_30 toe aan de lijst van nieuwe cellen
        for i in range(1, self.cell_amount+1):
            new_cell = self.cells[i-2] + self.cells[i-1] + self.cells[i%self.cell_amount]
            new_cells.extend(self.rule_30(new_cell))

        #zorgt er voor dat de nieuwe cellen op de juiste manier geprint worden, kunnen we later
        # nog aanpassen naar return als dat nodig is.
        # Ook wordt self.cells geasigned aan de niewe cellen zodat die daarna de goede nieuwe
        # generatie kan bepalen.
        self.cells = new_cells
        delimiter = ' '
        cells_configuration = delimiter.join(new_cells)
        print(cells_configuration) #return
    
    #Zorgt ervoor dat de nieuwe generatie x aantal keer geprint wordt.
    def layers(self):
        # Alleen startpatter is niet in de goede print form, aan elkaar ipv een spatie er tussen.
        # kunnen we later doen, moet een ez fix zijn.
        print(self.start_patern)
        for i in range(1, self.layers_amount+1):
            self.newgeneration()



p = OnedimCA(9, "000010000", 30, 4)
p.layers()

    

        

