# Convert an image into grayscale

from graphics import *
import random

def main():
    path = input("Enter the file path to an image: ")

    img = Image(Point(0, 0), path)
    width = img.getWidth()
    height = img.getHeight()
    img.move(width // 2, height // 2)

    win = GraphWin("Grayscaler", width, height)

    img.draw(win)

    win.getMouse()

    # Grayscale
    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            r, g, b = img.getPixel(x, y)
            brightness = int(round(0.299*r + 0.587*g + 0.114*b))
            img.setPixel(x, y, color_rgb(brightness, brightness, brightness))
        update()

    # # Evaporate
    # while True:
    #     for i in range(10000):
    #         r, g, b = img.getPixel(random.randint(0, width - 1), random.randint(0, height - 1))
    #         img.setPixel(random.randint(0, width - 1), random.randint(0, height - 1), color_rgb(r, g, b))
    #     update()

    # # Snap away
    # while True:
    #     x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
    #     dx, dy = random.randint(-5, 5), random.randint(-5, 5)
    #     x2, y2 = (x1 + dx) % width, (y1 + dy) % height
    #     col1 = img.getPixel(x1, y1)
    #     col2 = img.getPixel(x2, y2)
    #     img.setPixel(x2, y2, color_rgb(col1[0], col1[1], col1[2]))
    #     img.setPixel(x1, y1, color_rgb(col2[0], col2[1], col2[2]))
    #     update()

    
    win.getMouse() 

if __name__ == "__main__":
    main()