class Solution:
    def makeGood(self, s: str) -> str:
        def check_case(ch1, ch2):
                if ch1.islower() and ch2.isupper() and ch1 == ch2.lower():
                    return True
                return False
        def give_good(st):
            idx = 0
            n = len(st)
            res = ""
            

            while idx < n:
                if idx<n-1 and (check_case(st[idx], st[idx+1]) or check_case(st[idx+1], st[idx])):
                            idx += 2
                else:
                    res += st[idx]
                    idx += 1
            return res

        ans = s
        while True:
            ans2 = give_good(ans)
            # print(ans2)
            if ans2 == ans:
                ans = ans2
                break
            ans = ans2
        return ans

        