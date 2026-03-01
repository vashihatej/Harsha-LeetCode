class Solution:
    def minOperations(self, n: int) -> int:
        """
        We count ONLY operations of the form: n += 2^k or n -= 2^k.

        Greedy on lowest bits:
        - If n is even: we can shift right in our computation (free), because
          trailing zeros mean n is divisible by 2 and we're just moving to the next bit.
          (This is NOT an allowed operation, so we do NOT count it.)
        - If n is odd: we MUST do either n-1 or n+1 (i.e., subtract/add 1).
          That IS a valid operation (power of 2 = 1), so we count it.
          Then we divide by 2 to continue processing higher bits.

        Rule for odd n:
        - If n == 1: best is n -= 1 (finish)
        - Else if n % 4 == 1: do n -= 1  (binary ends with ...01)
        - Else: do n += 1      (binary ends with ...11), because adding 1 collapses
          a run of trailing 1s into trailing 0s (more efficient)
        """
        ops = 0

        while n > 0:
            if n % 2 == 0:
                # even -> just shift right in our reasoning (free)
                n //= 2
            else:
                # odd -> must use +/- 1 (a power of 2), so this is 1 operation
                ops += 1

                if n == 1 or n % 4 == 1:
                    # ...01 (or n==1): subtract 1
                    n = (n - 1) // 2
                else:
                    # ...11: add 1 (collapses trailing 1s), then divide by 2
                    n = (n + 1) // 2

        return ops