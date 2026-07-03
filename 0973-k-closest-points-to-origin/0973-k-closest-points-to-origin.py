class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    
        ans = []
        for i, j in points:
            prod = (i**2) + (j**2)
            ans.append([prod, i, j])
        heapq.heapify(ans)

        res = []
        while k > 0:
            dis, x, y = heapq.heappop(ans)
            res.append([x, y])
            k -= 1
        return res