class Solution:
    def trap(self, height: List[int]) -> int:
        traped = 0
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        while l < r:
            if maxl < maxr:   
                l += 1
                maxl = max(height[l],maxl)  
                traped += maxl - height[l]
            else:
                r -= 1
                maxr = max(height[r],maxr)
                traped += maxr - height[r]
        return traped