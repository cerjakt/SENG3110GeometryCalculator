###################
#
# Name: Jake Cermak
#
# Program Name: Finding Volume and Surface Area of a Cuboid
#
# Program Description: A simple program that asks for the length, 
# width, and height to find the surface area, volume, and lateral
# surface area of a cuboid.
#
###################
import math
def prompt():
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME AND SURFACE AREA OF A CUBOID")
    print("----------------------------------------------------------")
    length = eval(input("Please Enter the Length: "))
    width = eval(input("Please Enter the Width: "))
    height = eval(input("Please Enter the Height: "))
    print()
    surfarea = (2 * (length * height)) + (2 * (width * height)) + (2 * (length * width))
    volume = (length) * (width) * (height)
    latsurfarea = 2 * (length + width) * (height)
    print("The Surface Area of a Cuboid =",'%.2f' % (surfarea))
    print("The Volume of a Cuboid =",'%.2f' % (volume))
    print("The Lateral Surface Area of a Cuboid =",'%.2f' % (latsurfarea))
    print("----------------------------------------------------------")

if __name__ == '__main__':
    prompt()