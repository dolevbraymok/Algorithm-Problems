"""
Problem #6 from Project Euler


Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""
"""
Explanation: the diffrence in between the two is the sum of all mulitpication between 2 diffrent numbers
    The following solution will find the diffrence between a collection of numbers presented as a List
    
    Note that there a closed formula for only naturals but as the function is for every collection of numbers i wont use it
"""



def sumSquareDiffrence(nums:list)->float:
    sum=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sum+= nums[i]*nums[j]
    return sum*2


print(sumSquareDiffrence(list(range(101))))