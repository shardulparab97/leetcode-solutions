class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # https://leetcode.com/problems/optimal-account-balancing/solutions/219187/short-o-n-2-n-dp-solution-with-detailed-explanation-and-complexity-analysis/ 

        

        balances = collections.defaultdict(int)
        
        for giver, receiver, amount in transactions:
            balances[giver] -= amount
            balances[receiver] += amount

        amounts = [amount for amount in balances.values() if amount!=0]
        n = len(amounts)

        dp = [0] * (2**n)
        sum = [0] * (2**n)

        for mask in range(2**n):
            set_bit = 1
            for i in range(n):
                if mask & set_bit == 0: # item at set bit not used yet
                    nxt = mask | set_bit
                    sum[nxt] = sum[mask] + amounts[i]
                    if sum[nxt] == 0:
                        dp[nxt] = max(dp[nxt], dp[mask] + 1)
                    else:
                        dp[nxt] = max(dp[nxt], dp[mask])

                set_bit <<= 1

        return n - dp[-1]
