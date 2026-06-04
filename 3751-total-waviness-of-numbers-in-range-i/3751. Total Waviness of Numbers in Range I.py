class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def get_wavy(n):
            s = str(n)
            wavy_cnt = sum( (a > b < c) or (a < b > c) for a, b, c in zip(s, s[1:], s[2:]))

            return wavy_cnt

        return sum(get_wavy(n) for n in range(max(100,num1), num2+1))