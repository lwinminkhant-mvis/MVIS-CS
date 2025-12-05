

import os
import time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

guess_word ="apple"# input('Put a guess word: ')
clear()
word = []

guess_chance = ['0'] * 9
for letter in range(len(guess_word)):
    word.append('_')

a = 0

hangman_drawing = ['''
     
     
    
                     
   
_________''','''
     
    |   
    |  
    |               
    |   
____|_____''','''
     ___
    |   
    |  
    |                
    |   
____|_____''','''
     ___
    |   |
    |          
    |                
    |   
____|_____''','''
     ___
    |   |
    |  🙂
    |                
    |   
____|_____''','''    
     ___
    |   |
    |  😐
    |   |           
    |   
____|_____''','''    
     ___
    |   |
    |  😦
    |   |\\         
    |   
____|_____''','''    
     ___
    |   |
    |  😨
    |  /|\\         
    |   
____|_____''','''     
     ___
    |   |
    |  😰
    |  /|\\         
    |    \\
____|_____''','''  
     ___
    |   |
    |  😵
    |  /|\\         
    |  / \\
____|_____''']



while True:
    
    guess_letter = input('guess a letter or word: ')
    if '_' not in (word) or guess_letter == guess_word:
        print('\nWIN')
        print('''                   ___
                  |   |🔥
                  |          
                  |🔥     \\😁/      
                🔥|         |
              ____|_____   / \\ ''')
        print(f"The word is {guess_word}")
        break


    
    # if guess_letter == guess_word :
    #     print('win')
    #     print(guess_word)
    #     break
    

    if guess_letter in guess_word:
        clear()
        for i in range(len(guess_word)):
            if guess_word[i] == guess_letter:
                word[i] = guess_letter  
        
        for l in range(len(word)):
            print(word[l],end='')
        print(hangman_drawing[a])
        
    elif len(guess_letter) > 1 and guess_letter != guess_word:
        print('nooooooooo')

    else:
        clear()
        if a == 9:
            print("game over")
            break

        for l in range(len(word)):
            print(word[l],end='')
        
        print()
        print(hangman_drawing[a])
        a += 1
        print('letter not in word')
        print(f'you have {10 - a} chance left')


        
    print()
    



    



    print()