"""
Problem #7 from Project Euler

what is the 100001 Prime Number


"""
"""
Explanation: a number is prime if it doest divide by any number below him excpet one
                for every number we will check if it divide by previous prime numbers if it doesnt its a prime
                2 is the only even prime so we will make jumps of 2 each step
"""

def dividesByAll(nums:list, m)->bool:
    for n in nums:
        if m%n==0: return False
    return True

def nthPrime(n:int)->int:
    if n==1:
        return 2
    primes=[2]
    suspect = 3
    while len(primes) < n:
        if dividesByAll(primes, suspect):
            primes.append(suspect)
        suspect+=2
    return primes[-1]


print(nthPrime(10001))


