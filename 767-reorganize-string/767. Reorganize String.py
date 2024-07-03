class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        char_counts = collections.Counter(s)

        max_count, letter = 0, ''
        for ch, cnt in char_counts.items():
            if cnt > max_count:
                max_count = cnt
                letter = ch

        if max_count > (n + 1)//2:
            return ''

        ans = [''] * n

        idx = 0
        while char_counts[letter] != 0:
            ans[idx] = letter
            idx += 2
            char_counts[letter] -= 1

        for ch, cnt in char_counts.items():
            while cnt != 0:
                if idx >= len(s):
                    idx = 1
                ans[idx] = ch
                idx += 2
                cnt -= 1

        return ''.join(ans)
