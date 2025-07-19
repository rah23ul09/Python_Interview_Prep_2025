"""
    1. Using Function
    2. Using Method (Function define in class is consider method)
"""


def factorial(fact):
    result = 1
    for i in range(2, fact + 1):
        result *= i
    return result


print("Factorial is : ", factorial(5))


class Factorial:
    def factorial1(self, fact):
        result = 1
        for i in range(2, fact + 1):
            result *= i
        return result


factorial = Factorial()
print("Factorial is : ", factorial.factorial1(7))
