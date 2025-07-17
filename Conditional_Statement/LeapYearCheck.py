year = int(input("Enter year to check : "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"Year {year} is leap year")
else:
    print(f"Year {year} is not a leap year")