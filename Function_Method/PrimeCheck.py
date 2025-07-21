import math

#using function
def isPrime(prime):
    if prime <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(prime)) + 1):
            if prime % i == 0:
                return False
        return True


print("Number is prime" if isPrime(31) else "Number is not prime")


# Using class
class PrimeCheck:
    @staticmethod
    def isPrime(prime):
        if prime <= 1:
            return False
        else:
            for i in range(2, int(math.sqrt(prime)) + 1):
                if prime % i == 0:
                    return False
            return True


print("Number is prime" if isPrime(34) else "Number is not prime")
