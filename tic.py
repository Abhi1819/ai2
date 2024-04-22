def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    while True:
        print_board(board)
        player = players[turn % 2]
        move = input(f"Player {player}, enter your move (row col): ")
        row, col = map(int, move.split())
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = player
        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if all([cell != " " for row in board for cell in row]):
            print_board(board)
            print("It's a tie!")
            break
        turn += 1


tic_tac_toe()
