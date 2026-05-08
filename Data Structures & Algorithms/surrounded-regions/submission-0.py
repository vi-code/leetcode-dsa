class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        queue = deque()

        dirs = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]
        def bfs(row,col) -> None:
            queue.append((row,col))
            board[row][col] = "S"
            while queue:
                r,c = queue.popleft()
                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c

                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue
                    if board[nr][nc] != "O":
                        continue
                    
                    board[nr][nc]= "S"
                    queue.append((nr,nc))

        for r in range(rows):
            if board[r][0] == "O":
                bfs(r,0)
            if board[r][cols-1] == "O":
                bfs(r,cols-1)
        for c in range(cols):
            if board[0][c] == "O":
                bfs(0,c)
            if board[rows-1][c] == "O":
                bfs(rows-1,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"