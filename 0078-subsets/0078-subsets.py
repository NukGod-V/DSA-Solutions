class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i: int) -> List[int]:
            if i >= len(nums):
                res.append(subset.copy())
                return
            # option 1 include
            subset.append(nums[i])
            dfs(i+1)

            # option 2 do not include
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res