class Solution:
    def maxDepth(self, s: str) -> int:
        st = collections.deque()
        ans = float("-inf")
        cnt = 0

        for c in s:
            if c == "(":
                cnt += 1
            elif c == ")":
                cnt -= 1
            ans = max(ans, cnt)
        
        return ans if ans != float("-inf") else 0

        
        