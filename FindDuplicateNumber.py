"""
Problem from leetcode:

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.
"""

"""
Explanation : we look at the array as a linked list where the value in each index is the next node
    example [3,1,2]  is the linked list 3->2->1->3
    we notice that by the given information a cycle is guranteed by the finite numbers  of nodes that each have a out degree of 1
        and the entrance to the cycle is the number which appear twice ( once from entering the cycle and the other is the last in the cycle)
    
    we define 2 pointers one "slow" that do 1 step each time and one "fast" that do 2 steps we run them both like this
    when they meet we put slow back at the head [0] an easy mathematic proof show that the fast and slow both are the same distance from the entrance to the cycle
    so now we let the slow and fast move in the same step until they meet which will be entrance to the cycle
    
    Notes: 
    (1) this is a usage of Floyd’s Cycle Finding Algorithm
    (2) we can use the first part where the slow and fast moving at diffrent speeds to detect if theres a cylce if they meet before one of them reach the end
    

"""
def findDuplicate(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 2:
        return nums[0]
    slow = nums[0]
    fast = nums[slow]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
