# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res=[]
        self.itr=0
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.res.append(node.val)
            dfs(node.right)
        dfs(root)

    def next(self) -> int:
        val=self.res[self.itr]
        self.itr+=1
        return val

    def hasNext(self) -> bool:
        return self.itr < len(self.res)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()