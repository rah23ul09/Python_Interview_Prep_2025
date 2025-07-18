number = int(input("Enter the number : "))
count = 0
temp = abs(number)

if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10
print(f"Count of number {number} is {count}")