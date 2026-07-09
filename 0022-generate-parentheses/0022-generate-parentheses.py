class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        op_cl = [0, 0]
        res = []
        def backtrack(op_cl: List[int], cur: List) -> None:
            if op_cl[0] == n and op_cl[1] == n:
                res.append("".join(cur[::]))
                return
            if op_cl[0] < n:
                cur.append("(")
                op_cl[0] += 1
                backtrack(op_cl, cur)
                op_cl[0] -= 1
                cur.pop()
            if op_cl[1] < op_cl[0]:
                cur.append(")")
                op_cl[1] += 1
                backtrack(op_cl, cur)
                op_cl[1] -= 1
                cur.pop()
        backtrack(op_cl, [])
        return res
