# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
class NestedIterator:
    """
    This iterator flattens a nested list of integers using a stack.

    The key idea is to simulate a DFS traversal.

    Instead of flattening the entire structure at once (which may be expensive),
    we flatten only when needed using the stack.

    Stack always stores elements in reverse order so we can process
    them from left to right.
    """

    def __init__(self, nestedList):
        """
        Initialize the stack with the elements of nestedList.

        We push them in reverse order so that the first element
        appears at the top of the stack.
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        Since hasNext() guarantees the top of the stack is an integer,
        we simply pop and return it.
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        Ensure the top of the stack is always an integer.

        If the top element is a list, we expand it by pushing its
        elements back onto the stack in reverse order.
        """

        while self.stack:

            top = self.stack[-1]

            # If it's an integer, we're ready to return it
            if top.isInteger():
                return True

            # Otherwise it's a nested list → expand it
            self.stack.pop()
            nested = top.getList()

            # Push elements in reverse order
            for elem in reversed(nested):
                self.stack.append(elem)

        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())