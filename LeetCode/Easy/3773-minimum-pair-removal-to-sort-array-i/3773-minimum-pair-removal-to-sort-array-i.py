class Solution:
    def minimumPairRemoval(self, nums):
        """
        Problem:
        Repeatedly:
        1) Find the adjacent pair with the minimum sum.
        2) If multiple, choose the leftmost.
        3) Replace the pair with their sum.
        4) Count operations.
        Stop when array becomes non-decreasing.

        Non-decreasing means:
            nums[i] >= nums[i-1]

        ------------------------------------------------------------
        Example Walkthrough:
        ------------------------------------------------------------
        Input:
            nums = [5,2,3,1]

        Step 1:
            Check if sorted:
                5 > 2 ❌ → not sorted

            Adjacent sums:
                (5,2) = 7
                (2,3) = 5
                (3,1) = 4  ← minimum

            Replace (3,1) with 4

            nums becomes:
                [5,2,4]

            operations = 1

        Step 2:
            Check sorted:
                5 > 2 ❌

            Adjacent sums:
                (5,2) = 7
                (2,4) = 6  ← minimum

            Replace (2,4) with 6

            nums becomes:
                [5,6]

            operations = 2

        Step 3:
            Check sorted:
                5 <= 6 ✅

            STOP

        Answer = 2
        ------------------------------------------------------------
        """

        # Helper function to check if array is non-decreasing
        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True

        operations = 0

        # Keep merging until sorted
        while not is_sorted(nums):

            # Find adjacent pair with minimum sum
            min_sum = float('inf')
            index = 0

            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]

                # Leftmost minimum automatically chosen
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    index = i

            # Replace the pair with their sum
            # Example:
            # nums = [5,2,4]
            # If index = 1 (2,4), then:
            # nums[:1] = [5]
            # + [6]
            # + nums[3:] = []
            nums = nums[:index] + [min_sum] + nums[index + 2:]

            operations += 1

        return operations