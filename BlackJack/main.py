import random
from art import logo

card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print(logo)

user_cards = []
computer_cards = []
user_score = 0
computer_score = 0


def blackjack():
    if user_score == 21 or computer_score == 21:
        if user_score == 21 and computer_score != 21:
            return True
        elif user_score != 21 and computer_score == 21:
            return False
        elif user_score == 21 and computer_score == 21:
            return False


if decision == 'y':
    random1 = random.randint(0, 11)
    random2 = random.randint(0, 11)
    random3 = random.randint(0, 11)
    random4 = random.randint(0, 11)
    user_cards.append(card_deck[random1])
    user_cards.append(card_deck[random2])
    computer_cards.append(card_deck[random3])
    computer_cards.append(card_deck[random4])
    user_score = card_deck[random1] + card_deck[random2]
    computer_score = card_deck[random3] + card_deck[random4]

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {card_deck[random3]}")

    blackjack()

    if user_score > 21:
        aceincards = False
        for card in user_cards:
            if card == 11:
                aceincards = True

        if aceincards:
            modifiedscore = user_score - 11 + 1
            user_cards.remove(11)
            user_cards.append(1)
            if modifiedscore > 21:
                pass
            else:
                user_score = modifiedscore

    decision2 = input("Type 'y' to get another card, type 'n' to pass: ")
    while decision2 == 'y' and not blackjack():
        random5 = random.randint(0, 11)
        user_cards.append(card_deck[random5])
        user_score += card_deck[random5]
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {random3}")
        if blackjack():
            break
        else:
            if user_score > 21:
                aceincards = False
                for card in user_cards:
                    if card == 11:
                        aceincards = True
                if aceincards:
                    modifiedscore = user_score - 11 + 1
                    if modifiedscore > 21:
                        break
                    else:
                        user_score = modifiedscore
                else:
                    break
            else:
                decision2 = input("Type 'y' to get another card, type 'n' to pass: ")

computer_bust = False
while computer_score < 17:
    random6 = random.randint(0, 11)
    computer_cards.append(card_deck[random6])
    computer_score += card_deck[random6]
    if computer_score > 21:
        aceincards = False
        for card in computer_cards:
            if card == 11:
                aceincards = True

        if aceincards:
            modifiedscore = user_score - 11 + 1
            computer_cards.remove(11)
            computer_cards.append(1)
            if modifiedscore < 21:
                computer_score = modifiedscore
    if computer_score > 21 and user_score <= 21:
        computer_bust = True

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer\'s final hand: {computer_cards}, final score: {computer_score}")
if user_score > 21 and computer_score > 21:
    print("You went over. You lose 😤")
elif user_score == computer_score:
    print("Draw 🙃")
elif computer_score == 0:
    print("Lose, opponent has Blackjack 😱")
elif user_score == 0:
    print("Win with a Blackjack 😎")
elif user_score > 21:
    print("You went over. You lose 😭")
elif computer_score > 21:
    print("Opponent went over. You win 😁")
elif user_score > computer_score:
    print("You win 😃")
else:
    print("You lose 😤")