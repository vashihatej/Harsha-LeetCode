# The knows API is already defined for you.
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        STEP 1: Find a potential celebrity candidate.

        We start assuming person 0 might be the celebrity.

        For every other person i:
            If candidate knows i → candidate cannot be celebrity.
            So i becomes the new candidate.

        After this pass, we have ONE possible celebrity.
        """

        candidate = 0

        for i in range(1, n):

            # if candidate knows i, candidate cannot be celebrity
            if knows(candidate, i):
                candidate = i

        """
        STEP 2: Verify the candidate.

        The candidate must satisfy:
        1. Candidate knows nobody
        2. Everyone knows the candidate
        """

        for i in range(n):

            if i == candidate:
                continue

            # candidate should know nobody
            if knows(candidate, i):
                return -1

            # everyone should know candidate
            if not knows(i, candidate):
                return -1

        return candidate