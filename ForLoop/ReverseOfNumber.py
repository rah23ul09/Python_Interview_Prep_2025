number = int(input("Enter the number : "))
original = number
reversed = 0

while number != 0:
    digit = number % 10                 # remove the modulus
    reversed = reversed * 10 + digit    # add modulus into reversed
    number //= 10                       # remove the last digit

print(f"Reverse of entered number is {reversed}")

if original == reversed:
    print("Number is palindrome")
else:
    print("Number is not palindrome")