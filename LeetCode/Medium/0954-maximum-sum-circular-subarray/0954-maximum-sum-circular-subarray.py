class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum=nums[0]
        min_sum=nums[0]
        total=0
        cursum=0
        curmin=0
        for n in nums:
            
            cursum=max(cursum+n, n) #instead of tahen cursum + sum only if cursum is > 0 or just take n
            curmin=min(curmin+n, n)
            total +=n

            min_sum = min(min_sum, curmin)
            max_sum = max(max_sum, cursum)

        return max(total-min_sum, max_sum) if max_sum>0 else max_sum