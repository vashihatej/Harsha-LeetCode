# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head):
        # Step 1: Convert linked list to array for easy middle access
        values = []
        while head:
            values.append(head.val)
            head = head.next

        # Step 2: Recursively build BST from sorted array
        def build(left, right):
            # Base case: no elements in this range
            if left > right:
                return None

            # Pick the middle element as root
            mid = (left + right) // 2
            node = TreeNode(values[mid])

            # Everything to the left of mid → left subtree
            node.left = build(left, mid - 1)

            # Everything to the right of mid → right subtree
            node.right = build(mid + 1, right)

            return node

        return build(0, len(values) - 1)

