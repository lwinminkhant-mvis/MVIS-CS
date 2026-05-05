import os 
os.system('cls')


two_letter_word = input('give 2 letter word: ')

while len(two_letter_word) != 2:
    print('error') 
    two_letter_word = input('give 2 letter word: ')
    


whole_number = input('give an whole number: ')

decimal_number = str(int(float(input('give an decimal_number: '))))


print(whole_number + two_letter_word[1] + two_letter_word[0] + decimal_number)