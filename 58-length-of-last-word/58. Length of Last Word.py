class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        # print(s)
        return len(s.split(" ")[-1])
        