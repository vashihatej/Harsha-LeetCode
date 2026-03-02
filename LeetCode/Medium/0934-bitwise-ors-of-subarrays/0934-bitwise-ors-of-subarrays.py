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


"""
        PROBLEM:
        Return the number of DISTINCT bitwise OR results
        from all non-empty contiguous subarrays.

        -------------------------------------------------------
        KEY IDEA:
        Instead of generating ALL subarrays (O(n²)),
        we keep track of:

            cur = all OR results of subarrays
                  that END at current index

        Because:
        If we know all OR results ending at index i-1,
        then subarrays ending at index i are:

            1) The single element [x]
            2) previous_OR | x for every previous OR

        So:

            new_cur = { x } ∪ { prev | x for prev in cur }

        -------------------------------------------------------
        WHY THIS WORKS:

        Bitwise OR has special property:
        Once a bit becomes 1, it NEVER becomes 0.

        That means OR values grow but stabilize quickly.
        So the set size stays small (≤ about 30 values).

        -------------------------------------------------------
        EXAMPLE WALKTHROUGH
        -------------------------------------------------------

        Example:
            arr = [1, 1, 2]

        Step 1:
            x = 1
            cur = {1}
            ans = {1}

        Step 2:
            x = 1
            previous cur = {1}

            new_cur:
                start new subarray → {1}
                extend previous → 1|1 = 1

            new_cur = {1}

            ans still = {1}

        Step 3:
            x = 2
            previous cur = {1}

            new_cur:
                start new subarray → {2}
                extend previous → 1|2 = 3

            new_cur = {2, 3}

            ans = {1, 2, 3}

        FINAL ANSWER = 3

        -------------------------------------------------------
        Example 2:
            arr = [1,2,4]

        Step 1:
            x=1
            cur={1}
            ans={1}

        Step 2:
            x=2
            new_cur:
                {2}
                1|2=3
            cur={2,3}
            ans={1,2,3}

        Step 3:
            x=4
            new_cur:
                {4}
                2|4=6
                3|4=7
            cur={4,6,7}
            ans={1,2,3,4,6,7}

        FINAL ANSWER = 6

        -------------------------------------------------------
        INTUITION:

        We are not recomputing every subarray.
        We are building OR results incrementally.

        Each position only depends on previous OR results.

        -------------------------------------------------------
        TIME COMPLEXITY:
            O(n * 30)  ≈  O(n)

        Because at most ~30 distinct OR values per index.
        """