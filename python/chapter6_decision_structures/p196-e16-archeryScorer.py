# Write a program that draws an archery target and allows the user to click five points to represent arrow shots.
# Display the score for each click and keep track of a running sum for the entire series.
# Use five-band scoring, where a bulls-eye (yellow) is worth 9 points and each successive ring is worth 2 fewer points down to 1 for white.

from graphics import *
import math

colors = ["white", "black", "blue", "red", "yellow"]

def drawTarget(win):
    for i in range(len(colors)):
        circle = Circle(Point(0, 0), 10 - (i * 10 / len(colors)))
        circle.setFill(colors[i])
        circle.setWidth(0)
        circle.draw(win)

def getScore(arrowPos):
    distance = math.sqrt(arrowPos.getX() ** 2 + arrowPos.getY() ** 2)
    score = distance * len(colors) // 10 * 2
    score = 9 - score
    score = max(0, score)
    return math.floor(score)

def highlightWhite(win, obj, offset=Point(0.05, 0.03)):
    newObj = obj.clone()
    newObj.move(offset.getX(), offset.getY())
    newObj.setOutline("white")
    newObj.draw(win)

def shootArrow(win):
    arrowPos = win.getMouse()

    arrowSize = 0.5
    arrowLines = [
        Line(Point(arrowPos.getX() - arrowSize, arrowPos.getY() - arrowSize), 
             Point(arrowPos.getX() + arrowSize, arrowPos.getY() + arrowSize)),
        Line(Point(arrowPos.getX() - arrowSize, arrowPos.getY() + arrowSize), 
             Point(arrowPos.getX() + arrowSize, arrowPos.getY() - arrowSize))
    ]
    for arrowLine in arrowLines:
        arrowLine.setWidth(2)
        arrowLine.setOutline("black")
        arrowLine.draw(win)
        highlightWhite(win, arrowLine, Point(0.15, 0))
    
    score = getScore(arrowPos)

    scoreText = Text(Point(arrowPos.getX() + 1, arrowPos.getY() - 1), score)
    scoreText.setOutline("black")
    scoreText.draw(win)
    highlightWhite(win, scoreText)

    return score


def main():
    print("This program simulates a game of archery! Click 5 points to see the score.")

    win = GraphWin("Archery Scorer", 400, 400)
    win.setCoords(-10, -10, 10, 10)
    win.setBackground("#986B41")
    
    drawTarget(win)

    totalScore = 0
    totalScoreText = Text(Point(0, -9), "Score: 0")
    totalScoreText.draw(win)

    for i in range(5):
        totalScore += shootArrow(win)
        totalScoreText.setText("Score: " + str(totalScore))

    totalScoreText.setText("Final score: " + str(totalScore))
    win.getMouse()

if __name__ == "__main__":
    main()