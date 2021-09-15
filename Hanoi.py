import tkinter as tk
import time
clrs = ["#20B2AA", "#008080", "#008000", "#00FF00", "#ADFF2F", "#FFFF00", "#FF8C00", "#FF4500","#FF0000"]
class Visualisation_hanoi:
    def __init__(self, hanoi, n):
        self.n = n
        self.hanoi = hanoi
        self.visu=tk.Tk()
        self.visu.title("Les tours de Hanoï")
        self.visu.geometry("800x600")
        self.monCanvas = tk.Canvas(self.visu, width=800, height=600, bg='#A9A9A9')
        self.monCanvas.pack()
        self.monCanvas.create_rectangle(130,500,140,100,fill="black")
        self.monCanvas.create_rectangle(400,500,410,100,fill="black")
        self.monCanvas.create_rectangle(660,500,670,100,fill="black")
        self.monCanvas.create_rectangle(15,500,255,520,fill="black")
        self.monCanvas.create_rectangle(285,500,525,520,fill="black")
        self.monCanvas.create_rectangle(545,500,785,520,fill="black")
        for i in range(len(hanoi)):
            centre=[135,405,665]
            for j in range(len(hanoi[i])):
                self.monCanvas.create_rectangle(centre[i]-10-10*hanoi[i][j],498-20*j,centre[i]+10+10*hanoi[i][j],502-20*j-20,fill=clrs[i])
        self.visu.update()

    def mise_a_jour(self):
        time.sleep(0.1)
        self.monCanvas.delete("all")
        self.monCanvas.create_rectangle(130,500,140,100,fill="black")
        self.monCanvas.create_rectangle(400,500,410,100,fill="black")
        self.monCanvas.create_rectangle(660,500,670,100,fill="black")
        self.monCanvas.create_rectangle(15,500,255,520,fill="black")
        self.monCanvas.create_rectangle(285,500,525,520,fill="black")
        self.monCanvas.create_rectangle(545,500,785,520,fill="black")
        for i in range(len(self.hanoi)):
            centre=[135,405,665]
            for j in range(len(self.hanoi[i])):
                self.monCanvas.create_rectangle(centre[i]-10-10*self.hanoi[i][j],498-20*j,centre[i]+10+10*self.hanoi[i][j],502-20*j-20,fill=clrs[self.hanoi[i][j]-1])
        self.visu.update()

    def create(self):
        for i in range(self.n):
            self.hanoi[0].append(abs(i-self.n))
        print(self.hanoi)

    def move(self, a, b):
        self.mise_a_jour()
        x = self.hanoi[a][len(self.hanoi[a])-1]
        self.hanoi[a].remove (x)
        self.hanoi[b].append (x)
        print(self.hanoi)
        self.mise_a_jour()

    def algo(self, n, a, c, b):
        if n == 1:
            self.move(a, c)
            self.mise_a_jour()
            return
        self.algo(int(n-1), a, b, c)
        self.move(a, c)
        self.algo(n-1, b, c, a)



h = [[],[],[]]
v = Visualisation_hanoi(h, 9)
v.create()
v.algo(v.n, 0, 2, 1)
v.mise_a_jour()
