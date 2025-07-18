import math

number = int(input("Enter the number : "))
isPrime = True

if number <= 1:
    isPrime = False
else:
    for i in range(2, int(math.sqrt(number)) +1):
        if number % i == 0:
            isPrime = False
            break

if isPrime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
