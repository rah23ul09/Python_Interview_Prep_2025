row = 5
numbers = 1

for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(numbers, end=" ")
        numbers += 1
    print()