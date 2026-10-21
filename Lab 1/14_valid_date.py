# 14. Program to check if a date is valid.

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

valid = False

if year > 0 and 1 <= month <= 12:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:  # February
        if is_leap:
            max_day = 29
        else:
            max_day = 28

    if 1 <= day <= max_day:
        valid = True

if valid:
    print(f"{day}/{month}/{year} is a valid date.")
else:
    print(f"{day}/{month}/{year} is an invalid date.")
