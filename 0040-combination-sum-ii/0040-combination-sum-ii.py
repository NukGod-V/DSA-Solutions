class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []
        def backtracking(pos: int, curr: List[int], target: int) -> None:
            if target == 0:
                res.append(curr.copy())
            if target <= 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if prev == candidates[i]:
                    continue
                curr.append(candidates[i])
                backtracking(i + 1, curr, target - candidates[i])
                curr.pop()

                prev = candidates[i]
        backtracking(0, [], target)
        return res