message = "Hello, Rahul"
vowel = consonant = 0
message = message.lower()

for ch in message:
    if ch.isalpha():
        if ch in "aeiou":
            vowel += 1
        else:
            consonant += 1

print(f"Number of vowels in string are : {vowel}")
print(f"Number of consonants in string are : {consonant}")