class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        k=float("-inf")
        ans=0
        for x, y in intervals:
            if x>=k:
                k=y
            else:
                ans+=1
        return ans