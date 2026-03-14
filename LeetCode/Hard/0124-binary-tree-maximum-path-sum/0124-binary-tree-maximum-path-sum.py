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
        res = [root.val]
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(left, 0)
            right = max(right, 0)

            res[0] = max(res[0], root.val + left + right)

            return root.val + max(left, right)

        dfs(root)
        return res[0]


class Solution:
    def maxPathSum(self, root):
        """
        PROBLEM
        -------
        Given a binary tree, find the maximum possible sum of any path.

        A path:
        - Can start and end at ANY nodes
        - Must follow parent-child connections
        - Cannot reuse nodes
        - Does NOT have to pass through the root

        Example Tree
        ------------

                -10
                /  \
               9   20
                  /  \
                 15   7

        Possible paths:
            9
            15
            7
            20 → 15
            20 → 7
            15 → 20 → 7   ← best

        Maximum Path Sum = 15 + 20 + 7 = 42


        CORE IDEA
        ---------

        At each node, there are TWO things we care about:

        1️⃣ The best path that can extend upward to the parent
        2️⃣ The best path that passes THROUGH the current node

        ------------------------------------------------------------

        Case 1: Path that continues upward
        ----------------------------------

        When returning to the parent, we can only choose ONE side
        (left OR right), because paths cannot split upward.

                node
               /
            left

        OR

                node
                   \
                   right

        So we return:

            node.val + max(left, right)

        ------------------------------------------------------------

        Case 2: Path passing THROUGH the node
        -------------------------------------

        Here the path can include BOTH sides.

               left
                |
               node
                |
               right

        Path sum:

            left + node.val + right

        This might be the best path in the whole tree.

        ------------------------------------------------------------

        WHY max(0, dfs(child)) ?
        ------------------------

        If a subtree contributes a negative sum, we ignore it.

        Example:

                5
               /
             -10

        Taking -10 makes the sum worse.

        So we treat negative paths as 0.


        ------------------------------------------------------------
        RECURSION STRATEGY
        ------------------------------------------------------------

        DFS returns:

            maximum path sum that can extend upward from this node


        But during traversal we update a global maximum for:

            left + node.val + right


        ------------------------------------------------------------
        WHY res = [root.val] ?
        ------------------------------------------------------------

        We store the result in a list so the nested function
        can modify it.

        Lists are mutable, so updates inside dfs affect the
        outer variable.


        ------------------------------------------------------------
        WALKTHROUGH EXAMPLE
        ------------------------------------------------------------

                -10
                /  \
               9   20
                  /  \
                 15   7

        Step-by-step DFS:

        Node = 15
            left = 0
            right = 0
            path_through = 15
            res = 15
            return 15

        Node = 7
            left = 0
            right = 0
            path_through = 7
            res = 15
            return 7

        Node = 20
            left = 15
            right = 7
            path_through = 15 + 20 + 7 = 42
            res = 42
            return 20 + max(15,7) = 35

        Node = 9
            path_through = 9
            res = 42
            return 9

        Node = -10
            left = 9
            right = 35
            path_through = 9 + (-10) + 35 = 34
            res remains 42

        Final Answer = 42


        ------------------------------------------------------------
        TIME COMPLEXITY
        ------------------------------------------------------------
        O(n)
        We visit every node once.

        ------------------------------------------------------------
        SPACE COMPLEXITY
        ------------------------------------------------------------
        O(h)
        h = height of the tree (recursion stack)
        """

        # Store global maximum path sum
        res = [root.val]

        def dfs(node):

            # Base case
            if not node:
                return 0

            # Get max path from left subtree
            left = max(0, dfs(node.left))

            # Get max path from right subtree
            right = max(0, dfs(node.right))

            # Path that passes through current node
            current_path = left + node.val + right

            # Update global maximum if this path is larger
            res[0] = max(res[0], current_path)

            # Return the best single path that can extend upward
            return node.val + max(left, right)

        dfs(root)

        return res[0]