class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        for i in range(0, len(nums)):
            a = nums[i]
            diff = target - a

            if diff in freq:
                return [freq[diff], i]
            freq[a] = i

