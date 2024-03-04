class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        lo, hi = 0, n-1
        tokens.sort()

        score = 0

        while lo <= hi:
            if power >= tokens[lo]:
                score += 1
                power -= tokens[lo]
                lo += 1

            elif lo<hi and score >0: # because we still want a score from somewhere hence lo<hi and not lo<=hi
                score -=1
                power += tokens[hi]
                hi -= 1
            
            else:
                return score

        return score
                

        