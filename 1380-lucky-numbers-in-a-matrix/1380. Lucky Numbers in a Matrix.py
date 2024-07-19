class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        r, c = len(matrix), len(matrix[0])

        min_rows = collections.defaultdict(int)
        max_cols =  collections.defaultdict(int)

        for i in range(r):
            min_rows[i] = min(matrix[i])

        for i in range(c):
            max_cols[i] = max([matrix[j][i] for j in range(r)])

        # print(min_rows)
        # print(max_cols)
        ans = []
        for i in range(r):
            for j in range(c):
                if min_rows[i] == max_cols[j]:
                    ans.append(min_rows[i])

        return ans

