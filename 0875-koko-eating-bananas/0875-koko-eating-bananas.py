class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, res
        while l <= r:
            k = l + ((r-l)//2)
            tim = 0
            for i in piles:
                tim += math.ceil(i/k)
            if tim <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
            
                
