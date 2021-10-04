###################
#
# Name: Jake Cermak
#
# Program Name: Finding Area and Perimeter of an Equilateral Triangle
#
# Program Description: A simple program that asks for the length of
# any side of an equilateral triangle to find the area, perimeter, 
# semi perimeter, and altitude.
#
###################
import math
def prompt():
    print("--------------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND AREA AND PERIMETER OF AN EQUILATERAL TRIANGLE")
    print("--------------------------------------------------------------------")
    side = eval(input("Please Enter the Length of any Side of an Equilateral Triangle: "))
    print()
    area = (math.sqrt(3)/4) * ((side)**2)
    perimeter = 3 * (side)
    semiperimeter = perimeter/2
    altitude = (1/2) * math.sqrt(3) * (side)
    print("Area of an Equilateral Triangle =",'%.2f' % (area))
    print("Perimeter of an Equilateral Triangle =",'%.2f' % (perimeter))
    print("Semi Perimeter of an Equilateral Triangle =",'%.2f' % (semiperimeter))
    print("Altitude of an Equilateral Triangle =",'%.2f' % (altitude))
    print("--------------------------------------------------------------------")

if __name__ == '__main__':
    prompt()