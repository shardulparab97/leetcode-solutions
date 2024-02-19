class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mp = collections.defaultdict(list)

        for idx, g in enumerate(groupSizes):
            mp[g].append(idx)

        ans = []
        # print(mp)
        for k, v in mp.items():
            runs = len(v)//k
            for i in range(runs):
                ans.append(v[i*k:(i+1)*k])
        return ans