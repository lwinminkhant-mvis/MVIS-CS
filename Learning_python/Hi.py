#c = 10
#for i in range(5):
    #c = c - 2
    #print(" " *i + "I" + " " *c + "I")
    





#a = 5 
#for i in range(5):
    #a = a - 1
    #print(" "*a + "I")
import random

# gap = " " *4
# space = " " 
# a = int(input("number:"))

# hello=[4,3,2,3] * a

# print(gap + "/=\\")


# for s in hello:
#     print( space * s + "[=]")

board = [
        ['0','0','0','0','0'],
        ['0','0','0','0','0'],
        ['0','0','0','0','0'],
        ['0','0','|','0','0'],
        ['0','0','0','0','0']
    ]    

import operator



math_op = {
    '+' : operator.add,
    '-' : operator.sub
}
random_chose = random.choice(math_op)
print(1,random_chose,2)




