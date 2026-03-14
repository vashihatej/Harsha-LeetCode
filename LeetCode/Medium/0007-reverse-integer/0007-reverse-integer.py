

class Solution(object):
    def reverse(self, x):
        """
        Reverse digits of a signed 32-bit integer.

        Steps:
        1. Store the sign of x
        2. Work with the absolute value
        3. Build the reversed number digit by digit
        4. Put the sign back
        5. If result is outside 32-bit signed integer range, return 0

        32-bit signed integer range:
            [-2^31, 2^31 - 1]
            [-2147483648, 2147483647]
        """

        MAX = 2**31 - 1
        MIN = -2**31

        # Save sign separately
        sign = -1 if x < 0 else 1

        # Work only with positive value
        x = abs(x)

        rev = 0

        while x != 0:
            # Take last digit
            digit = x % 10

            # remove last digit from x
            x = x // 10

            # Build reversed number
            rev = rev * 10 + digit

        # Put sign back
        rev *= sign

        # Check 32-bit overflow
        if rev < MIN or rev > MAX:
            return 0

        return rev