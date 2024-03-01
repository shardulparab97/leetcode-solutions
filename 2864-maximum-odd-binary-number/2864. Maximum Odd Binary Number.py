class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        oc = s.count('1')

        n = len(s)

        return '1'*(oc-1) + '0' * (n-oc) + '1'