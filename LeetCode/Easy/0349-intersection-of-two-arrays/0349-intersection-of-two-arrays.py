class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1set=set(nums1)
        nums2set=set(nums2)
        res=[]
        if nums2set<nums1set:
            nums1set, nums2set= nums2set, nums1set
        for n in nums1set:
            if n in nums2set:
                res.append(n)
        return res

