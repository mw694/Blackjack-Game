import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate (card_score):
    total = sum(card_score)
    if total == 21 and len(card_score) == 2:
        return 0
    if 11 in cards and len(card_score) >= 3:
        card_score.remove(11)
        card_score.append(1)
    return sum(card_score)

def compare (sum_my_card, sum_com_card):
    if sum_my_card == sum_com_card:
        return "It's a draw."

    elif sum_my_card == 0:
        return "You got a Blackjack!"

    elif sum_com_card == 0:
        return "Computer got a Blackjack!"

    elif sum_my_card > sum_com_card and sum_my_card < 21:
        return "You win!"

    elif sum_com_card > sum_my_card and sum_com_card <21:
        return "Computer win!"

    elif sum_my_card > 21:
        return "You went over 21, computer wins!"

    elif sum_com_card > 21:
        return "Computer went over 21, you win!"




while True:
    play = input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no:").lower()
    if play == "n":
        print("Thank you!")
        break

    elif play != "y":
        continue

    print(art.logo)

    my_card = random.sample(cards,2)
    com_card = random.sample(cards,2)
    sum_my_card = sum(my_card)
    sum_com_card = sum(com_card)

    print(f"Your cards: {my_card}, your current score is: {sum_my_card}")
    print(f"Computer's first card: {com_card[0]}")

    if sum_my_card == 0 or sum_com_card == 0:
        print(compare(sum_my_card, sum_com_card))
        continue

    while True:
        get_more = input("Type 'y' to get another card, type 'n' to pass:").lower()
        while get_more not in ["y", "n"]:
            get_more = input("Please try again. (y / n)")

        if get_more == "y":
            my_new_card = random.choice(cards)
            my_card.append(my_new_card)
            sum_my_card = sum(my_card)
            print(f"Your new cards: {my_card}, you current score is: {sum_my_card}")

        else:
            break

    while sum_com_card < 17:
        com_new_card = random.choice(cards)
        com_card.append(com_new_card)
        sum_com_card = sum(com_card)

    print(f"Your final hand: {my_card}, your final score: {sum_my_card}")
    print(f"Computer's final hand: {com_card}, computer's final score: {sum_com_card}")
    print(compare(sum_my_card, sum_com_card))
    print("\n")
