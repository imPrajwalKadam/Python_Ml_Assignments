"""
Write a program which accept radius  of circle and area of circle .

"""
import math

def calculateArea(radius):
    """Calculates the area of a circle given its radius."""
    return math.pi * (radius ** 2)

def main():
        radius = float(input("Enter the radius of the circle: "))
        
        if radius < 0:
            print("Radius cannot be negative.")
            return
            
        area = calculateArea(radius)
        print(f"The area of the circle with radius {radius} is: {area:.2f}")
        

if __name__ == "__main__":
    main()
