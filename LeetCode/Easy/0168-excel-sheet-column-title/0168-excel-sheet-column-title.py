class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        This is similar to converting number to base-26,
        but Excel is 1-indexed (A = 1, not 0).

        So we:
        1) Subtract 1
        2) Take mod 26
        3) Convert to character
        4) Divide by 26
        """

        result = ""

        while columnNumber > 0:

            # Step 1: shift to 0-based
            columnNumber -= 1

            # Step 2: get remainder
            remainder = columnNumber % 26

            # Step 3: convert remainder to letter
            # chr(ord('A') + remainder)
            result = chr(ord('A') + remainder) + result

            # Step 4: move to next position
            columnNumber //= 26

        return result