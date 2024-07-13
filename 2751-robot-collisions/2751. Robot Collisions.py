class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        st = collections.deque()
        n = len(positions)
        indices = [i for i in range(n)]
        indices.sort(key = lambda x: positions[x])


        # q will also save the time of colision if needed
        for idx in indices:
            d = directions[idx]
            if d == 'R':
                st.append(idx)
            else:
                while st and healths[idx] > 0:
                    top_idx = st.pop() 
                    if healths[top_idx] > healths[idx]:
                        healths[idx] = 0
                        healths[top_idx] -= 1
                        st.append(top_idx)
                    elif healths[top_idx] < healths[idx]:
                        healths[idx] -= 1
                        healths[top_idx] = 0
                    else:
                        healths[idx] = 0
                        healths[top_idx] = 0

        ans = []
        for idx in range(n):
            if healths[idx] > 0:
                ans.append(healths[idx])

        return ans

            
