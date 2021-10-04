###################
#
# Name: Jake Cermak
#
# Program Name: Finding Area and Median of a Trapezoid
#
# Program Description: A simple program that asks for base1, 
# base2, and height to find the area and median of a trapezoid.
# 
#
###################
import math
def prompt():
    print("-----------------------------------------------------")
    print("PYTHON PROGRAM TO FIND AREA AND MEDIAN OF A TRAPEZOID")
    print("-----------------------------------------------------")
    base1 = eval(input("Please Enter the base1: "))
    base2 = eval(input("Please Enter the base2: "))
    height = eval(input("Please Enter the height: "))
    print()
    median = ((base1) + (base2))/2
    print("The Area of a Trapezoid =", area(median, height))
    print("The Median of a Trapezoid =",'%.2f' % (median))
    print("-----------------------------------------------------")

def area(median, height):
    area = (median) * (height)
    return area

if __name__ == '__main__':
    prompt()