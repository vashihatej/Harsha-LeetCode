class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        freq = {}

        # Count frequencies of all numbers
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        def dfs(sub):
            # Base case: when permutation is complete
            if len(sub) == len(nums):
                res.append(sub.copy())
                return

            # Try each unique number
            for n in freq:
                if freq[n] > 0:
                    # choose
                    sub.append(n)
                    freq[n] -= 1

                    # explore
                    dfs(sub)

                    # backtrack
                    sub.pop()
                    freq[n] += 1

        dfs([])
        return res
