class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = collections.deque()
        st.append(-1)
        n = len(s)
        ans = 0
        for i in range(n):
            ch = s[i]
            if ch == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    ans = max(ans, i - st[-1])
        return ans
