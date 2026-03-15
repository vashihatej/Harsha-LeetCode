"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""
class Codec:
    """
    We need to convert an N-ary tree into a string (serialize)
    and reconstruct the same tree from that string (deserialize).

    The main challenge with N-ary trees is that each node can have
    ANY number of children.

    In a binary tree, we always know:
        left child
        right child

    But in an N-ary tree we must store how many children each node has.

    ----------------------------------------------------------------

    STRATEGY

    During serialization we store for each node:

        [node_value, number_of_children]

    Then we recursively serialize all children.

    Example tree:

            1
         /  |  \
        3   2   4
       / \
      5   6

    DFS traversal order:

    Node 1:
        value = 1
        children = 3  -> (3,2,4)

    Node 3:
        value = 3
        children = 2  -> (5,6)

    Node 5:
        value = 5
        children = 0

    Node 6:
        value = 6
        children = 0

    Node 2:
        value = 2
        children = 0

    Node 4:
        value = 4
        children = 0

    Serialized sequence becomes:

        1,3,3,2,5,0,6,0,2,0,4,0

    Pattern:
        value , number_of_children

    ----------------------------------------------------------------

    DESERIALIZATION

    When rebuilding the tree we read the numbers in order.

    Example:

        1,3  → node 1 with 3 children
        3,2  → node 3 with 2 children
        5,0  → node 5 with 0 children
        6,0  → node 6 with 0 children
        2,0
        4,0

    Because we know the child count, we know exactly how many
    recursive calls to make to build children.
    """

    def serialize(self, root):
        """
        Converts the N-ary tree into a string.

        We perform a DFS traversal and record for each node:
            node value
            number of children

        Example output string:
            "1,3,3,2,5,0,6,0,2,0,4,0"
        """

        # If tree is empty return empty string
        if not root:
            return ""

        result = []

        def dfs(node):
            """
            DFS traversal that records node information.

            For each node we append two values:
                node value
                number of children

            Then recursively process all children.
            """

            # Store node value
            result.append(str(node.val))

            # Store number of children this node has
            # This is critical because N-ary nodes can have variable children
            result.append(str(len(node.children)))

            # Recursively serialize each child
            for child in node.children:
                dfs(child)

        # Start DFS from root
        dfs(root)

        # Convert list to comma separated string
        return ",".join(result)


    def deserialize(self, data):
        """
        Reconstruct the tree from the serialized string.

        We read the serialized values in order and rebuild the tree
        using the stored child counts.

        Example serialized data:
            "1,3,3,2,5,0,6,0,2,0,4,0"
        """

        # If input string is empty there is no tree
        if not data:
            return None

        # Split string into list of values
        values = data.split(",")

        # Pointer to track where we are in the list
        self.index = 0

        def dfs():
            """
            Recursive function that rebuilds the tree.

            Steps:
            1. Read node value
            2. Read number of children
            3. Create the node
            4. Recursively build its children
            """

            # Read the node value
            val = int(values[self.index])
            self.index += 1

            # Read how many children this node has
            child_count = int(values[self.index])
            self.index += 1

            # Create the node
            node = Node(val, [])

            # Recursively construct each child
            for _ in range(child_count):
                node.children.append(dfs())

            # Return constructed node
            return node

        # Start reconstruction from root
        return dfs()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))