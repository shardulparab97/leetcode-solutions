class Solution:
    def solve(self, idx, buy):
        if idx >= self.n: 
            return 0
        
        if (idx, buy) in self.dp:
            return self.dp[(idx, buy)]

        op1, op2 = None, None
        if buy:
            op1 = -self.prices[idx] + self.solve(idx+1, 0)
            op2 = self.solve(idx+1, 1)
        else:
            op1 = self.prices[idx] + self.solve(idx+2, 1)
            op2 = self.solve(idx+1, 0)
        
        self.dp[(idx, buy)] = max(op1, op2)
        return self.dp[(idx, buy)]

        
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.n = len(prices)
        self.dp = dict()

        return self.solve(0, 1)