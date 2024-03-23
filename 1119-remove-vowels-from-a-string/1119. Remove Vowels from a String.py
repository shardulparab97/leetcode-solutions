class Solution:
    def removeVowels(self, s: str) -> str:
        ans = ""
        ls = "aeiou"
        n = len(s)

        for i in range(n):
            c = s[i]
            if c not in ls:
                ans += c
        
        return ans