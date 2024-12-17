import random
from Hangman_words import wordList


lives = 6
chosen_Word = random.choice(wordList)

placeholder = ""
word_length = len(chosen_Word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []


while not game_over:
  guess = input("Guess a letter: ").lower()

  display = ""

  for letter in chosen_Word:

    if letter == guess:
        display += letter
        correct_letters.append(letter)

    elif letter in correct_letters:
        display += letter

    else:
        display += "_"

  print(display)

  if guess == chosen_Word:
      lives -= 1
      if lives == 0:
          game_over = True
          print("You lose!")

  if "_" not in display:
      game_over = True
      print("You win.")