class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list to set for O(1) existence checks
        # Order does not matter for this problem
        numset = set(nums)

        # Stores the length of the longest consecutive sequence found
        longest = 0

        # Iterate through each unique number in the array
        for n in numset:
            # Only start counting if 'n' is the START of a sequence
            # i.e., there is no number just before it (n - 1) like start with number 1 soo we can get [1,2,3,4] not by something like 2 where (2-1) exists in set so in this case you can get the max ans like [2,3,4] which is not correct
            if (n - 1) not in numset:
                # 'n' is the smallest number in this consecutive sequence
                length = 0

                # Count how long the consecutive sequence continues
                # Check for n, n+1, n+2, ...
                while (n + length) in numset:
                    length += 1

                # Update the maximum sequence length
                longest = max(longest, length)

        return longest
