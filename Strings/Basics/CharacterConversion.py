str = "RahUl sInGH"
print(f"Converted string : {str.swapcase()}")

# without using swapcase
result = ""
for ch in str:
    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch

print(f"Converted string : {str.swapcase()}")
