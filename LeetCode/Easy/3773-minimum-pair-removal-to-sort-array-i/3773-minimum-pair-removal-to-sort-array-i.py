class Solution:
    def minimumPairRemoval(self, nums):
        """
        Simulate the process:
        - While array is not non-decreasing:
            - Find adjacent pair with minimum sum
            - Replace that pair with their sum
            - Count operations
        """

        def is_sorted(arr):
            # Check if array is non-decreasing
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True

        operations = 0

        while not is_sorted(nums):

            # Find minimum adjacent pair sum
            min_sum = float('inf')
            index = 0

            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i+1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    index = i   # leftmost minimum automatically

            # Replace pair with their sum
            nums = nums[:index] + [min_sum] + nums[index+2:]

            operations += 1

        return operations