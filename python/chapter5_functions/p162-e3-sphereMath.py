import math

def sphereArea(radius):
    return 4 * math.pi * radius ** 2

def sphereVolume(radius):
    return (4 / 3) * math.pi * radius ** 3

def main():
    radius = float(input("Enter sphere radius: "))
    
    print("Volume:", sphereVolume(radius))
    print("Area:", sphereArea(radius))

main()