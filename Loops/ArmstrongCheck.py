number = int(input("Enter the number : "))
original = number

countDigit = 0
temp = number

while temp != 0:
    countDigit += 1
    temp //= 10

sum = 0
temp = number

while temp != 0:
    digit = temp % 10
    sum += digit ** countDigit
    temp //= 10

if original == sum:
    print("Number is armstrong")
else:
    print("Number is not armstrong")