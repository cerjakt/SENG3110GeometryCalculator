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
    area = (median) * (height)
    print("The Area of a Trapezoid =",'%.2f' % (area))
    print("The Median of a Trapezoid =",'%.2f' % (median))
    print("-----------------------------------------------------")

if __name__ == '__main__':
    prompt()