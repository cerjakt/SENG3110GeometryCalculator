###################
#
# Name: Jake Cermak
#
# Program Name: Finding Volume and Surface Area of a Cube
#
# Program Description: A simple program that asks for the length 
# of a side to find the surface area, volume, and lateral surface
# area of a cube.
#
###################
import math
def prompt():
    print("--------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME AND SURFACE AREA OF A CUBE")
    print("--------------------------------------------------------")
    side = eval(input("Please Enter the Length of any Side of a Cube: "))
    area = (side) * (side)
    print()
    surfarea = 6 * (area)
    latsurfarea = (surfarea) - (area * 2)
    print("Surface Area of a Cube =",'%.2f' % (surfarea))
    print("The Volume of a Cube = ", volume(side, area))
    print("Lateral Surface Area of a Cube =",'%.2f' % (latsurfarea))
    print("--------------------------------------------------------")

def volume(side, area):
    volume = (area) * (side)
    return volume

if __name__ == '__main__':
    prompt()