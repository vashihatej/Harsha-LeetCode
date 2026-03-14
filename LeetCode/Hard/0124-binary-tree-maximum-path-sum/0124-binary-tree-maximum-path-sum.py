# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # res = [root.val]
        # def dfs(root):
        #     if not root:
        #         return 0
            
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     left = max(left, 0)
        #     right = max(right, 0)

        #     res[0] = max(res[0], root.val + left + right)

        #     return root.val + max(left, right)

        # dfs(root)
        # return res[0]


        res=[root.val]
        def dfs(node):
            if not node:
                return 0
            left=max(0,dfs(node.left))
            right=max(0,dfs(node.right))
            res[0]=max(res[0],left+node.val+right)
            return node.val+max(left, right)
        dfs(root)
        return res[0]