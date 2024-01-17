#Cellular Automata
#Class for 1 dim CA
class OnedimCA:
    def __init__(self, cell_amount, start_pattern, apply_rule, layers_amount):
        self.cell_amount = cell_amount
        self.start_patern = start_pattern
        self.apply_rule = apply_rule
        self.layers_amount = layers_amount
        self.cells = []

    def cells(self):
        self.cells = list(self.start_patern)

    # Ben er mee bezig, gr Ruben.
    def rule_30(self):
        print("moet nog")

    def newgeneration(self):
        print("moet nog")

        

