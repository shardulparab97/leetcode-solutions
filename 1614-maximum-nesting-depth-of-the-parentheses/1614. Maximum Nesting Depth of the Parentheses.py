class Solution:
    def maxDepth(self, s: str) -> int:
        st = collections.deque()
        ans = float("-inf")
        for c in s:
            if c == "(":
                st.append(c)
                ans = max(ans, len(st))
            elif c == ")":
                st.pop()
            else:
                continue

        return ans if ans != float("-inf") else 0


        