# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.value = True #has we have defined as object attribute no need to pass to functions as parameters
        if not root:
            return True
        self.height(root)
        return True if self.value!= False else False
        
    def height(self, node):
        if not node:
            return 0
        lh = self.height(node.left)
        rh = self.height(node.right)
        if abs(lh - rh) > 1:
            self.value = False
        return 1 + max(lh, rh)