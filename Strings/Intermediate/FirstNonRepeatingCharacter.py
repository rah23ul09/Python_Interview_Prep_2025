str = "aabbsdncec"

for ch in str:
    if str.index(ch) == str.rindex(ch):
        print("First non-repeating character in string is : ", ch)
        break
else:
        print("No non repeating character is found")