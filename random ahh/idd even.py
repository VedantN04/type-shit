def is_even(number):
    return number % 2 == 0


def check_odd_even(number):
    if is_even(number):
        return f"{number} is even"
    return f"{number} is odd"


def main():
    number = int(input("Enter a number: "))
    print(check_odd_even(number))


main()
