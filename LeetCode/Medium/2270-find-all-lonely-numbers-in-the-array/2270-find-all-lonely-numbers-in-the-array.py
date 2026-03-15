from collections import Counter

class Solution:
    def findLonely(self, nums):
        """
        A number is lonely if:
        1. It appears exactly once
        2. Its neighbors (x-1 and x+1) do not appear in the array
        """

        # Count frequency of each number
        freq = Counter(nums)

        result = []

        # Check each number
        for num in nums:

            # Condition 1: number must appear exactly once
            if freq[num] == 1:

                # Condition 2: neighbors must not exist
                if (num - 1) not in freq and (num + 1) not in freq:
                    result.append(num)

        return result
        