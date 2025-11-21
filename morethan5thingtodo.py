import os 
import time 
os.system('cls' if os.name == 'nt' else 'clear')
# from colorama import Fore, Back, Style


# t = 4



# if t == 1:
#     a = input("What is your favourite character ? :")
#     print("Your favourite character is " + a )
# #______________________________________________________________________________________________|

# if t == 2:
#     first_name = input("What is your first name? ") 
#     time.sleep (0.5)
#     print("So your first name is " + first_name)
#     time.sleep (1)
#     last_name = input("What is your last name than? ")
#     time.sleep (0.5)
#     print(f"So your last name is {last_name}.")
#     time.sleep (1.5)
#     print("Then your full name must be ")
#     time.sleep (0.5)
#     dot = 1
#     for i in range(3):
#         time.sleep (1)
#         print(dot)
#         dot = dot + 1
#     time.sleep (0.5)
#     print(first_name + last_name)
# #_______________________________________________________________________________________________|

# if t == 3:
#     number = input("Guess a number between 1 - 10, \nif you get it right it will say True ")
#     if number == int(2): 
#         print("True")
#     elif number != int(2):
#         print("ture")
# #_______________________________________________________________________________________________|
# if t == 4:
#     print(""" lk;jafl;kjkfsal;kjf sl;kdj flsdj salkjf
#           as fd;l das jfdsla;j fsdla; jf;lasd j""")



# PI = 3.14159265359
# find_radius  = 1

# while  find_radius != 0:
#     find_radius  = int(input("What is the radius of the circle : "))
#     radius = find_radius * find_radius  
#     area_of_circle = PI * radius
#     print(area_of_circle)
    
    
# n = input()
    
# for i in range (0,n):
#     print(i**2)
    
# print(65 + 92)

# for i in range(15):
#     print("#",end="")

# print("")
# for i in range(5):
#     for x in range (5):
#         print(" #",end="")
#     print("")

# simbol  = "#"
# for i in range (15):
#     print(simbol)
#     simbol = simbol + "#"



square = int(input("square:"))
for y in range(-square , square +1 ):
    hash = " "
    for x in range(-square , square +1 ):
        if y == -square or y == square or x == -square or x==square:
            hash = hash + " #"
        else:
            hash = hash + "  "
    print(hash)    
print()