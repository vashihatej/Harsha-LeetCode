class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Problem:
        Count the number of substrings that:
        1) Contain equal number of 0s and 1s
        2) All 0s and all 1s in the substring are grouped consecutively

        Example:
        s = "00110011"

        Valid substrings:
        "0011", "01", "1100", "10", "0011", "01"
        Answer = 6
        """

        # Step 1: Build groups of consecutive same characters.
        # Instead of looking at substrings directly,
        # we compress the string into counts of consecutive characters.

        # Example:
        # s = "00110011"
        # groups = [2, 2, 2, 2]
        # meaning:
        # "00", "11", "00", "11"

        count = 1           # count of current consecutive characters
        groups = []         # stores lengths of consecutive groups

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                # If current character is same as previous,
                # increase the count of the current group
                count += 1
            else:
                # Character changed (e.g., 0 -> 1 or 1 -> 0)
                # Save the completed group size
                groups.append(count)
                # Start a new group
                count = 1

        # Append the last group (important!)
        groups.append(count)

        # Now groups contains sizes of consecutive character blocks.
        # Example:
        # "00110011" -> [2, 2, 2, 2]
        # "000111"   -> [3, 3]
        # "00110"    -> [2, 2, 1]

        # Step 2: Count valid substrings
        # Valid substrings occur only between adjacent groups.
        # For every pair of adjacent groups,
        # the number of valid substrings is:
        #
        # min(size_of_current_group, size_of_previous_group)
        #
        # Why?
        #
        # Example:
        # groups = [3, 2]
        # That means: "00011"
        #
        # We can form:
        # "01"
        # "0011"
        #
        # Total = min(3, 2) = 2

        res = 0

        for i in range(1, len(groups)):
            # Add the minimum of current and previous group
            res += min(groups[i], groups[i - 1])

        return res
