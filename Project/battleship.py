import os
import random
from colorama import Fore, Back, Style, init
os.system('cls')



# board_real = [
#         ['██','██','██','██','██'],
#         ['██','██','██','██','██'],
#         ['██','██','██','██','██'],
#         ['██','██','██','██','██'],
#         ['██','██','██','██','██']
# ]

# board_fake = [
#         ['██','██','██','██','██'],
#         ['██','██','██','██','██'],
#         ['██','██','██','██','██'],
#         ['██','██','██','██','██'],
#         ['██','██','██','██','██']
# ] 
board_real = []
board_fake = []

ocean = "█"
grid_size = 4
for row in range(grid_size+1):
    row_chars = []
    for col in range(grid_size+1):
        row_chars.append(ocean)
    board_real.append(row_chars)
    board_fake.append(row_chars)


def place():
    global ship_row,ship_col
    ship_row = random.randint(0,grid_size -1)
    ship_col = random.randint(0,grid_size -1)
    if ship_row == 5:
        board_real[ship_row][ship_col] = '_'
        board_real[ship_row][ship_col - 1] = '_'
    else:
        board_real[ship_row][ship_col ] = '|'
        board_real[ship_row + 1][ship_col ] = '|'
    # board.append(ship_row + ship_col + )         
place()
        
def dis_board():
        print(Back.BLACK + Fore.GREEN+ '  0 1 2 3 4')
        for i in range(0,5):
            print((Fore.GREEN + str(i)) , Fore.WHITE + ''.join(board_fake[i]))
        print()
        print(Fore.GREEN+ '  0 1 2 3 4')
        for row in range(0,5):
            for col in range(0,5):
                
                char = board_real[row][col]
                if ocean in char:
                    color = Fore.BLUE
                elif char == "X":
                    color = Fore.RED
                else:
                    color = Fore.WHITE
                if len(char) == 1:
                    char = char + " "
                if col == 0:
                    print((Back.BLACK + Fore.GREEN + str(row) + " "), end="")
            
                print(Back.BLUE + Fore.RED + char,end="")
            print(Back.RESET + Fore.RESET)
        
        

dis_board()
while True:
    try:
        intput_row = int(input('Row: '))
        intput_col = int(input('Column: '))
        # if intput_row or intput_col > 4:
        #      continue
    except:
        continue
    
    if  board_real[intput_row][intput_col] == '|':
        board_fake[intput_row][intput_col] = "X"
        board_real[intput_row][intput_col] = "X"
        dis_board()
        print('hit')
    else:
        print("NOOO")
        dis_board()

    all_hit_y_n = True

    for row in board_real:
         if "|" in row:
              all_hit_y_n = False
              break
    if all_hit_y_n:
         print('win') 
         break



# import os
# import random
# from colorama import Fore, Back, Style, init
# os.system('cls')
# board = [
#         ['██','██','██','██','██'],
#         ['██','██','██','██','██'],
#         ['██','██','██','██','██'],
#         ['██','██','██','██','██'],
#         ['██','██','██','██','██']
#     ]
# def place():
#     global ship_row,ship_col
#     ship_row = random.randint(0,4)
#     ship_col = random.randint(0,4)
#     board[ship_row][ship_col] = '|'
#     if ship_row == 4:
#          board[ship_row][ship_col - 1] = '|'
#     else:
#         board[ship_row + 1][ship_col ] = '|'
         
        
# place()
# def dis_board():
#         print(Fore.GREEN+ '  0 1 2 3 4')
#         for i in range(0,5):
#             print((Fore.GREEN + str(i)) , Fore.WHITE + ' '.join(board[i]))

# dis_board()
# while True:
#     try:
#         intput_row = int(input('Row: '))
#         intput_col = int(input('Column: '))
#     except:
#          continue
    
#     if board[intput_row][intput_col] == '|':
#         board[intput_row][intput_col] = "X"
#         dis_board()
#         print('found')
#     else:
#         print("NOOO")
#         dis_board()

#     for row in board:
         

