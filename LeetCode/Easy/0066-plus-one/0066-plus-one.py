class Solution:
    def plusOne(self, digits):
        """
        We are given a list of digits representing a non-negative integer.
        Example:
            [1,2,9] represents the number 129

        Goal:
            Add 1 to the number and return the new digits list.

        Core Idea:
            We simulate how addition works manually from right to left.
            If a digit is 9, adding 1 makes it 0 and produces a carry.
            If a digit is not 9, we add 1 and stop (no more carry).
        """

        # -------------------------------------------------------
        # Start from the LAST digit (rightmost)
        # Because addition begins from the right side.
        # -------------------------------------------------------
        for i in range(len(digits) - 1, -1, -1):

            # ---------------------------------------------------
            # If digit is 9:
            # 9 + 1 = 10
            # So we write 0 and carry 1 to the left.
            # ---------------------------------------------------
            if digits[i] == 9:
                digits[i] = 0   # set to 0 and continue loop (carry)

            # ---------------------------------------------------
            # If digit is NOT 9:
            # Just add 1 and stop.
            # No more carry is needed.
            # ---------------------------------------------------
            else:
                digits[i] += 1
                return digits   # done

        # -------------------------------------------------------
        # If we exit the loop,
        # it means ALL digits were 9.
        #
        # Example:
        #   [9,9,9]
        #
        # Step-by-step:
        #   → [0,9,9]
        #   → [0,0,9]
        #   → [0,0,0]
        #
        # Since we still have a carry left,
        # we add 1 at the beginning.
        #
        # Final result:
        #   [1,0,0,0]
        # -------------------------------------------------------
        return [1] + digits

        # # Convert list of digits to string
        # num_str = "".join(str(d) for d in digits)
        
        # # Convert to integer and add 1
        # num = int(num_str) + 1
        
        # # Convert back to list of integers
        # return [int(c) for c in str(num)]