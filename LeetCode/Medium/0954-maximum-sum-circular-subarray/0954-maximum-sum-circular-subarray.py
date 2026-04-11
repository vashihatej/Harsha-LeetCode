class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Problem:
        --------
        Given a circular array, find the maximum possible sum of a non-empty subarray.

        Core Thinking:
        --------------
        This is an extension of the classic maximum subarray problem (Kadane’s Algorithm).

        In a circular array, the maximum subarray can be of TWO types:

        1) NON-WRAPPING SUBARRAY (normal case)
        Example: [1, -2, 3, -2] → best = [3]
        → This is solved using standard Kadane’s Algorithm.

        2) WRAPPING SUBARRAY (circular case)
        Example: [5, -3, 5] → best = [5] + [5] (wraps around)
        
        Instead of directly finding the wrapping subarray, we use this trick:
        
        total_sum = sum of entire array
        middle_part = the subarray we EXCLUDE (this will be the minimum subarray)
        
        So:
        wrapping_sum = total_sum - minimum_subarray_sum

        → We find the minimum subarray using a modified Kadane.

        Final Answer:
        -------------
        max(
            max_subarray_sum (normal Kadane),
            total_sum - min_subarray_sum (wrap case)
        )

        Important Edge Case:
        --------------------
        If all elements are negative:
            Example: [-3, -2, -3]
            - max_subarray_sum = -2
            - min_subarray_sum = -8
            - total_sum - min_subarray_sum = 0 (INVALID → empty subarray)

        So:
            If max_subarray_sum < 0 → return max_subarray_sum directly

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # Step 1: Compute total sum of array
        total_sum = sum(nums)

        # Step 2: Initialize Kadane variables for max and min subarrays
        curr_max = global_max = nums[0]  # For maximum subarray
        curr_min = global_min = nums[0]  # For minimum subarray

        # Step 3: Traverse array and update both Kadane computations
        for num in nums[1:]:
            # Standard Kadane (max subarray)
            # Either start fresh from current number OR extend previous subarray
            curr_max = max(num, curr_max + num)
            global_max = max(global_max, curr_max)

            # Reverse Kadane (min subarray)
            # Either start fresh OR extend previous (for minimum sum)
            curr_min = min(num, curr_min + num)
            global_min = min(global_min, curr_min)

        # Step 4: Handle edge case (all numbers are negative)
        if global_max < 0:
            return global_max

        # Step 5: Return best of both cases
        return max(global_max, total_sum - global_min)