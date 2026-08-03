class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diago = set()
        neg_diago = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtracking(r: int):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (c+r) in pos_diago or (r-c) in neg_diago:
                    continue
                cols.add(c)
                pos_diago.add(c + r)
                neg_diago.add(r - c)
                board[r][c] = "Q"

                backtracking(r + 1)

                cols.remove(c)
                pos_diago.remove(c + r)
                neg_diago.remove(r - c)
                board[r][c] = "."
        backtracking(0)
        return res

