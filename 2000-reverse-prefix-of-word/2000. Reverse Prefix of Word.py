class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx != -1:
            p1 = word[0:idx+1]
            p1 = p1[::-1]
            ans = p1 + word[idx+1:]
        else:
            ans = word

        return ans