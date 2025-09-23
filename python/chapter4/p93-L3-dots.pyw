# Put some dots in a window

import graphics

win = graphics.GraphWin()

p = graphics.Point(50, 60)
p.draw(win)

p2 = graphics.Point(140, 100)
p2.draw(win)

print("Click window to close")
win.getMouse()

win.close()