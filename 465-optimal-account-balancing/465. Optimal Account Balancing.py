class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # backtracking 
        
        balance = collections.defaultdict(int)

        for t in transactions:
            balance[t[0]] -= t[2]
            balance[t[1]] += t[2]
        balance = [v for v in balance.values() if v!=0]
        # print(balance)
        n = len(balance)
        def solve(idx):
            # move to the next non zero option
            while idx<n and balance[idx] == 0:
                idx += 1
            
            if idx == n:
                return 0

            ans = float("inf")
            for t in range(idx+1, n):
                # if there needs to be a transactions
                if balance[idx] * balance[t] < 0:
                    balance[t] += balance[idx]
                    ans = min(ans, 1+solve(idx+1))
                    balance[t] -= balance[idx]
            return ans
        # print("here")
        # ans = solve(0)
        # print(ans)
        # return 0
        return solve(0)

        # balance_map = collections.defaultdict(int)
        # for a, b, amount in transactions:
        #     balance_map[a] += amount
        #     balance_map[b] -= amount
        
        # balance_list = [amount for amount in balance_map.values() if amount]
        # n = len(balance_list)
        # print(balance_list)
        
        # def dfs(cur):
        #     while cur < n and not balance_list[cur]:
        #         cur += 1
        #     if cur == n:
        #         return 0
        #     cost = float('inf')
        #     for nxt in range(cur + 1, n):
        #         # If nxt is a valid recipient, do the following: 
        #         # 1. add cur's balance to nxt.
        #         # 2. recursively call dfs(cur + 1).
        #         # 3. remove cur's balance from nxt.
        #         if balance_list[nxt] * balance_list[cur] < 0:
        #             balance_list[nxt] += balance_list[cur]
        #             cost = min(cost, 1 + dfs(cur + 1))
        #             balance_list[nxt] -= balance_list[cur]
        #     return cost
        # return dfs(0)


        