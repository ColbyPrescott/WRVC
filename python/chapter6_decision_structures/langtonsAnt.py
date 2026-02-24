# Try writing a program myself

from graphics import *
import math

cellSize = 8
cellsX = 80
cellsY = 80
cells = []
for i in range(cellsX):
    cells.append([])
    for j in range(cellsY):
        cells[i].append(True)

antX = math.floor(cellsX / 2)
antY = math.floor(cellsY / 2)
antRot = 2 # right up left down

win = None
cellRects = []

def initCellRects():
    for i in range(cellsX):
        cellRects.append([])
        for j in range(cellsY):
            rect = Rectangle(Point(i, j), Point(i + 1, j + 1))
            rect.setFill("white")
            rect.draw(win)
            cellRects[i].append(rect)

def redrawCell(cellX, cellY):
    cell = cells[cellX][cellY]
    rect = cellRects[cellX][cellY]
    rect.setFill("white" if cell else "black")

def rotate(n):
    global antRot
    antRot += n
    
    if antRot < 0:
        antRot = 3
    elif antRot >= 4:
        antRot = 0

def move(x, y):
    global antX, antY
    antX += x
    antY += y
    
    if antX < 0:
        antX = cellsX - 1
    elif antX >= cellsX:
        antX = 0
    if antY < 0:
        antY = cellsY - 1
    elif antY >= cellsY:
        antY = 0

def moveForward():
    if antRot == 0:
        move(1, 0)
    elif antRot == 1:
        move(0, 1)
    elif antRot == 2:
        move(-1, 0)
    elif antRot == 3:
        move(0, -1)

def tick():
    global cells
    cell = cells[antX][antY]
    
    if cell:
        rotate(-1)
    else:
        rotate(1)
    
    cells[antX][antY] = not cell
    redrawCell(antX, antY)
    
    moveForward()

def main():
    global win
    win = GraphWin("Langton's Ant", cellsX * cellSize, cellsY * cellSize)
    win.setCoords(0, 0, cellsX, cellsY)
    initCellRects()
    
    while True:
        tick()

main()