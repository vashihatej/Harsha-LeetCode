class Solution:
    def subarrayBitwiseORs(self, arr):
        """
        We maintain:
        - cur: all distinct OR values of subarrays ending at current index
        - ans: global set of all distinct OR values
        
        Key idea:
        For each element x:
            New subarrays ending here are:
                - [x]
                - previous_subarray_OR | x
        """

        ans = set()
        cur = set()

        for x in arr:
            # Compute new OR results ending at this position
            new_cur = {x}
            
            for prev in cur:
                new_cur.add(prev | x)

            cur = new_cur

            # Add all new OR values to answer set
            ans |= cur

        return len(ans)