from vpython import * 
import os
import time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



place = ["0","1","2","3","4","5","6","7","8","9"]
scene.background = color.white
scene.title = '3D tic_tac_toe'

position_line = [-0.5,0.5]
grid_line = []
x_o_position = {i: [] for i in range(1,10)}


for i in range(2):
    v = box(pos= vec(position_line[i],0,0), color = color.black, size= vec(0.1,2.9,0.1) )
    x = box(pos= vec(0,position_line[i],0), color = color.black, size= vec(0.1,2.9,0.1), axis = vec(0,1,0) )
    grid_line.append(v)
    grid_line.append(x) 
position_block = [None,
                  vec(-1,1,0),vec(0,1,0),vec(1,1,0),
                  vec(-1,0,0),vec(0,0,0),vec(1,0,0),
                  vec(-1,-1,0),vec(0,-1,0),vec(1,-1,0)
                  ]

squares = {}
for a in range(1,10):
    squares[a] = box(pos= position_block[a], size = vec(0.9,0.9,0.1),color = color.white , opacity = 0
                      )


def display_board():    
    print(f"{place[1]} {place[2]} {place[3]}")
    print(f"{place[4]} {place[5]} {place[6]}")
    print(f"{place[7]} {place[8]} {place[9]}")
def check_win():
    wins = [
        [1,2,3],[4,5,6],[7,8,9],
        [1,4,7],[2,5,8],[3,6,9],
        [1,5,9],[3,5,7]
    ]
    for a,b,c in wins:
        if place[a] == place[b] == place[c]:
            return [a,b,c]
    return []
    

def check_full_board():
    for x in place[1:]:
       if x not in ["X","O"]:
           return False
    return True

def draw_X(pos,choice):
    
    p1 = box(pos=pos, size = vec(0.1,1,0.1), axis = vec(1,1,0),color = color.red)
    p2 = box(pos=pos, size = vec(0.1,1,0.1), axis = vec(-1,1,0),color = color.red)
    x_o_position[choice].append(p1)
    x_o_position[choice].append(p2)

def draw_O(pos, choice):
    o = ring(pos=pos, axis = vec(0,0,1), radius=0.35, thickness=0.05, color = color.blue)
    x_o_position[choice].append(o)
def gray_all_non_winner(winning_po):
    for i in  squares:
        if i not in winning_po:
            squares[i].color = color.gray(0.5)
            for m in x_o_position[i]:
                m.color = color.gray(0.5)
                
    for g in grid_line:
        g.color = color.gray(0.5)


        



def tic_tac_toe():
    current = "X"
    while True:
        display_board()    
        
        choice = (input("Choose a number from 1-9:\n"))
        if not  choice.isdigit() or int(choice)  not in range(1,10):
            print("Invalid choice!! (not in 1-9)")
            time.sleep(1)
            continue
        integer = int(choice)
        if choice not in place:
            print("Invalid choice!! already picked")
            time.sleep(1)
            continue
        place[integer] = current
        
        if current == 'X':
            draw_X(squares[integer].pos , integer)
        else:
            draw_O(squares[integer].pos, integer)
        
        winning_po = check_win()

        if winning_po:
            clear()
            display_board()
            print(f" player -{current}- Win")
            text(text = f'Player -{current}- win ', pos = vec(-1.7,-1.2,0.2) , color = color.green, height = 0.4)
            gray_all_non_winner(winning_po)
            break

        if check_full_board():
            clear()
            display_board()
            print("It's a drew!!")
            text(text = f"It's a drew!! ", pos = vec(-1.5,-1.2,0.2) , color = color.black, height = 0.4)
            gray_all_non_winner(winning_po)
            break

        
        if current == "O":
            current = "X"
        else:
            current = "O"





tic_tac_toe()

while True:
    rate(60)