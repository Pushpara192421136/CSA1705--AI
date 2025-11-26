def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()
def check_win(board, player):
    return any(all(cell==player for cell in row) for row in board) or \
           any(all(board[r][c]==player for r in range(3)) for c in range(3)) or \
           all(board[i][i]==player for i in range(3)) or \
           all(board[i][2-i]==player for i in range(3))
board = [[" "]*3 for _ in range(3)]
players = ["X","O"]
turn = 0
while True:
    print_board(board)
    r,c = map(int,input(f"Player {players[turn%2]} enter row,col (0-2): ").split(","))
    if board[r][c]==" ":
        board[r][c] = players[turn%2]
        if check_win(board, players[turn%2]):
            print_board(board)
            print(f"Player {players[turn%2]} wins!")
            break
        if all(cell!=" " for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break
        turn += 1
    else:
        print("Cell occupied, try again.")
