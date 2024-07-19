class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        q, farthest_idx = [0], 0

        # typical BFS, but the visited flag is not required as move 
        # only in one direction
        while q:
            idx = q.pop(0)
            if idx == (n - 1):
                return True
            # ideally the range should be range(idx + minJump, min(idx + maxJump + 1, n))
            # however, since we keep moving in one direction only, we can make use of the 
            # farthest we have already explored
            for new_idx in range(max(idx + minJump, farthest_idx + 1), min(idx + maxJump + 1, n)):
                if s[new_idx] == "0":
                    q.append(new_idx)
            # this is useful for preventing memory explosion
            farthest_idx = idx + maxJump

        return False
