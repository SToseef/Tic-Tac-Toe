import os, time

# v The main board and reference v
def display_board():
    print('\n Board   # Reference:')
    print(f"|{board[1]}|{board[2]}|{board[3]}|  #  |1|2|3| \n"
    f"|{board[4]}|{board[5]}|{board[6]}|  #  |4|5|6| \n"
    f"|{board[7]}|{board[8]}|{board[9]}|  #  |7|8|9|     \n\n")

board = {1:'1',2:'2',3:'3',4:'4',5:'5', 6:'6', 7:'7', 8:'8',9:'9'}

# User picks number on board
def human_input(mark):
    while True:
        inp = input(f"[PLAYER] '{mark}' Enter your choice: ")
        if inp.isdigit() and int(inp) <10 and int(inp) >0:
            inp = int(inp)
            if board[inp] == " ":
                return inp
            else:
                print(f"[PLAYER] '{mark}' place already taken.")
        else:
            print(f"[PLAYER] '{mark}' Enter valid option (1 - 9).")

# Defines winning spots in horizontal, vertical, & diagonal
def winning(mark,board):
    winning_place = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == mark:
            return True


def win_move(i,board,mark):
    temp_board = list(board)
    temp_board[i] = mark
    if winning(mark,temp_board):
        return True
    else:
        return False


def cpu_input(cpu , human , board):
    for i in range(1,10):
        if board[i] == ' ' and win_move(i,board,cpu):
            return i
    for i in range(1,10):
        if board[i] == ' ' and win_move(i,board,human):
            return i
    for i in [5,1,7,3,2,9,8,6,4]:
        if board[i] == ' ':
            return i

# Restarts game
def new_game():
    while True:
        nxt = input('\n[PLAYER] Would you like to go for another round or just end this game?(y/n): ')
        if nxt in['y','Y']:
            again = True
            break
        elif nxt in ['n','N']:
            print('\nHave a nice life.\n')
            again = False
            break
        else:
            print('Enter correct input')
    if again:
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n____________________NEW GAME____________________\n')
        main_game()
    else:
        return False

#Checks board for win
def win_check(human , cpu):
    winning_place = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == human:
            print('\n[PLAYER] wins the match!')
            if not new_game():
                return False
        elif board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == cpu:
                print('\n[CPU] wins the match!')
                if not new_game():
                    return False
    if ' ' not in board:
        print('\nMATCH DRAW!!')
        if not new_game():
            return False
    return True

# User selects X or O 
def user_choice():
    while True:
        inp = input('[PLAYER] Welcome to Tic-Tac-Toe game, please choose your letter [x/o]: ')
        if inp in ['x' , 'X']:
            print('\n[PLAYER]You choose "X".\n[PLAYER]You play first.')
            return 'x','o'
        elif inp in ['O','o']:
            print('\n[PLAYER] You choose "O".\n[PLAYER] CPU plays first.')
            return 'o','x'
        else:
            print('\n[PLAYER] Enter correct input!')

#Main game
def main_game():
    global board
    play = True
    board =['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    human , cpu = user_choice()
    display_board()
    while play:
        if human == 'x':
            x = human_input(human)
            board[x] = human
            display_board()
            play = win_check(human , cpu)
            if play:
                o = cpu_input(cpu , human , board)
                print(f'[CPU] Entered:{o}')
                board[o] = cpu
                os.system('cls' if os.name == 'nt' else 'clear')
                display_board()
                play = win_check(human , cpu)
        else:
            x = cpu_input(cpu , human , board)
            print(f'[CPU] Entered:{x}')
            board[x] = cpu
            display_board()
            play = win_check(human , cpu)
            if play:
                o = human_input(human)
                board[o] = human
                os.system('cls' if os.name == 'nt' else 'clear')
                display_board()
                play = win_check(human , cpu)

           
if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    main_game()
