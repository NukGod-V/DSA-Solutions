class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            n = l + ((r-l)//2)
            res = min(res,nums[n])
            if nums[n] >= nums[l]:
                l = n + 1
            else:
                r = n - 1
        
        return res