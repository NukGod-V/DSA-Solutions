class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        dist = []
        l, r = 0, len(height) - 1
        while l < r:
            arr = min(height[l], height[r]) * (r - l)
            if arr > ans:
                ans = arr
            if height[l] > height[r]:
                r -= 1
                continue
            elif height[l] < height[r]:
                l += 1
                continue
            elif height[l+1] > height[r-1]:
                l += 1
                continue
            else:
                r -= 1
                continue
        return ans