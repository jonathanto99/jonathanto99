from math import pi

# core requirements & stretch 1
print()
square_area = float(input("What is the length of a side of the square? "))
print(f"The area of the square is: {square_area ** 2}")

print()
rectangle_length = float(input("What is the length of rectangle? "))
rectangle_width = float(input("What is the width of the rectangle "))
print(f"The area of the rectangle is: {rectangle_length * rectangle_width}")

print()
circle_radius = float(input("What is the radius of the circle? "))
print(f"The area of the circle is : {round(pi * circle_radius ** 2, 2)}")
print()

# stretch 2
fancy = float(input("What is your super important length? "))
print(f"Area of a square: {fancy ** 2}")
print(f"Area of a circle: {round(pi * fancy ** 2, 2)}")
print(f"Volume of a cube: {fancy ** 3}")
print(f"Volume of a sphere: {4 / 3 * pi * fancy ** 3}")
