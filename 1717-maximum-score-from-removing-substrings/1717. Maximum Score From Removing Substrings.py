class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        hi_pair = "ab" if x>y else "ba"
        lo_pair = "ba" if hi_pair == "ab" else "ab"

        st_first_pass = self.remove_substring(s, hi_pair)
        removed_pairs_count = (len(s) - len(st_first_pass))//2
        ans += (removed_pairs_count * max(x, y))

        st_second_pass = self.remove_substring(st_first_pass, lo_pair)
        removed_pairs_count = (len(st_first_pass) - len(st_second_pass))//2
        ans += (removed_pairs_count * min(x, y))

        return ans


    def remove_substring(self, s, target_pair):
        st = collections.deque()
        for ch in s:
            if (ch == target_pair[1] and st and st[-1] == target_pair[0]):
                st.pop()
            else:
                st.append(ch)
        # print(st)
        
        return "".join(st)