# 15. Program to find the roots of a quadratic equation.
# Quadratic equation: ax^2 + bx + c = 0

import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("Not a quadratic equation (a cannot be 0).")
else:
    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Roots are real and distinct.")
        print("Root 1 =", root1)
        print("Root 2 =", root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("Roots are real and equal.")
        print("Root =", root)
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-discriminant) / (2 * a)
        print("Roots are complex (imaginary).")
        print(f"Root 1 = {real_part} + {imag_part}i")
        print(f"Root 2 = {real_part} - {imag_part}i")
