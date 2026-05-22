class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        pre = 1
        pos = 1
        for i in nums:
            ans.append(pre)
            pre *= i
            
        le = len(ans) - 1
        while le > 0:
            pos *= nums[le]
            ans[le-1] *= pos
            le -= 1

        return ans