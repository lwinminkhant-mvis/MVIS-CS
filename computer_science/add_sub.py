# while True:
#     first_num = input('what is the first number or type "q" or "x" to quite : ')
#     if first_num  in ['x','X','q','Q']:
#         break
#     first_num = int(first_num)
#     sec_num = int(input('What is the second number : '))

#     for i in range(1,11):
#         print(f'{first_num} + {sec_num*i} = {first_num + sec_num*i}')
#     print("")
#     for i in range(1,11):
#         print(f'{first_num} - {sec_num*i} = {first_num - sec_num*i}')

my_input = input('type some english word or a sentence:')

vowels = 'aeiouAEIOU '
consonants = 0
for i in my_input:
    if i.isalpha() and i not in vowels:
        consonants = consonants + 1


print(f'there are {consonants} in this english word or a sentence')