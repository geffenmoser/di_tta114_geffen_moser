#TicTacToe

tic_tac_2d_list =[[' ', ' ', ' '] , [' ', ' ', ' '] , [' ', ' ', ' ']]
player_turn = 'X'
move_row = int
move_col = int
def display_TicTacToe_board():
    global tic_tac_2d_list
    print("***************\n")
    print(f"* {tic_tac_2d_list[0][0]} |  {tic_tac_2d_list[0][1]} | {tic_tac_2d_list[0][2]}  *\n")
    print("*___|____|___*\n")
    print(f"* {tic_tac_2d_list[1][0]} |  {tic_tac_2d_list[1][1]} | {tic_tac_2d_list[1][2]}  *\n")
    print("*___|____|___*\n")
    print(f"* {tic_tac_2d_list[2][0]} |  {tic_tac_2d_list[2][1]} | {tic_tac_2d_list[2][2]}  *\n")
    print("***************\n")

def player_input(player):
    global move_col
    global move_row
    print(f"Player {player}'s turn...")
    if player == "X":
        move_row = int(input("Enter 'X' row:"))
        move_col = int(input("Enter 'X' col:"))
    elif player == "O":
        move_row = int(input("Enter 'O' row:"))
        move_col = int(input("Enter 'O' col:"))

def check_win():
    win = False
    diag_check1 = [tic_tac_2d_list[0][0], tic_tac_2d_list [1][1], tic_tac_2d_list[2][2]]
    diag_check2 = [tic_tac_2d_list[2][0], tic_tac_2d_list [1][1], tic_tac_2d_list[0][2]]
    if diag_check1[0] == diag_check1[1] == diag_check1 [2] and diag_check1[0] != ' ':
        win = True
    elif diag_check2[0] == diag_check2[1] == diag_check2[2] and diag_check2[0] != ' ':
        win = True
    for r in tic_tac_2d_list:
        if r[0] == r[1] == r[2] and r[0] != ' ': #horizontal check
            win = True
    for col in range(3):
        if tic_tac_2d_list[0][col] == tic_tac_2d_list[1][col] == tic_tac_2d_list[2][col] and tic_tac_2d_list[0][col] != ' ':
            win = True
    print(f"win == {win}")
    return win

def play():
    global player_turn
    global tic_tac_2d_list
    display_TicTacToe_board()
    i = 0
    while i < 9:
        player_input(player_turn)
        print(f"Move made by Player {player_turn} at position ({move_row}, {move_col})")
        display_TicTacToe_board()
        if tic_tac_2d_list[move_row][move_col] != ' ':
            print("Invalid turn, spot already filled")
            continue
        else:
            tic_tac_2d_list[move_row][move_col] = player_turn
            win = check_win()
            if win is True:
                display_TicTacToe_board()
                print(f"Congratulations Player {player_turn}, you Win!!")
                break
            elif player_turn == 'X':
                player_turn = 'O'
            else:
                player_turn = 'X'
            i += 1
        display_TicTacToe_board()
    if i == 9 and win is False:
        print("It's a draw!")
play()
