numbers = []

num = int(input("Enter a number (0 to stop): "))
while num != 0:
    numbers.append(num)
    num = int(input("Enter a number (0 to stop): "))

longest = 0
count = 1

for i in range(1, len(numbers)):
    if numbers[i] == numbers[i - 1]:
        count = count + 1
    else:
        count = 1

    if count > longest:
        longest = count

print("Widest fragment length:", longest)
