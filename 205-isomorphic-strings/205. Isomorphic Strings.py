class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp1, mp2 = {}, {}
        n = len(s)

        for sc, tc in zip(s, t):
            if tc not in mp2 and sc not in mp1:
                mp2[tc] = sc
                mp1[sc] = tc
            else:
                if sc in mp1 and tc not in mp2:
                    return False
                elif sc not in mp1 and tc in mp2:
                    return False
                elif mp2[tc] != sc:
                    return False


        return True

        