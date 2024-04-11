#TicTacToe

tic_tac_2d_list =[['', '', ''] , ['', '', ''] , ['', '', '']]
player_turn = 'X'
move_row = int
move_col = int
def display_TicTacToe_board():
    print("***************\n")
    print(f"*  {tic_tac_2d_list[0][0]} |  {tic_tac_2d_list[0][1]} | {tic_tac_2d_list[0][2]}  *\n")
    print("*---|---|---*\n")
    print(f"*  {tic_tac_2d_list[1][0]} |  {tic_tac_2d_list[1][1]} | {tic_tac_2d_list[1][2]}  *\n")
    print("*---|---|---*\n")
    print(f"*  {tic_tac_2d_list[2][0]} |  {tic_tac_2d_list[2][1]} | {tic_tac_2d_list[2][2]}  *\n")
    print("***************\n")

def player_input(player):
    global move_col
    global move_row
    print(f"Player {player}'s turn...")
    if player == "X":
        move_row == int(input("Enter 'X' row:"))
        move_col == int(input("Enter 'X' col:"))
    elif player == "O":
        move_row == int(input("Enter 'O' row:"))
        move_col == int(input("Enter 'O' col:"))
    display_TicTacToe_board()

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
    i = 0
    while i < 3: #vertical check
        if tic_tac_2d_list[0][i] == tic_tac_2d_list[1][i] == tic_tac_2d_list[2][i] and tic_tac_2d_list[1][i] != '':
            win = True
        i += 1
    return win
def play():
    global player_turn
    display_TicTacToe_board()
    win = check_win()
    i = 0
    while win == False and i <= 9:
        display_TicTacToe_board()
        player_input(player_turn)
        if tic_tac_2d_list[move_row][move_col] != '':
            print("Invalid turn, spot already filled")
            continue
        else:
            tic_tac_2d_list[move_row][move_col] = player_turn
            if player_turn == 'X':
                player_turn = '0'
            elif player_turn == 'O':
                player_turn = 'X'
            i += 1
    if win == True:
        print(f"Congratulations Player {player_turn}, you Win!!")
play()
