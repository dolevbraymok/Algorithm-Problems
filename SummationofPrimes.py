"""
Problem #10 from Project euler

Find the sum of all the primes below two million.
"""

"""
Explanation: I provide to solutions, one Simple one Efficent
    simple one/:
            we simply find all numbers below 2 milion and sum them.
                we check if a number is a prime if its not evely divides by any prime before him.
                As always the function will work for any number n and the solution will come from n=2 milion
    Efficent:
        we create a boolean array all true, each index represents a number,
        when we get to a number , if its true we add it to our sum, and then change all his multipications to false
        that way if we get to an index which its array value is true it means every number before doesnt divides it, 
        which means the number is a prime.
"""


def dividesByAll(nums:list, m)->bool:
    """
    helper function ill use to check if a number is a prime
    :param nums: a list of ints in my usage it will be list of found primes
    :param m: suspect as  a prime
    :return:
    """
    for n in nums:
        if m%n==0: return False
    return True

def summationofPrimesSimple(n:int)->int:
    if n==1:
        return 2
    if n==2:
        return 5
    primes=[2,3]
    sum =5
    for num in range(6,n,6):
        print(num)
        if dividesByAll(primes, num-1):
            primes.append(num-1)
            sum+=num-1
        if dividesByAll(primes, num+1):
            primes.append(num+1)
            sum+=num+1
    return sum


def summationofPrimesEfficent(n:int)->int:
    if n==1:return 2
    primes =[True]*n
    primesSum = 2
    for k in range(3,n):
        if primes[k]:
            primesSum+=k
            for i in range(2*k,n,k):
                primes[i]=False
    return primesSum

print(summationofPrimesEfficent(2000000))
"""142913828922"""

