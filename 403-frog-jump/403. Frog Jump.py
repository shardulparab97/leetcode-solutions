class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {}
        if 1 not in stones:
            return False
        n = max(stones)
        isStone = set(stones)
        

        def solve(idx, jump_val):
            if idx == n:
                return True
            if idx >n:
                return False
            if (idx, jump_val) in dp:
                return dp[(idx, jump_val)]

            op1, op2, op3 = False, False, False

            if idx + jump_val <= n and idx+jump_val in isStone:
                op1 = solve(idx+jump_val, jump_val)
            
            if jump_val-1 > 0 and idx + jump_val-1 <= n and idx+jump_val-1 in isStone:
                op2 = solve(idx+jump_val-1, jump_val-1)
            
            if idx + jump_val+1 <= n and idx+jump_val+1 in isStone:
                op3 = solve(idx+jump_val+1, jump_val+1)

            dp[(idx, jump_val)] = op1 or op2 or op3
            return dp[(idx, jump_val)]

        return solve(1, 1)


            
            
