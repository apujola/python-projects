import random

def draw_board(board):
    """
    This function prints out the board that it was passed.
    "board" is a list of 10 strings representing the board (ignore index 0).
    """
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def input_player_letter():
    """
    Lets the player type which letter they want to be.
    Returns a list with the player's letter as the first item, and the computer's letter as the second.
    """
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def who_goes_first():
    """
    Randomly chooses which player goes first.
    """
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def make_move(board, letter, move):
    """
    Function that updates the board with the player or computer's move.
    """
    board[move] = letter

def is_winner(board, letter):
    """
    Given a board and a player's letter, this function returns True if that player has won.
    """
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or 
            (board[4] == letter and board[5] == letter and board[6] == letter) or 
            (board[1] == letter and board[2] == letter and board[3] == letter) or 
            (board[7] == letter and board[4] == letter and board[1] == letter) or 
            (board[8] == letter and board[5] == letter and board[2] == letter) or 
            (board[9] == letter and board[6] == letter and board[3] == letter) or 
            (board[7] == letter and board[5] == letter and board[3] == letter) or 
            (board[9] == letter and board[5] == letter and board[1] == letter))

def get_board_copy(board):
    """
    Make a duplicate of the board list and return it.
    """
    return board[:]

def is_space_free(board, move):
    """
    Return True if the passed move is free on the passed board.
    """
    return board[move] == ' '

def get_player_move(board):
    """
    Ask the player for their move and return the index of the move.
    """
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def choose_random_move_from_list(board, moves_list):
    """
    Returns a valid move from the passed list on the passed board.
    Returns None if there is no valid move.
    """
    possible_moves = []
    for move in moves_list:
        if is_space_free(board, move):
            possible_moves.append(move)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def get_computer_move(board, computer_letter):
    """
    Given a board and the computer's letter, determine where to move and return that move.
    """
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Check if the computer can win in the next move
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    # Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])

#This function iterates through the board positions from 1 to 9 and checks if each position is 
# free by calling the is_space_free() function. If any space is found to be free, the function returns False. 
# If all the spaces are occupied, it returns True.
# #
def is_board_full(board):
    """
    Return True if every space on the board has been taken. Otherwise, return False.
    """
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


# Here the game starts #

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    the_board = [' '] * 10
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print('The ' + turn + ' will go first.')
    game_is_playing = True

    while game_is_playing:
        if turn == 'player':
            # Player's turn.
            draw_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)

            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print('Hooray! You have won the game!')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)

            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print('The computer has beaten you! You lose.')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not input('Do you want to play again? (yes or no)\n').lower().startswith('y'):
        break

              
#This code will start a new game each time the previous game ends, as long as the user types "yes" when prompted.
# If the user types anything else, the program will break out of the while loop and exit.
# #