from SuperClass_CA_Project import CA
import numpy as np

import matplotlib.pyplot as plt

import matplotlib.animation as animation
class TwodimCA(CA):
    def __init__(self, start_pattern, apply_rule, layers_amount, boundary_con, row, colom):
        super().__init__(start_pattern, apply_rule, layers_amount, boundary_con)
        self.row = row
        self.colom = colom
        

        self.fig, self.ax = plt.subplots()
        plt.axis("off")
        self.im = self.ax.imshow(self.start_patern, cmap='magma', interpolation='nearest')

        self.ani = animation.FuncAnimation(self.fig, self.update, frames=100, interval=50, save_count=50, blit=True)

        

    def new(self,bord):
        lijst = []
        for q in range(1, self.row+1):
            lijst.append([])
            for w in range(1, self.colom+1):
                lijst[q-1].append(bord[q-1][w-1])
        self.cells =  lijst



    def update(self,frame):
        self.new(self.start_patern) 
        nieuw_bord = self.cells
        for i in range(1,self.row+1):
            for j in range(1, self.colom+1):
                if self.start_patern[i-1][j-1] == 1:
                    som = (self.start_patern[i-2][j-2] + self.start_patern[i-2][j-1] + self.start_patern[i-2][j%self.colom] +
                    self.start_patern[i-1][j-2] + self.start_patern[i-1][j%self.colom] +
                    self.start_patern[i%self.row][j-2] + self.start_patern[i%self.row][j-1] + self.start_patern[i%self.row][j%self.colom])
                    if som < 2 or som > 3:
                        nieuw_bord[i-1][j-1] = 0
                else:
                    som = (self.start_patern[i-2][j-2] + self.start_patern[i-2][j-1] + self.start_patern[i-2][j%self.colom] +
                    self.start_patern[i-1][j-2] + self.start_patern[i-1][j%self.colom] +
                    self.start_patern[i%self.row][j-2] + self.start_patern[i%self.row][j-1] + self.start_patern[i%self.row][j%self.colom])
                    if som == 3:
                        nieuw_bord[i-1][j-1] = 1
        self.start_patern = nieuw_bord
        self.im.set_data(self.start_patern)

        return self.im,
        #print("...",nieuw_bord,"...")


       
   

    

    

k = TwodimCA([[0,0,1,0,0,0],[1,0,1,0,0,0],[0,1,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]], "Game of life", 25, "periodic", 5, 6) 
plt.show()



    

    

        

