class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        m, n = len(version1), len(version2)
        

        for i in range(min(m, n)):
            v1 = int(version1[i])
            v2 = int(version2[i])

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        if m>n:
            for i in range(n, m):
                if int(version1[i]) > 0:
                    return 1
        
        elif n>m:
            for i in range(m, n):
                if int(version2[i]) > 0:
                    return -1


        return 0 


            