str = "I love what love me"
result = ""

for ch in str:
    if ch not in result:
        result += ch

print("After removing duplicate : ", result)
