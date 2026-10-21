N = int(input("Enter number of cards: "))
card_list = list(range(1, N + 1))

R = int(input("Enter the missing card: "))
card_list.remove(R)

print(f"The missing card is {R}")
summation = sum(card_list)
print(f"The sum of the remaining cards is {summation}")

'''
1) Get input from user for number of cards (N)
2) Create a list of cards from 1 to N
3) Get input from user for the missing card (R) and remove it from the list
4) Print the missing card (R)
5) Calculate the sum of the remaining cards and print the result
'''