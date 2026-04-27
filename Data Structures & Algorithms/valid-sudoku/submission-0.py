class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: int = len(board)
        cols: int = len(board[0])
        check_set: set[int] = set()

        ### Check if any row has recurring numbers
        for r in range(rows):
            check_set.clear()
            for c in range(cols):
                if board[r][c] in check_set:
                    return False
                elif board[r][c] is not ".":
                    check_set.add(board[r][c])

        ### Check if any column has recurring numbers
        for c in range(cols):
            check_set.clear()
            for r in range(rows):
                if board[r][c] in check_set:
                    return False
                elif board[r][c] is not ".":
                    check_set.add(board[r][c])
        
        ### Check every 3x3
        # Each cube is (0,0) (0,3) (0,6) .... (3,6) (6,6)
        # +2 for each cube for i,j (i+2) (j+2)
        for row_start in range(0, rows, 3):
            for col_start in range(0, cols, 3):
                print("new box: ", row_start,col_start)
                check_set.clear()
                for r in range(row_start, row_start+3):
                    for c in range(col_start, col_start+3):
                        value = board[r][c]
                        if value is ".":
                            continue
                        if value in check_set:
                            return False
                        else:
                            check_set.add(value)

        return True