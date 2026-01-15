# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if not root:
        #     return
        # if root.val == val:
        #     return root
        # elif val < root.val:
        #     return self.searchBST(root.left, val)
        # else:
        #     return self.searchBST(root.right, val)

        def dfs(root, target):
            if not root:
                return None
            if target == root.val:
                return root
            elif target < root.val:
                return dfs(root.left, target)
            else:
                return dfs(root.right, target)
        return dfs(root, val)

        