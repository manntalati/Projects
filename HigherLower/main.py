from art import logo, vs
from game_data import data
import random

def randomperson():
    r = random.randint(0, len(data))
    random2 = data[r]
    return random2


def aValue(value):
    name = value['name']
    description = value['description']
    country = value['country']
    print(f"Compare A: {name}, {description}, {country}")


def bValue(value2):
    name = value2['name']
    description = value2['description']
    country = value2['country']
    print(f"Against B: {name}, {description}, {country}")


def game():
    score = 0
    endofgame = False
    aPerson = randomperson()
    bPerson = randomperson()
    while endofgame == False:
        while aPerson == bPerson:
            bPerson = randomperson()
        print(logo)
        aValue(aPerson)
        print(vs)
        bValue(bPerson)
        decision = input("Who has more followers? Type 'A' or 'B': ")
        if decision.lower() == "a":
            if aPerson['follower_count'] > bPerson['follower_count']:
                score += 1
                print(f"You\'re right! Current score {score}")
                bPerson = randomperson()
            else:
                endofgame = True

        if decision.lower() == "b":
            if bPerson['follower_count'] > aPerson['follower_count']:
                score += 1
                print(f"You\'re right! Current score {score}")
                aPerson = bPerson
                bPerson = randomperson()
            else:
                endofgame = True

    print(logo)
    print(f"Sorry, that\'s wrong. Final score: {score}")


game()