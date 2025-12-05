while True:
    x = input ("Enter a letter:")
    match x:
        case "A"|"a":
            print ("You enter A.")
        case "B"|"b":
            print("You enter B.")
        case "C"|"c":
            print("You enter C.")
        case "q":
            break
        case _:
            print("You did not enter A,B or C")





# print ('''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''')

# #  1)=========

# #
# #          
# #  2)=========

a = ['1'] * 10
for i in range(len(a)):
    print(a[i],end='')

