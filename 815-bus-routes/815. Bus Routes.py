class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        bus_route_dict = collections.defaultdict(list)
        # g = collections.defaultdict(list)
        for r_idx, route in enumerate(routes):
            for stop in route:
                bus_route_dict[stop].append(r_idx)

        vis = set()
        q = collections.deque()
        q.append((source, 0))
        # vis.add(source)

        while q:
            stop, dist = q.popleft()
            # vis.add(stop)

            if stop == target:
                return dist

            for nextroute in bus_route_dict[stop]:
                if nextroute in vis:
                    continue
                vis.add(nextroute) # very important see where we are storing routes

                for stop in routes[nextroute]:
                    q.append((stop, dist+1))

        return -1

        






