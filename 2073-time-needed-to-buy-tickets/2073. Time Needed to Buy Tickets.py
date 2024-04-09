class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        ans = 0

        for i in range(n):
            if i <= k:
                ans += min(tickets[k], tickets[i])
            else:
                ans += min(tickets[k]-1, tickets[i])

        return ans

        
