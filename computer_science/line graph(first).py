import os
#import time

os.system('cls' if os.name == 'nt' else 'clear')





char = "  "
gs = 10
for y in range(gs , -gs, -1 ):
    for x in range(-gs, gs + 1):
        char = "  "
        if y == 0 and x == 0:
            char = " +"
        elif y == 0:
            char = " -"
        elif x == 0: 
            char = " |"
        print(char, end="")
    print("")
    

























































# char =  "."
# gs = 10
# for y in range(-gs, gs+ 1 ):
#     for x in range(-gs, gs + 1 ):
#         if y == 0:
#             print(" -", end="") 
#         elif x == 0:
#             print(" |", end="")
        
#         elif x != 0:
#             print(" " + char, end ="")
#         else:
#             print(" -")

#     print("")








# for y in range(-gs, gs+ 1 ):
#     for x in range(-gs, gs + 1 ):
#         if x == 0:
#             print("|", end="") 
#         else:
#             print(char, end="")
        
#         if y == 0:
#             print("-", end="")

       
#     print("")






            





# space = "          " 
# first_space = "\t"
# print(first_space  + space + "Y")



# for y in range(10):
#     print(first_space + space + "|")
#     if y == 4:
#         print( "X", end="") 
#         print( "-"*20, end="" )
# #print( "X\t" + "----------" * 2 )