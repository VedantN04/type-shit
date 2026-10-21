N = int(input("Enter number of pins: "))
K = int(input("Enter number of balls: "))

pins = ["I"] * N

for i in range(K):
    start = int(input("Enter start pin: "))
    stop = int(input("Enter stop pin: "))

    for j in range(start - 1, stop):
        pins[j] = "."

print("".join(pins))
