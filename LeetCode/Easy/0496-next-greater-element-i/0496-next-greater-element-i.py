from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        We need, for each value x in nums1, the FIRST greater value to the RIGHT of x in nums2.
        nums1 is a subset of nums2 (and values are distinct), so each value appears exactly once in nums2.

        Big idea:
        1) First compute "next greater" for EVERY value in nums2 (one pass) using a monotonic stack.
        2) Store results in a map: next_greater[value] = next greater value (or -1 if none).
        3) Build answer for nums1 by looking up each nums1 value in the map.
        """

        # ------------------------------------------------------------
        # STEP 1: Build next_greater map for nums2
        #
        # "Next greater element" for a number v means:
        #   Scan to the right of v in nums2,
        #   the first number you meet that is > v is the answer.
        #   If no such number exists, answer is -1.
        #
        # Example: nums2 = [1, 3, 4, 2]
        #   next greater of 1 is 3
        #   next greater of 3 is 4
        #   next greater of 4 is -1
        #   next greater of 2 is -1
        #
        # We compute this efficiently using a monotonic DECREASING stack.
        # Stack stores values (or indices) that are still "waiting" to find their next greater.
        #
        # Invariant:
        #   stack is decreasing from bottom -> top
        #   (top is the smallest among the waiting ones)
        # ------------------------------------------------------------
        next_greater = {}    # value -> next greater value
        stack = []          # stack of values waiting for a next greater

        for cur in nums2:
            # While current number is bigger than the stack top,
            # it means: cur is the "next greater" for that stack top value.
            #
            # Why?
            # Because:
            # - stack top appeared earlier (to the left)
            # - we are scanning left -> right
            # - this is the first time we found something bigger than it
            while stack and cur > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = cur  # first greater element to its right is cur

            # Push current value onto stack (it will wait for its next greater)
            stack.append(cur)

        # Any values left in the stack never found a greater element on the right.
        # So their next greater is -1.
        while stack:
            next_greater[stack.pop()] = -1

        # ------------------------------------------------------------
        # STEP 2: Answer queries from nums1 using the map
        #
        # Now next_greater contains answers for EVERY number in nums2.
        # Since nums1 is a subset of nums2, each nums1 value exists in the map.
        # ------------------------------------------------------------
        return [next_greater[x] for x in nums1]


"""
-------------------------
Quick Walkthrough Example
-------------------------
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

Build next_greater using stack:

cur=1: stack=[] -> push 1
  stack=[1]

cur=3: 3 > 1 -> pop 1, next_greater[1]=3
  stack=[] -> push 3
  stack=[3]

cur=4: 4 > 3 -> pop 3, next_greater[3]=4
  stack=[] -> push 4
  stack=[4]

cur=2: 2 is not > 4 -> push 2
  stack=[4,2]

end: leftover stack -> next_greater[2]=-1, next_greater[4]=-1

Map is:
  1 -> 3
  3 -> 4
  4 -> -1
  2 -> -1

Now answer nums1:
  4 -> -1
  1 -> 3
  2 -> -1

Return [-1, 3, -1]
"""