class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        PROBLEM
        -------
        We are given two lists of intervals:
            firstList  = [[start1, end1], ...]
            secondList = [[start2, end2], ...]

        Each list is already sorted by start time.

        Our goal is to find ALL overlapping intervals between these two lists.

        ---------------------------------------------------------------

        KEY IDEA (Two Pointer Technique)
        --------------------------------
        Since both lists are sorted, we can use two pointers:

            i → pointer for firstList
            j → pointer for secondList

        At each step we compare:

            firstList[i]
            secondList[j]

        ---------------------------------------------------------------

        HOW DO WE CHECK IF TWO INTERVALS OVERLAP?

        Suppose we have:

            A = [a_start, a_end]
            B = [b_start, b_end]

        They overlap if:

            max(a_start, b_start) <= min(a_end, b_end)

        Why?

            The later start must come before the earlier end.

        Example:

            [5,10]
            [8,12]

            start = max(5,8) = 8
            end   = min(10,12) = 10

            overlap → [8,10]

        ---------------------------------------------------------------

        WHAT DO WE DO AFTER CHECKING?

        We move the pointer whose interval finishes first.

        Example:

            firstList[i]  = [5,10]
            secondList[j] = [8,12]

        Since 10 < 12,
        the first interval finishes earlier,
        so we move pointer i forward.

        This works because the earlier interval cannot overlap with future intervals anymore.

        ---------------------------------------------------------------

        TIME COMPLEXITY
        ----------------
        O(n + m)

        where:
            n = len(firstList)
            m = len(secondList)

        Each pointer moves at most once per interval.

        ---------------------------------------------------------------

        SPACE COMPLEXITY
        ----------------
        O(k)

        where k = number of intersections stored.
        """

        result = []

        i = 0
        j = 0

        # Traverse both interval lists
        while i < len(firstList) and j < len(secondList):

            start = max(firstList[i][0], secondList[j][0])
            end   = min(firstList[i][1], secondList[j][1])

            # If start <= end → intervals overlap
            if start <= end:
                result.append([start, end])

            # Move the pointer whose interval ends first
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result