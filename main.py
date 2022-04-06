from english_words import english_words_lower_alpha_set as complete_words

guess_word = []

print('Type `!` to stop')
for x in range(1,6):
    letter = input(f"{x} Letter: ")
    if letter == "!":
        break
    if letter.isalpha():
        guess_word.append(letter.lower())
    else:
        print(f'{letter} is not a word.')
        exit(0)

assumption_words = []

for word in complete_words:
    if len(word) != 5:
        continue
    counter = 0
    for x in guess_word:
        if x not in word:
            break
        
        counter += 1
        if counter == len(guess_word):
            assumption_words.append(word)


print(assumption_words)
print(len(assumption_words))