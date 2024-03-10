"""
Problem #5 from Project Euler
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

    we will Solve for all numbers from 1 to n
"""


"""
Explanation: we find the Least Common multiply of all number as its the answer
        Note that for the problem  from 1 to 20 we dont need code as the answer is:
        2520 * 2 *11*13*17*19 where 2520 is given as the smallest number evenly divisible by all of the numbers from 1 to 10

"""
def findLCM(a:int, b:int)->int:
    large = max(a, b)
    small = min(a, b)
    for i in range(large, a*b+1, large):
        if i % small == 0:
            return i


def SmallestMultiple(n:int)->int:
    if n<2 :return 1
    number=2
    for i in range(2,n+1):
        number=findLCM(number,i)
    return number


print(SmallestMultiple(20))
