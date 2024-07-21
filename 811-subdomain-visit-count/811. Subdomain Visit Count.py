class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomains = collections.defaultdict(int)

        for cpdomain in cpdomains:
            cnt, cpdomain = cpdomain.split(" ")
            cnt = int(cnt)

            curr_domain = ""
            for cp in reversed(cpdomain.split(".")):
                curr_domain = cp + f".{curr_domain}" if curr_domain != "" else cp
                subdomains[curr_domain] += cnt
        # print(subdomains)
        ans = []
        for sd in subdomains:
            ans.append(f"{subdomains[sd]} {sd}")

        return ans