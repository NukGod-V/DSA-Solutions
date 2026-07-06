class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []

        def dfs(i: int) -> List[int]:
            if sum(sub) == target:
                res.append(sub.copy())
                return
            if i >= len(candidates) or (sum(sub) > target):
                return
            # with next value
            sub.append(candidates[i])
            dfs(i)

            #without adding value
            sub.pop()
            dfs(i+1)
        dfs(0)
        return res