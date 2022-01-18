def test_board(board):
    
    print(' ' + '|' + ' ' + '|')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(' ' + '|' + ' ' + '|')
    print('---------------------')
    print(' ' + '|' + ' ' + '|')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(' ' + '|' + ' ' + '|')
    print('----------------------')
    print(' ' + '|' + ' ' + '|')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(' ' + '|' + ' ' + '|')
def player_input():
    marker=' '
    while marker!='X' and marker!='O':
        marker=input('playrer please choose between X and O::').upper()
    if marker=='X':
        return ('X','O')
    else:
        return('O','X')
def place_maker(board,marker,position):
    board[position]=marker
def win_check(board,mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark)or
           (board[4]==mark and board[5]==mark and board[6]==mark)or
           (board[1]==mark and board[2]==mark and board[3]==mark)or
           (board[7]==mark and board[4]==mark and board[1]==mark)or
           (board[8]==mark and board[5]==mark and board[2]==mark)or
           (board[9]==mark and board[6]==mark and board[3]==mark)or
           (board[7]==mark and board[5]==mark and board[3]==mark)or
           (board[9]==mark and board[5]==mark and board[1]==mark))
import random
def choose_first():
    flip=random.randint(0,1)
    if flip==1:
        return 'player1'
    else:
        return 'player2'


def space_check(board, position):
    return board[position] == " "
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    position=0
    while position not in ['1','2','3','4','5','6','7','8','9'] and not space_check(board,position):
        position=input('player please choose a number between 1 to 9:')
    return int(position)
def replay():
    choice=input('player if you want to play again please type Yes or No')
    return choice=='Yes'


print('Welcome to tik tac toe')
while True:
    display_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first')
    play_game = input('ready to play? y or n::')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'player1':
            test_board(display_board)
            position = player_choice(display_board)
            place_maker(display_board, player1_marker, position)
            if win_check(display_board, player1_marker):
                test_board(display_board)
                print('congrats player 1 you won')
                game_on = False
            else:
                if full_board_check(display_board):
                    print('ahhh! this is a tie game')
                    game_on = False
                else:
                    turn = 'player2'
        else:

            test_board(display_board)
            position = player_choice(display_board)

            place_maker(display_board, player2_marker, position)
            if win_check(display_board, player2_marker):
                test_board(display_board)
                print('congrats player 2 you won')
                game_on = False
            else:
                if full_board_check(display_board):
                    print('ahhh! this is a tie game')
                    game_on_on = False
                else:
                    turn = 'player1'
    if not replay():
        break


















