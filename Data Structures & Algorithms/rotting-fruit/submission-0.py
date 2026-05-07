class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Find initial count of fresh fruit first
        # When we find a rotten fruit
        # BFS - all directions and mark fresh fruit as rotten every loop
        #       because 1 loop is 1 minute (change 1 to 2)
        #       decrement counter of fresh fruit, increment minutes
        # Once counter reaches 0 we return number of minutes
        # if counter is not 0, return -1

        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0
        minutes = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh+=1
                if grid[row][col] == 2:
                    q.append((row,col))
        
        dir = [
            (1,0),
            (-1,0),
            (0,-1),
            (0,1)
        ]

        while q and fresh > 0:
            level = len(q)
            for _ in range(level):
                row, col = q.popleft()
                for x, y in dir:
                    if(
                        0 <= row+x < rows and
                        0 <= col+y < cols
                    ):
                        if grid[row+x][col+y] == 1:
                            grid[row+x][col+y] = 2
                            fresh-=1
                            q.append((row+x, col+y))
            minutes +=1
        if fresh == 0:
            return minutes
        return -1




















