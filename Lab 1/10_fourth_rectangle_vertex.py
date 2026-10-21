x1, y1 = map(int, input("Enter first coordinate: ").split(","))
x2, y2 = map(int, input("Enter second coordinate: ").split(","))
x3, y3 = map(int, input("Enter third coordinate: ").split(","))
x4 = x3 - x2 + x1
y4 = y3 - y2 + y1
print(f"The fourth coordinate is: ({x4}, {y4})")