
board = [" "]*9


winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
]
def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def board_full():
       return " " not in board

def check_winner(player):
    for combination in winning_combinations:
        if (board[combination[0]] == player and
            board[combination[1]] == player and
            board[combination[2]] == player):
            return True

    return False

player = "X"


while True:
    
        display_board()

        position = int(input(f"Player {player},enter position (1-9): ")) - 1

        if position < 0 or position > 8:
            print("Invalid position! Enter a number from 1 to 9")
            continue

        if board[position] != " ":
            print("Position already occupied.Try again")
            continue

        board[position] = player

        if check_winner(player):
            display_board()
            print("Player", player, "wins!")
            break

        if board_full():
            display_board()
            print("It's a draw!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"



