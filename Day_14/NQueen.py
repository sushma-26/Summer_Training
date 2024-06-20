#NQueen with rook elephant 
'''def is_safe(board, row, col, N):
    # Check if the row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens_util(board, col, N,c):
    if col >= N:
        return c
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            c=c+1
            if solve_nqueens_util(board, col + 1, N,c):
                return True
            board[i][col] = 0
            c=c-1
    return False


def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
N=8
board = [[0] * N for _ in range(N)]
print(solve_nqueens_util(board, 0, N,0))
print_board(board)'''
#check once right or not
n = 6
col = []
posdia = []
negdia = []
board = [["."] * n for _ in range(n)]
rooki=0
rookj=5
def nqueen(r, n, c1):
    if r == n:
        return c1

    if r == rooki:
        return nqueen(r + 1, n, c1)
    max_queens = c1
    for c in range(n):
        if c in col or (r + c) in posdia or (r - c) in negdia or c == rookj:
            continue
        board[r][c] = "Q"
        col.append(c)
        posdia.append(r + c)
        negdia.append(r - c)
        max_queens = max(max_queens, nqueen(r + 1, n, c1 + 1))
        board[r][c] = '.'
        col.remove(c)
        posdia.remove(r + c)
        negdia.remove(r - c)
    max_queens = max(max_queens, nqueen(r + 1, n, c1))
    return max_queens

print(nqueen(0, n, 0))
