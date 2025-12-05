import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



startin_place = ['','1','2','3','4','5','6','7','8','9']
place = startin_place

def display_board():    
    print(f"{place[1]} {place[2]} {place[3]}")
    print(f"{place[4]} {place[5]} {place[6]}")
    print(f"{place[7]} {place[8]} {place[9]}")

def check_win():
    wins = [
        [1,2,3],[4,5,6,],[7,8,9], # row
        [1,4,7],[2,5,8],[3,6,9],  # colum
        [1,5,9],[3,5,7]           # diagonal
        
    ]
    for a,b,c in wins:
        if place[a] == place[b] == place[c]:
            return True
    return False

def check_full_board():
    for x in place[1:]:
       if x not in ["X","O"]:
           return False
    return True

def tic_tac_toe():
    clear()
    current = "X"
    while True:
        clear()
        display_board()    
        
        choice = (input("Choose a number from 1-9:\n"))
        if not  choice.isdigit() or int(choice)  not in range(1,10):
            print("Invalid choice!! (not in 1-9)")
            time.sleep(1)
            continue
        integer = int(choice)
        if integer not in place:
            print("Invalid choice!! already picked")
            time.sleep(1)
            continue
        place[integer] = current
        
        
        if check_win():
            clear()
            display_board()
            print(f" player -{current}- Win")
            break

        if check_full_board():
            clear()
            display_board()
            print("It's a drew!!")
            break

        
        if current == "O":
            current = "X"
        else:
            current = "O"

        



def main():
    clear()
    question = input("Do you want to play tic tac toe \n(1)Yes (2)No\n")
    while True:
        for i in range(0,10):
            place[i] = i        # place = startin_place
        if question == "1":
            tic_tac_toe()
            again = input("\nPlay again? (y/n)")
            if again != "y":
                print("Bye Bye")
                break


        elif question == "2":
            print("Bye Bye")
            break
        else:
            print("Invalid choice")
            continue

        

    
main()