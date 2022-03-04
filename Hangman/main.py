import random
from hangman_words import word_list
from hangman_art import logo

end_of_game = False
chosen_word = random.choice(word_list)
lives = 6

print(logo)

display = []
for i in range(0, len(chosen_word)):
    display.append("_")

words = []
i = 0
while end_of_game == False:
    if (i != 0):
        print(f"You have already guessed these letters: {', '.join(words)}")
    guess = input("Guess a letter: ").lower()
    j = 0
    for letter in chosen_word:
        if letter == guess:
            display[j] = guess
            if (letter not in words):
                words.append(guess)
        j += 1

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