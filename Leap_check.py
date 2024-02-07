print("Welcome to Leap year checker!!!!")
print()

year = int (input("Enter the year to verify if it is a Leap year or not: \n"))
print()

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a Leap year!!")
        else:
            print(f"The year {year} is not a leap year!!")
    else:
        print(f"The year {year} is Leap year!!")
else:
    print(f"The year {year} is not a leap year!!")
