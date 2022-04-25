from os import CLD_CONTINUED
from english_words import english_words_lower_alpha_set as complete_words
import json
from datetime import datetime

guess_word = []
guess_word_str = ''

uninclusive_word = []

print('Type `!` to stop')
for x in range(1,6):
    letter = input(f"{x} Letter: ")
    if letter == "!":
        break
    if letter.isalpha():
        guess_word.append(letter.lower())
        guess_word_str += letter.lower()
    else:
        print(f'{letter} is not a word.')
        exit(0)

print('Words NOT to include...')
print('Type `!` to stop')
while True:
    letter = input(f"Letter: ")
    if letter == "!":
        break
    if letter.isalpha():
        uninclusive_word.append(letter.lower())
    else:
        print(f'{letter} is not a word.')
        exit(0)


assumption_words = []
continue_flag = False

for word in complete_words:
    if len(word) != 5:
        continue
    counter = 0
    
    if (all(item in guess_word for item in word)):
        print(word)
        continue_flag = True

    if continue_flag:
        continue 

    for x in guess_word:
        if x not in word:
            break
        
        counter += 1
        if counter == len(guess_word):
            assumption_words.append(word)


print(assumption_words)
print(len(assumption_words))
json.dump(assumption_words, open(f'{(datetime.now()).isoformat()}-{guess_word_str}.json', 'w'))