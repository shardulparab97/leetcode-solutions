class Solution:
    def removeVowels(self, s: str) -> str:
        ans = ""
        ls = "aeiou"

        for c in s:
            if c not in ls:
                ans += c
        
        return ans