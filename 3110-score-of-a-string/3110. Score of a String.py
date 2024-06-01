class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)

        ans = 0
        for i in range(0, n-1):
            ans += abs(ord(s[i]) - ord(s[i+1]))

        return ans