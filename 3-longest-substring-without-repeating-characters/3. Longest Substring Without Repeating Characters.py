class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        lo, hi = 0, 0
        freq = collections.defaultdict(int)

        ans = 0
        
        while hi<n:
            ch = s[hi]
            freq[ch] += 1

            while freq[ch] > 1:
                ch_lo = s[lo]
                freq[ch_lo] -= 1
                lo += 1
            
            ans = max(ans, hi-lo+1)
            hi += 1
        
        return ans
            
