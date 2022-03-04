import random
from art import rock, paper,scissors

game_images = [rock, paper, scissors]
user_signal = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(game_images[user_signal])
random_num = random.randint(0, 2)
print("\nComputer chose: \n")
print(game_images[random_num])
if ((user_signal == 0 and random_num == 0) or (user_signal == 1 and random_num == 1) or (
        user_signal == 2 and random_num == 2)):
    print("Tie! Play again!")
elif ((user_signal == 0 and random_num == 1) or (user_signal == 1 and random_num == 2) or (
        user_signal == 2 and random_num == 0)):
    print("You Lost! So dumb! Play again!")
else:
    print("You Won! So smart! Great Job!")