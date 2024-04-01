class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans, p = 0, len(s) - 1

        while p >= 0:
            if s[p] != ' ':
                ans += 1
            elif ans>0:
                return ans
            p -= 1

        return ans