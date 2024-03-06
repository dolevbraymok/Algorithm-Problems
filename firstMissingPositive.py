"""
following problem from leetcode
Problem:Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
    Example :
    Input: nums = [3,4,-1,1]
    Output: 2
    Explanation: 1 is in the array but 2 is missing.
"""
"""

Explanation:we go over the list and we check the range [1,array length]
    for each number val found in this range we put it in the switch it with nums[val]
    after going over all the numbers we have that every exisiting number in the range of length is in its index
    if we have a value higher than the length it means we have a missing number in [1,array length]
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        counter=0
        while counter < n:
            val=nums[counter]
            if val > 0 and val <= n:
                index = val-1
                if val != nums[index]:
                    tmp = nums[index]
                    nums[index]=nums[counter]
                    nums[counter]=tmp
                    counter -=1
            counter+=1
        for i in range(n):
            if(i+1 != nums[i]):return i+1
        return n+1

