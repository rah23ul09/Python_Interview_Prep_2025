number1 = float(input("Enter number 1 : "))
number2 = float(input("Enter number 2 : "))
number3 = float(input("Enter number 3 : "))

if (number1 > number2) and (number1 > number3):
    print(f"number {number1} is greater")
elif number2 > number3:
    print(f"number {number2} is greater")
else:
    print(f"number {number3} is greater")