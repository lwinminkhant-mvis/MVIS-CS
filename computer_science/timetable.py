import os
os.system('cls')

user_number = int(input('Put a number that you want a timetable of: '))

for i in range(1,11):        
        print(f"{user_number} × {i}\t=", user_number * i)
        