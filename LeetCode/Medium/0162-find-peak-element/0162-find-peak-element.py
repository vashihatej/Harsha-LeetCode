class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #here we will implement n=binary search but we will serch the half where the the higher number is present which is adjacent to middle one like ex: [1,2,3,1] first m will be at 2 so which side the higher number is present its 3 and its right ride of the middle number so then we go on searching in that right side half
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            #if left neighbour is greater
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1
            #if right neighbour is greater
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
            else:
                return m