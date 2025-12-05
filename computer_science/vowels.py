word = input('type a word or a sentence: ')
vowels = ['a','e','i','o','u','A','E','I','O','U']
# vowels = 'a,e,i,o,u'
vowels_in_word = 0
found = []
# for i in range (len(word)):
#     if word[i] in vowels:
#         vowels_in_word += 1
#         # if found != "":
#         #     found += ','

#         found += word[i]

#         # if found == "":
#         #     found = word[i]
#         # else:
#         #     found = found + ", " + word[i] 

for i in word:
    if i in vowels:
        vowels_in_word += 1
        found += i 

print(vowels_in_word) 
print(",".join(found))


