class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums1 = nums.copy()
        # return nums+nums1
        nums1 = nums.copy()
        ans=nums.extend(nums1)
        return nums