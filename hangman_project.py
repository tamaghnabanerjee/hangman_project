##importing modules
import random
import figures
from replit import clear

##hangman ascii design
print(figures.logo[0])


##pick a word randomly
f = open('words.txt')
words = [word for word in f]
computer_word = random.choice(words).strip()
# print(computer_word)
f.close()

##provide dashes to user
mask = ''
for letter in computer_word:
    mask = mask + '_ ' 
    mask_list = mask.split()
print()
print(mask)
print()


##ask user to guess a letter
guess_number = 0
found_count = 0
won = False
letter_selected = []
while (guess_number) < 7:

    print()
    guess = input("Guess a letter: ").lower()
    clear()
    print(figures.logo[0])
    print()
    
    if guess in letter_selected:
        print('You have already chosen: {}, please select another one'.format(guess))
    else:
        letter_selected.append(guess)
        if guess in computer_word:
            for i in range(len(computer_word)):
                if computer_word[i] == guess:
                    mask_list[i] = computer_word[i]
                    found_count += 1
                    if found_count == len(computer_word):
                        won = True
            
            if won:
                mask = ' '.join(mask_list)
                print(mask)
                print()
                print('You won!')
                print()
                break    
        else:
            print('You guessed {}, which is not in the word'.format(guess))
            print(figures.stages[guess_number])
            guess_number += 1    

    mask = ' '.join(mask_list)
    print(mask)

if found_count < len(computer_word):
    print()
    print("You lose")
    print()
    print('The word was: {}'.format(computer_word))
    print()
