class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = collections.defaultdict(int)
        ans = 0
        n = len(s)
        for ch in s:
            mp[ch] += 1
            if mp[ch] % 2 == 0:
                ans += 2

        return ans+1 if ans<n else ans
        

