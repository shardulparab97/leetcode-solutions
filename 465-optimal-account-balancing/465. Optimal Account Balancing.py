class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # https://leetcode.com/problems/optimal-account-balancing/solutions/219187/short-o-n-2-n-dp-solution-with-detailed-explanation-and-complexity-analysis/ 
        balances = collections.defaultdict(int)

        for t in transactions:
            balances[t[0]] -= t[2]
            balances[t[1]] += t[2]
        
        balances = [v for v in balances.values() if v!=0]

        n = len(balances)
        dp = [0] * (2**n) # dp[-1] will be when all are set/ all are available
        sums = [0] * (2**n)

        for mask in range(2**n): # looping over all the masks
            set_bit = 1
            for b in range(n): # setting 1 bit at a time
                if set_bit & mask == 0: # means it was unset previously
                    nxt = mask | set_bit
                    sums[nxt] = sums[mask] + balances[b]
                    if sums[nxt] == 0: # means we have found a useful subset
                        dp[nxt] = max(dp[nxt], dp[mask] + 1) 
                    else:
                        dp[nxt] = max(dp[nxt], dp[mask])
                set_bit = set_bit<<1
        return n - dp[-1]


        