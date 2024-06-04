def solveNQueens(n: int) -> list[list[str]]:
    col = set()
    mainDiag = set()
    antiDiag = set()

    res = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):

        if r == n:
            res.append(["".join(row) for row in board])
            return
        
        for c in range(n):
            if c in col or (r-c) in mainDiag or (r+c) in antiDiag:
                continue

            col.add(c)
            mainDiag.add(r-c)
            antiDiag.add(r+c)
            board[r][c] = "Q"

            backtrack(r+1)

            col.remove(c)
            mainDiag.remove(r-c)
            antiDiag.remove(r+c)
            board[r][c]="."

    backtrack(0)
    return res

print(solveNQueens(4))