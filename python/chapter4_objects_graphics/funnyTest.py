import random
from graphics import *

root = tk.Tk()
root.withdraw()

class IdiotWin():
    def __init__(self, x = 0, y = 0, width = 200, height = 200, velX = 20, velY = 20):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.velX = velX
        self.velY = velY
        
        self.win = GraphWin("Funny")
        self.updateGeometry()
    
    def updateGeometry(self):
        geo = str(self.width) + "x" + str(self.height) + "+" + str(self.x) + "+" + str(self.y)
        self.win.master.geometry(geo)
    
    def update(self):
        self.x = self.win.master.winfo_x()
        self.y = self.win.master.winfo_y()
        
        self.x += self.velX
        self.y += self.velY
        
        if self.x < 0:
            self.velX *= -1
            self.x = 0
        elif self.x > root.winfo_screenwidth() - self.width:
            self.velX *= -1
            self.x = root.winfo_screenwidth() - self.width
        
        if self.y < 0:
            self.velY *= -1
            self.y = 0
        elif self.y > root.winfo_screenheight() - self.height:
            self.velY *= -1
            self.y = root.winfo_screenheight() - self.height
        
        self.updateGeometry()

def main():
    idiotWins = []
    
    for i in range(3):
        width = 200
        height = 200
        x = random.randint(0, root.winfo_screenwidth() - width)
        y = random.randint(0, root.winfo_screenheight() - height)
        velX = random.randint(20, 40) * (-1 if random.random() < 0.5 else 1)
        velY = random.randint(20, 40) * (-1 if random.random() < 0.5 else 1)
        idiotWins.append(IdiotWin(x, y, width, height, velX, velY))
    
    while True:
        for i in range(len(idiotWins)):
            idiotWins[i].update()
        
        update(30)

main()