class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        cursum=0
        for n in nums:
            
            if cursum<0:
                cursum=0
            cursum+=n

            max_sum = max(max_sum, cursum)
        return max_sum