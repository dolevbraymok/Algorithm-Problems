"""
Problem from leetcode:
    Given the head of a singly linked list, return the middle node of the linked list.
        If there are two middle nodes, return the second middle node.
"""

"""
Explanation: we define two walkers one slow take 1 step each time and the other fast takes two step each time
            when the fast reach the end than the slow is exacly in the middle as
                the ratio between their step is exactly 1:2


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None:
            return head
        snail=head
        hare=head
        while hare != None and hare.next !=None:
            snail=snail.next
            hare=hare.next.next
        return snail