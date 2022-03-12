from art import logo, vs
from game_data import data
import random

# this function chooses a random dataset to take from the given data from game_data
def randomperson():
    r = random.randint(0, len(data))
    random2 = data[r]
    return random2


# this function uses the dictionary inputted into function and output the separate values
def aValue(value):
    name = value['name']
    description = value['description']
    country = value['country']
    print(f"Compare A: {name}, {description}, {country}")


# this function uses the dictionary inputted into function and output the separate values
def bValue(value2):
    name = value2['name']
    description = value2['description']
    country = value2['country']
    print(f"Against B: {name}, {description}, {country}")


def game():
    score = 0
    endofgame = False
    # get two random datasets and store them as a person to use later to compare
    aPerson = randomperson()
    bPerson = randomperson()
    while endofgame == False:
        # make sure that the datasets don't equal each other
        while aPerson == bPerson:
            bPerson = randomperson()
        print(logo)
        aValue(aPerson)
        print(vs)
        bValue(bPerson)
        decision = input("Who has more followers? Type 'A' or 'B': ")
        # check whether the user has guessed a or b
        if decision.lower() == "a":
            # check if the user is correct with their guess
            if aPerson['follower_count'] > bPerson['follower_count']:
                score += 1
                print(f"You\'re right! Current score {score}")
                # replace the bvalue with a new data_set
                bPerson = randomperson()
            else:
                endofgame = True

        # if the user guessed b there is a slightly different process
        if decision.lower() == "b":
            if bPerson['follower_count'] > aPerson['follower_count']:
                score += 1
                print(f"You\'re right! Current score {score}")
                # assign the avalue to be the bvalue to flip the values over
                # assign the bvalue to another random data_set
                aPerson = bPerson
                bPerson = randomperson()
            else:
                endofgame = True

    print(logo)
    print(f"Sorry, that\'s wrong. Final score: {score}")


game()
