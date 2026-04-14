# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator=iterator
        self.next_val=self.iterator.next() if self.iterator.hasNext() else None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_val
        

    def next(self):
        """
        :rtype: int
        """
        val=self.next_val
        if self.iterator.hasNext():
            self.next_val=self.iterator.next()
        else:
            self.next_val = None

        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_val is not None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


#----------------------------------#

class PeekingIterator:
    """
    PeekingIterator wraps an existing iterator and adds one extra feature:
    the ability to peek at the next element without advancing the iterator.

    Normally an iterator supports:
        next()    -> return next element and move forward
        hasNext() -> check if more elements exist

    We must add:
        peek()    -> see the next element WITHOUT moving the iterator.

    Key Idea
    --------
    We store (prefetch) the next element in advance.

    This variable:
        self.next_val

    always holds the NEXT element that should be returned.

    So:
        peek()    -> return next_val
        next()    -> return next_val and load the next element
        hasNext() -> check if next_val exists

    Example
    -------
    Input iterator: [1,2,3]

    Initialization:
        next_val = 1

    Operations:
        peek() -> 1 (pointer does NOT move)
        next() -> 1 (pointer moves, next_val becomes 2)
        peek() -> 2
        next() -> 2
        next() -> 3
        hasNext() -> False
    """

    def __init__(self, iterator):
        """
        Store the original iterator and prefetch the first value.

        Prefetching means we immediately read the first element
        so that peek() can return it without moving the iterator.
        """
        self.iterator = iterator

        # If the iterator has elements, load the first one.
        # Otherwise store None.
        self.next_val = iterator.next() if iterator.hasNext() else None


    def peek(self):
        """
        Return the next element WITHOUT advancing the iterator.

        Since we always store the next element in self.next_val,
        we simply return it.
        """
        return self.next_val


    def next(self):
        """
        Return the next element and move the iterator forward.

        Steps:
        1. Save the current next_val (this is the value to return).
        2. Fetch the next element from the underlying iterator.
        3. Update next_val.
        """
        val = self.next_val  # store value to return

        # Move iterator forward by fetching the next element
        if self.iterator.hasNext():
            self.next_val = self.iterator.next()
        else:
            # If no more elements remain
            self.next_val = None

        return val


    def hasNext(self):
        """
        Return True if another element exists.

        Instead of checking the underlying iterator,
        we check the cached value.

        If next_val is not None, there is still an element
        available to return.
        """
        return self.next_val is not None