H = int(input("Enter hour hand position (0-12): "))
M = int(input("Enter min hand position (0-59): "))
S = int(input("Enter sec hand position (0-59): "))

angle = (H * 30 + M * 0.5 + S * (1/120))
print("Angle of hour hand from 12 o'clock position is:", angle, "degrees")