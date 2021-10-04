import cone
import cube
import cuboid
import cylinder
import equilateral_triangle
import sphere
import trapezoid
import triangle

def main():

    while True:
        print("\nGeometry Program")
        print("----------------")
        print("1. Cone")
        print("2. Cube")
        print("3. Cuboid")
        print("4. Cylinder")
        print("5. Equilateral Triangle")
        print("6. Sphere")
        print("7. Trapezoid")
        print("8. Triangle")
        print("0. Quit")
        selection = int(input("\nPlease enter your selection: "))
        if selection == 1:
            cone.prompt()
        elif selection == 2:
            cube.prompt()
        elif selection == 3:
            cuboid.prompt()
        elif selection == 4:
            cylinder.prompt()
        elif selection == 5:
            equilateral_triangle.prompt()
        elif selection == 6:
            sphere.prompt()
        elif selection == 7:
            trapezoid.prompt()
        elif selection == 8:
            triangle.prompt()
        if selection == 0:
            print("\nTerminating Program...\n")
            break
        
if __name__ == '__main__':
    main()