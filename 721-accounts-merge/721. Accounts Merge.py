class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        g = collections.defaultdict(set)

        for account in accounts:
            for email in account[1:]:
                g[account[1]].add(email)
                g[email].add(account[1])

        vis = set()

        def dfs(email, res):
            vis.add(email)
            res.append(email)

            for nei in g[email]:
                if nei not in vis:
                    dfs(nei, res)

        ans = []
        for account in accounts:
            name = account[0]
            
            
            for email in account[1:]:
                if email not in vis:
                    res = []
                    dfs(email, res)
                    ans.append([name] + sorted(res))

        return ans

