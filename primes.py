"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    num = 2
    count = 1
    list = []
    while count <= number_of_primes:
        prime = True
        for i in range(2, num):
            if (num % i) == 0:
                prime = False
                break
        if prime:
            list.append(num)
            count += 1
        num += 1

    return list
