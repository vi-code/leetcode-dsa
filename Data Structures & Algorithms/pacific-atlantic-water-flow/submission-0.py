class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pac = set()
        atl = set()

        dir = [
            (1,0),
            (-1,0),
            (0,-1),
            (0,1)
        ]

        def dfs(r, c, visited) -> None:
            visited.add((r,c))

            for dr,dc in dir:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if (nr, nc) in visited:
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                dfs(nr,nc, visited)
        
        for c in range(cols):
            dfs(0, c, pac)
        for r in range(rows):
            dfs(r,0,pac)

        for c in range(cols):
            dfs(rows-1, c, atl)
        for r in range(rows):
            dfs(r, cols-1, atl)
        
        return list(pac & atl)