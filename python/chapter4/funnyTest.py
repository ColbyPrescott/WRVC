import time
from graphics import *

class IdiotWin():
    

def main():
    width = 200
    height = 200
    x = 0
    y = 0
    velX = 20
    velY = 20
    
    root = tk.Tk()
    root.withdraw()
    
    win = GraphWin("Sshtooupeed", width, height)
    
    while True:
        x += velX
        y += velY
        
        if x < 0:
            velX *= -1
            x = 0
        elif x > root.winfo_screenwidth() - width:
            velX *= -1
            x = root.winfo_screenwidth() - width
        
        if y < 0:
            velY *= -1
            y = 0
        elif y > root.winfo_screenheight() - height:
            velY *= -1
            y = root.winfo_screenheight() - height
        
        geo = str(width) + "x" + str(height) + "+" + str(x) + "+" + str(y)
        win.master.geometry(geo)
        
        update(30)
    
    win.getMouse()

main()