class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        def dfs(i, canbuy):
            if i>=len(prices):
                return 0
            if (i, canbuy) in memo:
                return memo[(i, canbuy)]
            if canbuy:
                buy=dfs(i+1, not canbuy)-prices[i]
                cooldown=dfs(i+1, canbuy)
                profit=max(buy,cooldown)
            else:
                sell=dfs(i+2, not canbuy)+prices[i]
                cooldown=dfs(i+1, canbuy)
                profit=max(sell,cooldown)
            memo[(i,canbuy)]=profit
            return memo[(i,canbuy)]
        return dfs(0, True)

#---------------------------#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        309. Best Time to Buy and Sell Stock with Cooldown

        ------------------------------------------------------------
        CORE IDEA
        ------------------------------------------------------------
        At every day, we only need to know ONE thing:

            Are we allowed to BUY right now?
            OR
            Are we currently HOLDING a stock, so next useful action is SELL?

        So our recursion state is:

            dfs(i, buying)

        where:
            i       = current day index
            buying  = True  -> we do NOT own a stock now, so we can buy
                       False -> we already own a stock now, so we can sell

        ------------------------------------------------------------
        WHAT CHOICES DO WE HAVE?
        ------------------------------------------------------------

        1) If buying == True
           We have two choices:

           a) BUY today
              profit = dfs(i + 1, False) - prices[i]

              Why?
              - We spend money to buy the stock, so subtract prices[i]
              - Tomorrow we will be in "holding stock" state,
                so buying becomes False

           b) COOLDOWN / SKIP today
              profit = dfs(i + 1, True)

              Why?
              - We do nothing today
              - Tomorrow we are still allowed to buy

           So:
               dfs(i, True) = max(buy, cooldown)

        ------------------------------------------------------------

        2) If buying == False
           This means we already own a stock.
           We again have two choices:

           a) SELL today
              profit = dfs(i + 2, True) + prices[i]

              Why i + 2 ?
              - If we sell today, the next day is COOLDOWN
              - We are NOT allowed to buy on the very next day
              - So we skip one day and move to i + 2
              - After selling, we no longer hold a stock, so buying=True

           b) COOLDOWN / SKIP today
              profit = dfs(i + 1, False)

              Why?
              - We keep holding the stock
              - Tomorrow we are still in "holding stock" state

           So:
               dfs(i, False) = max(sell, cooldown)

        ------------------------------------------------------------
        BASE CASE
        ------------------------------------------------------------
        If i >= len(prices):
            return 0

        Why?
        - No more days left
        - No more profit can be made

        ------------------------------------------------------------
        WHY MEMOIZATION?
        ------------------------------------------------------------
        Many recursive calls repeat the same state.

        Example:
            dfs(3, True) might be reached from multiple different paths.

        Instead of recomputing it every time, we store:

            dp[(i, buying)] = answer

        This reduces time complexity from exponential to linear.

        ------------------------------------------------------------
        RECURSION TREE INTUITION
        ------------------------------------------------------------
        Example:
            prices = [1, 2, 3, 0, 2]

        Start:
            dfs(0, True)

        Tree idea:

                               dfs(0, True)
                              /            \
                     buy at 1 /              \ skip
                            /                \
                  dfs(1, False)            dfs(1, True)
                    /       \                /       \
            sell at 2       hold      buy at 2      skip
              /               \          /            \
       dfs(3, True)     dfs(2, False)  ...          ...

        Let's follow one optimal path:

            dfs(0, True)
            -> buy at price 1
            -> dfs(1, False)

            dfs(1, False)
            -> sell at price 2
            -> dfs(3, True)      # note: i + 2 because of cooldown

            dfs(3, True)
            -> buy at price 0
            -> dfs(4, False)

            dfs(4, False)
            -> sell at price 2
            -> dfs(6, True)

        Profit from this path:
            -1 + 2 - 0 + 2 = 3

        Which matches the expected answer.

        ------------------------------------------------------------
        VISUAL STATE TRANSITION
        ------------------------------------------------------------

            buying = True
                |
                |-- Buy today  -> dfs(i+1, False) - prices[i]
                |
                |-- Skip today -> dfs(i+1, True)

            buying = False
                |
                |-- Sell today -> dfs(i+2, True) + prices[i]
                |                (because next day is cooldown)
                |
                |-- Skip today -> dfs(i+1, False)

        ------------------------------------------------------------
        TIME COMPLEXITY
        ------------------------------------------------------------
        There are only 2 possible buying states for each day.

            states = n * 2

        Each state is solved once due to memoization.

            Time Complexity:  O(n)
            Space Complexity: O(n)

        ------------------------------------------------------------
        WHY THIS SOLUTION IS EASY TO REMEMBER
        ------------------------------------------------------------
        Just remember:

            dfs(i, buying)

        If buying:
            max( buy, skip )

        Else:
            max( sell, skip )

        And the only special part in this problem is:

            SELL -> jump to i + 2

        because of the cooldown day.
        """

        # Memo dictionary:
        # key   -> (day_index, buying_state)
        # value -> maximum profit from that state onward
        dp = {}

        def dfs(i, buying):
            """
            Returns the maximum profit we can make starting from day i.

            Parameters:
                i       : current day
                buying  : True  -> we are allowed to buy
                           False -> we currently hold a stock, so we may sell
            """

            # Base case:
            # If we are beyond the last day, no profit can be made.
            if i >= len(prices):
                return 0

            # If this state was already computed, return cached answer.
            if (i, buying) in dp:
                return dp[(i, buying)]

            # Case 1: We are allowed to buy
            if buying:
                # Option 1: Buy stock today
                # We spend prices[i], so subtract it.
                buy = dfs(i + 1, False) - prices[i]

                # Option 2: Do nothing today
                cooldown = dfs(i + 1, True)

                # Choose the better option
                dp[(i, buying)] = max(buy, cooldown)

            # Case 2: We currently hold a stock
            else:
                # Option 1: Sell stock today
                # We gain prices[i]
                # Then next day is cooldown, so move to i + 2
                sell = dfs(i + 2, True) + prices[i]

                # Option 2: Do nothing today and keep holding
                cooldown = dfs(i + 1, False)

                # Choose the better option
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        # Start from day 0, and initially we are allowed to buy
        return dfs(0, True)
