class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        rem_k = 0
        ans =[]
        vis = set()

        def get_combinations(i, vis, curr_list, rem_k):
            if rem_k == k:
                ans.append(curr_list)
                return
            
            if i > n:
                return


            # option_1
            rem_k += 1
            vis.add(i)
            get_combinations(i+1, vis, curr_list+[i], rem_k)
            vis.remove(i)
            rem_k -= 1

            get_combinations(i+1, vis, curr_list, rem_k)

        get_combinations(1, vis, [], rem_k)

        return ans

            
        

