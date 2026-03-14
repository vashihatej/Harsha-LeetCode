class Solution:
    def numberToWords(self, num: int) -> str:
        """
        Convert a non-negative integer into English words.

        Strategy
        --------
        1. English numbers are naturally grouped in blocks of 3 digits:
           Billion -> Million -> Thousand -> (last 3 digits)

        2. For each 3-digit block we convert it independently using a helper
           function.

        3. Then attach the appropriate scale word
           (Thousand / Million / Billion).

        Example:
            1234567

            1       Million
            234     Thousand
            567

        Final:
            One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven
        """

        # Edge case
        if num == 0:
            return "Zero"

        # Words for numbers < 20
        below_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six",
            "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
            "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"
        ]

        # Words for tens place
        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        # Large number labels
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            """
            Convert a number < 1000 into words.
            """

            if n == 0:
                return ""

            # Case 1: number < 20
            elif n < 20:
                return below_20[n] + " "

            # Case 2: number < 100
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)

            # Case 3: number >= 100
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        i = 0

        # Process number in groups of 3 digits
        while num > 0:

            if num % 1000 != 0:
                # Convert current 3-digit block
                res = helper(num % 1000) + thousands[i] + " " + res

            num //= 1000
            i += 1

        # Remove extra spaces
        return res.strip()