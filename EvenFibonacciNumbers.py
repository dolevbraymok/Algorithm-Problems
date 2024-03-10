"""
Problem from project euler

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms
"""

"""
Explanation: we simply move over the fibonacci sequence and add each even number to the sum
we do so by letting fOne be F_i-1 and fTwo be F_i-2  and current = F_i  and we check if F_i is even every time
for this reason every interation we find what is the new number in the following while as F_i=F_i-1+F_i-2
"""


def solution(limit:int)->int:
    fOne = 1
    fTwo=1
    current = fOne+fTwo
    sum=0
    while(current <= limit):
        if current%2==0:
            sum+=current
        fTwo=fOne
        fOne=current
        current=fOne+fTwo
    return sum

print(solution(4000000))