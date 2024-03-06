"""
problem from project euler:
    If we list all the natural numbers below 10 that are multiples of 3 or 5 , we get 3,5,6 and 9.
     The sum of these multiples is 23 .


    Find the sum of all the multiples of  3 or 5 below 1000

     """


"""
    Explanation:
    this explanation will be for 3,5 but the function will be for any 2 numbers in (0,k)
    first we notice that the sum of all numbers between 1 to 1000 that are divisible by X is equal to X multiplied by the sum of all numbers from
    1 to the number 1000/X
    so it means that the sum of all numbers divided by 3 is 3(1+2+3.....+333) and by 5 is 5(1+2+....+200)
    but now we notice that some numbers counted twice such as 15  so we need to remove 15(1+2+....+[1000/15]) from there sum
"""

import math
def solution(n:int, m:int, k:int):
    k=k-1
    nNumbers = math.floor(k/n)
    mNumbers = math.floor(k/m)
    mnNumbers = math.floor(k/(m*n))


    nSum = n * (nNumbers*(nNumbers+1)/2)
    mSum = m * (mNumbers * (mNumbers + 1) / 2)
    mnSum = (m*n)* (mnNumbers * (mnNumbers + 1) / 2)


    return nSum+mSum-mnSum

print(solution(3,5,1000))
""" Answer is 233168.0"""