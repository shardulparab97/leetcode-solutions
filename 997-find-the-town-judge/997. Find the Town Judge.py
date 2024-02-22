class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        res = [0] * (n+1)

        for a, b in trust:
            res[a] = -1
            if res[b] != -1:
                res[b] += 1

        ans = -1
        for i in range(1, n+1):
            if res[i] == n-1:
                if ans != -1:
                    return -1
                ans = i
        
        return ans


        