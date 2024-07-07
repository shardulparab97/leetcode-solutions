class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for _ in range(numCourses)]

        for p in prerequisites:
            g[p[1]].append(p[0])

        vis = set()
        inCycle = set()

        st = collections.deque()

        def isCycle(node):
            vis.add(node)
            inCycle.add(node)
            
            for nei in g[node]:
                if nei not in vis:
                    if isCycle(nei):
                        return True
                elif nei in inCycle:
                    return True

            st.appendleft(node)
            inCycle.remove(node)
            return False

        for i in range(numCourses):
            if i not in vis: 
                if isCycle(i):
                    return []

        return st