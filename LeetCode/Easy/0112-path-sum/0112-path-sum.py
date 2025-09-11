# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # def dfs(node, cursum):
        #     if not node:
        #         return False
        #     cursum += node.val
        #     if not node.left and not node.right:
        #         return cursum == targetSum
            
        #     return(dfs(node.left, cursum) or
        #     dfs(node.right, cursum))
        # return dfs(root, 0)

        def dfs(node, sum):
            if not node:
                return False
            sum_t = sum + node.val
            if not node.right and not node.left:
                if sum_t == targetSum:
                    return True
            if dfs(node.right, sum_t):
                return True
            if dfs(node.left, sum_t):
                return True
            return False
        return dfs(root, 0)
