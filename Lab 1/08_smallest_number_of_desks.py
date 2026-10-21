import math

class1 = int(input("Enter the number of students in class 1: "))
class2 = int(input("Enter the number of students in class 2: "))
class3 = int(input("Enter the number of students in class 3: "))

result = math.ceil(class1 / 2) + math.ceil(class2 / 2) + math.ceil(class3 / 2)
print("Total Desks needed are:", result)