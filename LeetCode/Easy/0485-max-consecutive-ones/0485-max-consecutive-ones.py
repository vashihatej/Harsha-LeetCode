class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        We scan the array once.
        
        If we see 1 → increase current streak.
        If we see 0 → reset streak.
        
        Track maximum streak seen so far.
        """

        current_count = 0
        max_count = 0

        for num in nums:

            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0  # streak breaks

        return max_count