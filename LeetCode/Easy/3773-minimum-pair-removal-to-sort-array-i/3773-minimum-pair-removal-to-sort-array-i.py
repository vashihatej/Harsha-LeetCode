class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def issorted(arr):
            for i in range(1, len(arr)):
                if arr[i]<arr[i-1]:
                    return False
            return True
        count_operations=0
        while not issorted(nums):
            min_sum=float('inf')
            index=0
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1]<min_sum:
                    min_sum=nums[i]+nums[i+1]
                    index=i
            nums = nums[:index] + [min_sum] + nums[index+2:]
            count_operations+=1
        return count_operations