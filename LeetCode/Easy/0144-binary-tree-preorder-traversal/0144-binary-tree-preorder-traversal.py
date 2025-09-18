# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        cur = root
        res=[]
        while cur or stack:
            if cur:
                res.append(cur.val)
                print(cur.val)
                if cur.right:
                    stack.append(cur.right)
                cur=cur.left
            else:
                cur=stack.pop()
        return res