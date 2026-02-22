# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       
        # def inorder(node):
        #     return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        
        # return inorder(root)[k-1]

        res =[]
        # If we do inorder traversal on binary search tree we will get a sorted list in the end as in inorder we will have left most first and that will be the smallest in BST
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res[k-1]