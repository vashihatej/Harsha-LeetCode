class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost):
            return -1
        start=0
        total=0
        for i in range(len(gas)):
            total+=gas[i]-cost[i]
            if total<0:
                start=i+1
                total=0
        return start

        