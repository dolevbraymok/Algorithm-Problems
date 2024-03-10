"""
Problem #4 in Project Euler , also appears in leetcode for n-digit as hard
    A palindromic number reads the same both ways.
    Find the largest palindrome made from the product of two 3-digit numbers.


    defined in leetcode as :
        Given an integer n, return the largest palindromic integer that can be represented as the product of two n-digits integers.
         Since the answer can be very large, return it modulo 1337

"""




"""
Explanation:
    as a product of 2 n-digits must be no more than 2n-digits we pass over all possible 2n-digits palindrom from largest
        to smallest and check if there are 2 n-digits whose product is the palindrom  and return the first found which its the largest
    
    in the first 'for' loop we create a possible palindrom
    in the second 'for' loop we check if its a product of 2 n-digits we bound by root of the palindrom to avoid double checking
    Note: return -1 at the end unneeded as theres such a palindrom for sure.

"""
import math

def LargestPalindromProduct(n:int)->int:
    if n==1:
        return 9

    large = 10**n -1
    small = 10**(n-1)


    for i in range(large, small-1,-1):
        tmpString = str(i)
        pali = int(tmpString + tmpString[::-1])
        for j in range(large, int(math.sqrt(pali))-1, -1):
            secondNum = pali//j
            if pali % j == 0 and small <= secondNum and secondNum<= large:
                return pali
    return -1

print(LargestPalindromProduct(2))
