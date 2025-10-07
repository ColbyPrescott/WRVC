# Modify p105-L5_3-futval_graph.py to use Entry objects for principal and APR input

from graphics import *

def main():
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    
    win.setCoords(0, 0, 1, 1)
    introText = Text(Point(0.5, 0.9), "This program plots the growth\nof a 10-year investment.")
    introText.draw(win)
    
    # Get principal and interest rate from user
    principalLabel = Text(Point(0.4, 0.6), "Initial principal:")
    principalLabel.draw(win)
    principalEntry = Entry(Point(0.8, 0.6), 5)
    principalEntry.draw(win)
    
    aprLabel = Text(Point(0.4, 0.4), "Annualized interest rate:")
    aprLabel.draw(win)
    aprEntry = Entry(Point(0.8, 0.4), 5)
    aprEntry.draw(win)
    
    statusMessage = Text(Point(0.5, 0.1), "Click anywhere to graph")
    statusMessage.draw(win)
    win.getMouse()
    
    principal = float(principalEntry.getText())
    apr = float(aprEntry.getText())
    
    introText.undraw()
    principalLabel.undraw()
    principalEntry.undraw()
    aprLabel.undraw()
    aprEntry.undraw()
    statusMessage.undraw()
    
    # Create graphics window with labels on the left side
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), " 0.0K").draw(win)
    Text(Point(-1, 2500), " 2.5K").draw(win)
    Text(Point(-1, 5000), " 5.0K").draw(win)
    Text(Point(-1, 7500), " 7.5K").draw(win)
    Text(Point(-1, 10000), "10.0K").draw(win)
    
    # Draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    
    # Draw a bar for each subsequent year
    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    
    win.getMouse()
    win.close()

main()