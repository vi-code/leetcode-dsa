class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        rows = len(grid)
        cols = len(grid[0])
        treasures = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    treasures.append((row,col))
        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]
        while treasures:
            r,c = treasures.popleft()
            
            for dr, dc in directions:
                next_row = r+dr
                next_col = c+dc

                if (
                    next_row < 0 or
                    next_row >= rows or
                    next_col < 0 or
                    next_col >= cols
                ):
                    continue
                if grid[next_row][next_col] == 2147483647:
                    grid[next_row][next_col] = grid[r][c] + 1
                    treasures.append((next_row,next_col))
