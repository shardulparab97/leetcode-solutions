class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # two check conditions
        if n == 1:
            return True
        
        g = collections.defaultdict(list)

        def getPrimeFactors(num):
            pf = []
            i = 2
            while i*i <= num:
                if num % i == 0:
                    pf.append(i)
                    while num % i == 0:
                        num = num // i
                i += 1
            if num != 1:
                pf.append(num)
            return pf
        
        seen = collections.defaultdict(int)

        for num in nums:
            if num == 1:
                return False
            pf = getPrimeFactors(num)
            for p in pf:
                if p in seen:
                    g[num].append(seen[p])
                    g[seen[p]].append(num)
                else:
                    seen[p] = num
        
        # find number of connected components
        def dfs(num):
            vis.add(num)
            for node in g[num]:
                if node not in vis:
                    dfs(node)

        numConnected = 0
        vis = set()
        for num in nums:
            if num not in vis:
                dfs(num)
                numConnected += 1
        return numConnected == 1



        

        
        