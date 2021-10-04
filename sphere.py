###################
#
# Name: Jake Cermak
#
# Program Name: Finding Volume and Surface Area of a Sphere
#
# Program Description: A simple program that asks for the radius to
# find the surface area and volume of a sphere.
#
###################
import math
def main():
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME AND SURFACE AREA OF A SPHERE")
    print("----------------------------------------------------------")
    radius = eval(input("Please Enter the Radius: "))
    surfarea = 4 * (math.pi) * (radius)**2
    volume = (4/3) * (math.pi) * (radius)**3
    print("The Surface Area of a Sphere =",round(surfarea,2))
    print("The Volume of a Sphere =",round(volume,2))
    print("----------------------------------------------------------")

main()