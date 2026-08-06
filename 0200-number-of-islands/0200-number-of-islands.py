class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        island = 0

        def bfs(r: int, c: int) -> None:
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    if ((row + dr) in range(rows) and
                        (col + dc) in range(cols) and
                        grid[row + dr][col + dc] == "1" and 
                        (row + dr, col + dc) not in visited):

                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    island += 1
        return island       
        
