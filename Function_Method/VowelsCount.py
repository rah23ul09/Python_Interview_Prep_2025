# Using function
def vowelsCount(str):
    vowel = 0
    lowerStr = str.lower()

    for ch in lowerStr:
        if ch.isalpha():
            if ch in "aeiou":
                vowel += 1
    return vowel


print(f"Number of vowels are : {vowelsCount("I am Rahul")}")


# Using class
class VowelCount:
    @staticmethod
    def vowelCount(self, str):
        vowel = 0
        lowerStr = str.lower()
        for ch in lowerStr:
            if ch.isalpha():
                if ch in "aeiou":
                    vowel += 1
        return vowel


print(f"Number of vowels are : {vowelsCount("I am Rahul Singh")}")

