# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res=[]
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        vals=data.split(",")
        self.i=0
        def dfs():
            if vals[self.i]=="N":
                self.i+=1
                return None
            node=TreeNode(int(vals[self.i]))
            self.i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()

#-------------------------------#

class Codec:
    """
    This class implements serialization and deserialization of a binary tree.

    Idea:
    -----
    We use PREORDER DFS traversal to convert the tree into a string.

    Preorder order:
        root → left → right

    While serializing:
        - If the node exists → store its value.
        - If the node is None → store a special marker "N".

    Example tree:

            1
           / \
          2   3
             / \
            4   5

    Preorder traversal with null markers becomes:

        1,2,N,N,3,4,N,N,5,N,N

    Why do we store "N" for null?
        Because without null markers we lose the tree structure.

        Example:
            1,2,3
        could represent multiple different trees.

        Adding null markers ensures we can reconstruct the exact structure.

    During deserialization:
        - We read values in preorder order.
        - If we see "N", we return None.
        - Otherwise we create a node and recursively build its left and right children.

    This works because preorder traversal uniquely reconstructs the tree
    when null markers are included.

    Time Complexity:
        O(n)

    Space Complexity:
        O(n)
    """

    def serialize(self, root):
        """
        Convert the binary tree into a string representation.
        """

        res = []

        def dfs(node):
            # If the node is None, record a null marker
            if not node:
                res.append("N")
                return

            # Record current node value
            res.append(str(node.val))

            # Recursively process left subtree
            dfs(node.left)

            # Recursively process right subtree
            dfs(node.right)

        # Start DFS from root
        dfs(root)

        # Convert list to comma-separated string
        return ",".join(res)


    def deserialize(self, data):
        """
        Convert the serialized string back into the original binary tree.
        """

        # Split the string into list of values
        vals = data.split(",")

        # Pointer used to track current index while rebuilding the tree
        self.i = 0

        def dfs():
            """
            Build the tree using preorder reconstruction.
            """

            # If the current value is "N", this represents a null node
            if vals[self.i] == "N":
                self.i += 1
                return None

            # Create a node with the current value
            node = TreeNode(int(vals[self.i]))

            # Move to the next value
            self.i += 1

            # Recursively construct the left subtree
            node.left = dfs()

            # Recursively construct the right subtree
            node.right = dfs()

            return node

        # Start rebuilding from root
        return dfs()