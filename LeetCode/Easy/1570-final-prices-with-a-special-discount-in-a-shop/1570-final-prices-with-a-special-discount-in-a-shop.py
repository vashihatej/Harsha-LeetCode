class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []  # will store indices
        result = prices[:]  # copy original prices
        
        for i in range(n):
            # While current price is smaller or equal,
            # it becomes discount for previous items
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                result[idx] = prices[idx] - prices[i]
            
            stack.append(i)
        
        return result