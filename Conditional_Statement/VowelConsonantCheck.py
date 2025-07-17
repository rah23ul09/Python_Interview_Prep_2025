ch = input("Enter character to check : ")

if len(ch) == 1 and ch.isalpha():
    ch = ch.lower()
    if ch in ('a', 'e', 'i', 'o', 'u'):
        print(f"{ch} is vowel.")
    else:
        print(f"{ch} is consonant.")
else:
    print(f"{ch} is not a letter.")