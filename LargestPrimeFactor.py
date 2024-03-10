"""
Problem 3 from Project Euler :
    The prime factors of 13195 are 5,7,13 and 29.
    What is the largest prime factor of the number 600851475143
"""


"""
as each number is a product of prime numbers we can divide the number by smallest prime number each time 
    we notice that unless num is prime that its a product of atleast 2 primes
    we also notice that each iteration if we get to the while we remove divide num by p^k  where k is the number of times
        p is in the unique prime product form of num
    by those 2 facts we can conclude that  when p*p> original we passed the largest prime factor of the original num 
        unless it is a prime itself ( which is the reason for the if after the 'for' loop)
    also as every number is prime or a product of smaller primes  each number that pass the second if in the
        while must be a prime that is also a factor of the original

"""
import math


def solution(num:int)->int:
    prime = 2
    original=num
    for p in range(prime, num + 1):
        if p*p > original:
            break
        if(num%p!=0 and num!=p):
            continue
        prime = p
        while(num%prime==0 and prime!=num):
            num /= prime

    if prime==2 and original%2==1:
        return original
    return prime

print(solution(600851475143))
