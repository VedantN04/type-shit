def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:  
        print("Odd")

def is_even(n):
        return n % 2 == 0


main()



# Algorithm: Check whether a number is odd or even

# Start
# Read a number x from the user
# Divide x by 2 and find the remainder (x % 2)
# If the remainder is 0, print "Even"
# Else, print "Odd"
# Stop