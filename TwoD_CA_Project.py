#Cellular Automata
#Class for 1 dim CA


"""""""""
Importing SuperClass_CA_Project for necessary variables.
Importing matplotlib.pylot for the plot functions.
Importing matplotlib.animation for the animation functions.
""""""'"""

from SuperClass_CA_Project import CA
import matplotlib.pyplot as plt
import matplotlib.animation as animation



"""""""""
The class for the two-dimensional CA.
"""""""""

class TwodimCA(CA):
    """""""""
    The __init__ function contains all variabeles for the TwoD CA.
    These variables are in a specific order, which is also the order in which the user types 
    in the values they want for those variables.
    """""""""

    def __init__(self, start_pattern, apply_rule, layers_amount, boundary_con, row, colom):
        # Uses variables written in the superclass
        super().__init__(start_pattern, apply_rule, layers_amount, boundary_con)
        # The amount of rows and coloms.
        self.row = row
        self.colom = colom
        
        # Necessary functions and variables for the plot of the the animation.
        self.fig, self.ax = plt.subplots()
        plt.axis("off")
        self.im = self.ax.imshow(self.start_patern, cmap='magma', interpolation='nearest')
        self.ani = animation.FuncAnimation(self.fig, self.update, frames=100, interval=50, save_count=50, blit=True)

        
    """""""""
    This function makes a copy of the bord and assigns it to self.cells.
    """""""""

    def new(self,bord):
        list = []
        for q in range(1, self.row+1):
            list.append([])
            for w in range(1, self.colom+1):
                list[q-1].append(bord[q-1][w-1])
        self.cells =  list




    """""""""
    This function updates the new_bord and then assigns the new_bord to the original bord (self.startpatern).
    This function uses periodic boundaries.
    """""""""

    def update(self,frame):
        # Makes a copy of the old bord.
        self.new(self.start_patern) 
        nieuw_bord = self.cells

        # Determines the new state of each cell from the old bord by checking all its neighbors.
        # Then it updates each cell in the new_bord.
        for i in range(1,self.row+1):
            for j in range(1, self.colom+1):

                # Checks if the cell is alive, else the cell is dead.
                if self.start_patern[i-1][j-1] == 1:

                    # The sum of all neighbors equals the amount of alive cells.
                    sum = (self.start_patern[i-2][j-2] + self.start_patern[i-2][j-1] + self.start_patern[i-2][j%self.colom] +
                    self.start_patern[i-1][j-2] + self.start_patern[i-1][j%self.colom] +
                    self.start_patern[i%self.row][j-2] + self.start_patern[i%self.row][j-1] + self.start_patern[i%self.row][j%self.colom])
                    
                    # Updates the cell in the new_bord.
                    if sum < 2 or sum > 3:
                        nieuw_bord[i-1][j-1] = 0

                else:
                    # The sum of all neighbors equals the amount of alive cells.
                    sum = (self.start_patern[i-2][j-2] + self.start_patern[i-2][j-1] + self.start_patern[i-2][j%self.colom] +
                    self.start_patern[i-1][j-2] + self.start_patern[i-1][j%self.colom] +
                    self.start_patern[i%self.row][j-2] + self.start_patern[i%self.row][j-1] + self.start_patern[i%self.row][j%self.colom])
                    # Updates the cell in the new_bord.
                    if sum == 3:
                        nieuw_bord[i-1][j-1] = 1

        # The old bord becomes the new_bord.                
        self.start_patern = nieuw_bord
        # Makes an image of the new_bord.
        self.im.set_data(self.start_patern)
        # Returns that image to the animation.
        return self.im,
        


       
   

    

    
# Makes k an instance of the class with the values of the variables that are necessary for the program to run.
# Could be changed to accept inputs for a more interactive style.
k = TwodimCA([[0,0,1,0,0,0],[1,0,1,0,0,0],[0,1,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]], "Game of life", 25, "periodic", 5, 6)
# Shows all the new_bords in the animation. 
plt.show()



    

    

        

