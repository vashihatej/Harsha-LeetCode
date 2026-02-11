class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key = lambda x:x[0])

        if intervals:
            end=intervals[0][1]
        else:
            return True

        for i in range(1, len(intervals)):
            if intervals[i][0]<end:
                return False
            end=intervals[i][1]
        return True

        