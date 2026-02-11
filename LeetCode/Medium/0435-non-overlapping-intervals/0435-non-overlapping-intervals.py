class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their end time
        # Greedy idea: always keep the interval that finishes earliest
        intervals.sort(key=lambda x: x[1])

        # 'k' stores the end time of the last interval we decided to keep
        # Initialize to negative infinity so the first interval is always considered
        k = float("-inf")

        # 'ans' counts how many intervals we need to remove
        ans = 0

        # Iterate through each interval in order of increasing end time
        for x, y in intervals:
            # If the current interval starts after or exactly when
            # the last kept interval ends, it does NOT overlap
            if x >= k:
                # Keep this interval and update the last end time
                k = y
            else:
                # Overlap detected
                # We remove this interval (greedy choice)
                ans += 1

        # Return the total number of removed intervals
        return ans
