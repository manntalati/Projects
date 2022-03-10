import random
from hangman_words import word_list
from hangman_art import logo

# chose a random word from the hangman word list
# start number of lives to 6
end_of_game = False
chosen_word = random.choice(word_list)
lives = 6

print(logo)

# display the number of spaces for the words
display = []
for i in range(0, len(chosen_word)):
    display.append("_")

words = []
i = 0
while end_of_game == False:
    # show the letters that the user has already guessed
    if (i != 0):
        print(f"You have already guessed these letters: {', '.join(words)}")
    # have the user guess a letter
    guess = input("Guess a letter: ").lower()
    j = 0
    # if the letter is in the word that has been guessed then replace the blank with the letter
    for letter in chosen_word:
        if letter == guess:
            display[j] = guess
            if (letter not in words):
                words.append(guess)
        j += 1

    # if the letter is not in the word then the user loses a life and when lives = 0 then end the game
    if guess not in chosen_word:
        lives -= 1
        words.append(guess)
        if lives == 0:
            end_of_game = True
            print("You Lose.")
            print(f"The word was {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    from hangman_art import stages

    print(stages[lives])
    i += 1
