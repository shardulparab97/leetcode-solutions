class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_ptr, t_ptr = 0, 0
        l_s, l_t = len(s), len(t)
        # ans = 0
        while s_ptr < l_s  and t_ptr < l_t :
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
                t_ptr += 1
            else:
                s_ptr += 1

        # print(s_ptr)
        # print(t_ptr)
        if t_ptr == l_t:
            return 0
        else:
            return l_t - t_ptr 