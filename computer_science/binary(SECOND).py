import os
os.system('cls')

search_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
low_pos  = 0
high_pos = len(search_list) - 1 
mediam = 0
found = False

while True:
    my_num_t_find = int(input("Enter: "))
    low_pos  = 0
    high_pos = len(search_list) - 1 


    while True:
        mediam = int((low_pos + high_pos)/2)
        mediam_value = search_list[mediam] 

        if mediam_value == my_num_t_find:
            print('found the number')
            print('your number is ',my_num_t_find)
            print('the number possition is ',mediam)
            break

        elif low_pos == high_pos:
            print('not in list ')
            break 
        
        elif mediam_value < my_num_t_find:
            low_pos = mediam +1
            

        else:
            high_pos = mediam 
            





