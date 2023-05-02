from random import randint
from art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_cards=[cards[randint(0,12)]]

player_cards=[cards[randint(0,12)], cards[randint(0,12)]]

def BlackJack():
    global cards
    global player_cards
    global dealer_cards
    answer="y"
    while answer=="y":
        player_score=sum(player_cards)
        dealer_score=sum(dealer_cards)
        if player_score >21:
            if 11 in player_cards:
                player_cards[player_cards.index(11)]=1
                player_score=sum(player_cards)
            else:
                print(f"Dealers cards: {dealer_cards} current score = {dealer_score}")
                print(f"Your cards: {player_cards} current score = {player_score}")
                print("You lose")
                return
        print(f"Dealers cards: {dealer_cards} current score = {dealer_score}")
        print(f"Your cards: {player_cards} current score = {player_score}")
        if player_score ==21:
            print("You win")
            return
        answer=input('If you want to draw a card type "y": ')
        print("")
        if answer=="y":
            player_cards.append(cards[randint(0,12)])
    
    dealer_score=sum(dealer_cards)

    while dealer_score<17:
        dealer_cards.append(cards[randint(0,12)])
        dealer_score=sum(dealer_cards)
        if dealer_score > 21:
            if 11 in dealer_cards:
                dealer_cards[dealer_cards.index(11)]=1
                dealer_score=sum(dealer_cards)
            else:
                print(f"Dealers cards: {dealer_cards} current score = {dealer_score}")
                print(f"Your cards: {player_cards} current score = {player_score}")
                print("You win")
                return

    if dealer_score == player_score:
        print(f"Dealers cards: {dealer_cards} current score = {dealer_score}")
        print(f"Your cards: {player_cards} current score = {player_score}")
        print("Draw")
    elif dealer_score > player_score:
        print(f"Dealers cards: {dealer_cards} current score = {dealer_score}")
        print(f"Your cards: {player_cards} current score = {player_score}")
        print("Dealer wins")
    elif player_score > dealer_score:
        print(f"Dealers cards: {dealer_cards} current score = {dealer_score}")
        print(f"Your cards: {player_cards} current score = {player_score}")
        print("You win")

BlackJack()
