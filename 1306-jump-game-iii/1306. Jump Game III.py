class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # vis = set()
        q = collections.deque()
        n = len(arr)

        q.append(start)
       

        while q:
            pos = q.popleft()
            # print(pos)
            # print(f"arr: {arr[pos]}")
            if arr[pos] == 0:
                return True
            if arr[pos] < 0:
                continue

            if pos + arr[pos] < n:
                q.append(pos + arr[pos])
            if pos - arr[pos] >= 0:
                q.append(pos - arr[pos])
            arr[pos] = -1
        
        return False
        