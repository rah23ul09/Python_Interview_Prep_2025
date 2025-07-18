str = "Hey Rahul, How are you buddy?"
count = 0
isWord = False

for ch in str:
    if ch not in(' ', '\t', '\n'):
        if not isWord:
            count += 1
            isWord = True
    else:
        isWord = False

print(f"Word count is : {count}")