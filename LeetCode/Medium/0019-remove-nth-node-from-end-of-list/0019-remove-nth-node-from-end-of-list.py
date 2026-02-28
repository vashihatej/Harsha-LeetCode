# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #create one dummy node and add it to start of the list
        dummy = ListNode(0, head)
        left = dummy
        right = head
        #to maintain the difference b/t left and right with n distances so that when we are traversing 
        #in the list and stop at the end we need a node that nth node from the end so
        while n > 0 and right:
            right=right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        #deleting that nth node
        left.next = left.next.next
        return dummy.next