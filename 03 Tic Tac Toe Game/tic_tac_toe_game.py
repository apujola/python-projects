#/******************************************************************************************************
#This code defines several functions:

#print_board: takes in a list representing the game board and prints it to the console.
#get_move: prompts the current player for their move and returns it as an integer (with input validation).

#check_win: takes in a list representing the game board and checks whether there is a winner.

#play_game: main game loop that initializes the game board, players, and current player, 
# and then loops until there is a winner or a tie.

#To play the game, simply call the play_game function.
#******************************************************************************************************/

def print_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-|-|-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-|-|-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def get_move(player, board):
    valid_move = False
    while not valid_move:
        move = input(f"{player}, please enter your move (1-9): ")
        try:
            move = int(move)
            if move < 1 or move > 9:
                print("Move must be between 1 and 9")
            elif board[move-1] != " ":
                print("That space is already occupied")
            else:
                valid_move = True
        except ValueError:
            print("Invalid input. Please enter a number.")
    return move

def check_win(board):
    # check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True
    # check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True
    # check diagonals
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    # no win
    return False

def play_game():
    board = [" "] * 9
    players = ["X", "O"]
    current_player = players[0]
    while not check_win(board) and " " in board:
        print_board(board)
        move = get_move(current_player, board)
        board[move-1] = current_player
        if current_player == players[0]:
            current_player = players[1]
        else:
            current_player = players[0]
    print_board(board)
    if check_win(board):
        print(f"{current_player} wins!")
    else:
        print("It's a tie.")

play_game()