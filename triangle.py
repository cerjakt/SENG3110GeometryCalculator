###################
#
# Name: Jake Cermak
#
# Program Name: Finding Perimeter and Area of Triangle
#
# Program Description: A simple program that asks for 3 sides
# of a triangle to find the perimeter, semi perimeter, and area
# of a triangle.
#
###################
import math
def prompt():
    print("-------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND PERIMETER AND AREA OF A TRIANGLE")
    print("-------------------------------------------------------")
    side1 = eval(input("Please Enter the First Side of the Triangle: "))
    side2 = eval(input("Please Enter the Second Side of the Triangle: "))
    side3 = eval(input("Please Enter the Third Side of the Triangle: "))
    print()
    perimeter = (side1) + (side2) + (side3)
    semiperimeter = (perimeter/2)
    area = ((side1) * (side2))/2
    print("The Perimeter of a Triangle =",'%.2f' % (perimeter))
    print("The Semi Perimeter of a Triangle =",'%.2f' % (semiperimeter))
    print("The Area of a Triangle =",'%.2f' % (area))
    print("-------------------------------------------------------")

if __name__ == '__main__':
    prompt()