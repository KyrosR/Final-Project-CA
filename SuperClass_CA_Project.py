

""""""""" 
This is the superclass of the CA's.
It contains variables that both CA's need, although the use of them could be a little different.
Access to this super class is granted by importing it.
"""""""""

class CA:
    # The __init__ function contains all variabels for both CA"s.

    def __init__(self, start_pattern, apply_rule, layers_amount, boundary_con):
        # The pattern of one's and zero's the 1 dimensional array
        self.start_patern = start_pattern
        # The rule that is applied to a given array
        self.apply_rule = apply_rule  
        # The amount of array's(layers) of nextgeneration cells.
        self.layers_amount = layers_amount 
        # Putting the start_pattern in a list
        self.cells = list(self.start_patern)
        # The boundary conditions for the firs/last cell of the array.
        self.boundary_con = boundary_con