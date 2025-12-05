import os 
os.system('cls' if os.name == 'nt' else 'clear')
# A program is required to create a new key.
# The program takes two inputs.
# The first input is a four-character string.
# The second input is a whole number.
# The key is constructed by joining the first two characters from the string, the number and the final two characters from the string.
# When the user enters the four-character string abcd and the integer 123, the program must construct and display the new key ab123cd.

def new_key(chara, numb):
    new_key2 = ""
    new_key2 += chara[:2]
    new_key2 += (numb)
    new_key2 += chara[2:]
    return new_key2


four_character = input("Enter a four-character string: ")
while True:
    if len(four_character) != 4:
        print('Error, to')
        four_character = input("Enter a four-character string: ")


number = input('Enter any chain of number: ')


finally_key = new_key(four_character,number)
print(finally_key)















