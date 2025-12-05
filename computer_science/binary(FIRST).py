search_list = [10,11,12,13,14,15,16,17,18,19]
low_pos = 0
high_pos = len(search_list) - 1
median_pos = 0
found = False
# print(''.join(search_list))
find_value =20
possibly_in_list = True

 #input(f'type something from this list:')

while not found and possibly_in_list:
    median_pos = int((low_pos + high_pos)/2)
    if low_pos == high_pos:
          print('not in list')
          possibly_in_list = False

    median_value = search_list[median_pos]
    
    if find_value == median_value:
        print("found")
        print("position",median_pos,'in list')
        found = True
    elif find_value < median_value: 
        high_pos = median_pos-1
    else:
         low_pos = median_pos +1
    # if find_value != median_va lue:
    #         if find_value < median_value: 
    #                 high_pos = median_pos-1
    #         else :
    #             low_pos = median_pos + 1
    
    # else:
    #     print("found")
    #     print("position",median_pos,'in list')
    #     found = True
    
#--------------------------------------------------------------------------------------------------------------------------


