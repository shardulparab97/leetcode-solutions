class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]

        vis = set()
        inCycle = set()
        for p in prerequisites:
            g[p[1]].append(p[0])

        def checkCycle(node):
            vis.add(node)
            inCycle.add(node)

            for nei in g[node]:
                if nei not in vis:
                    if checkCycle(nei):
                        return True
                elif nei in inCycle:
                    return True

            inCycle.remove(node)
            return False

        for i in range(numCourses):
            if i not in vis:
                if checkCycle(i) == True:
                    return False

        return True