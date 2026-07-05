class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for t in tasks:
            counts[t] = 1 + counts.get(t, 0)
        # counts = Counter(tasks)
        maxheap = [-cnt for cnt in counts.values()]
        heapq.heapify(maxheap)
        #heapq.heapify_max(+postive )

        time = 0
        q = deque()

        while q or maxheap:
            time += 1
            if maxheap:
                max_c = 1 + heapq.heappop(maxheap)
                if max_c:
                    q.append([max_c, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time