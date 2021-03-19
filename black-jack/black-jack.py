from functools import total_ordering
from hashlib import algorithms_guaranteed
import random
from random import seed

# Create Class Player
class Player:
    def __init__(self, name, initial_cards, deck):
        self.name = name
        self.initial_cards = initial_cards
        self.hand = self.deal_cards(deck)
    
# Deal cards
    def deal_cards(self, deck):
        hand = {}
        for i in range(self.initial_cards):
            # Secure random
            seed(18)
            # Get random card from deck
            card, value = random.choice(list(deck.items()))
            # Delete given card from deck
            deck.pop(card)
            hand[card] = value
        return hand

    def ask_card(self, deck):
        # Check value
        if self.hand_value <= 21:
            # Secure random
            seed()
            # Get random card from deck
            card, value = random.choice(list(deck.items()))
            # Delete given card from deck
            deck.pop(card)
            # Update values
            self.hand[card] = value
            self.hand_figure = self.show_figure()
            self.hand_value = self.add_values()


class Dealer(Player):
    def __init__(self, name, initial_cards, deck):
        super().__init__(name, initial_cards, deck)
    
    def ask_card(self, deck):
        super().ask_card(deck)
        if self.hand_value <= 16:
            # Secure random
            seed(5)
            # Get random card from deck
            card, value = random.choice(list(deck.items()))
            # Delete given card from deck
            deck.pop(card)
            # Update values
            self.hand[card] = value
            self.hand_figure = self.show_figure()
            self.hand_value = self.add_values()


class Gumbler(Player):
    def __init__(self, name, initial_cards, deck):
        super().__init__(name, initial_cards, deck)


# Show the cards
def show_hand(player):
    figures = ''
    for i in player.hand.keys():
        figures += i + ' '
    return figures


def add_values(player):
    total_value = 0 
    second_value = 0
    for key, value in player.hand.items():
        if 'A' in key:
            total_value += value
            second_value += value
        else:
            total_value += value
    # Take A's values as 11
    second_value += 1
    return total_value, second_value
        
    


def start_game():
# Create Deck
    spade = {'A♠': 1, '2♠': 2, '3♠': 3, '4♠': 4, '5♠': 5, '6♠': 6, '7♠': 7, 
             '8♠': 8, '9♠': 9, '10♠': 10, 'J♠': 10, 'Q♠': 10, 'K♠': 10}
    heart = {'A♥': 1, '2♥': 2, '3♥': 3, '4♥': 4, '5♥': 5, '6♥': 6, '7♥': 7, 
             '8♥': 8, '9♥': 9, '10♥': 10, 'J♥': 10, 'Q♥': 10, 'K♥': 10}
    club = {'A♣': 1, '2♣': 2, '3♣': 3, '4♣': 4, '5♣': 5, '6♣': 6, '7♣': 7, 
            '8♣': 8, '9♣': 9, '10♣': 10, 'J♣': 10, 'Q♣': 10, 'K♣': 10}
    diamond = {'A♦': 1, '2♦': 2, '3♦': 3, '4♦': 4, '5♦': 5, '6♦': 6, '7♦': 7, 
               '8♦': 8, '9♦': 9, '10♦': 10, 'J♦': 10, 'Q♦': 10, 'K♦': 10}
    
    deck = dict(spade, **heart, **club, **diamond)

# Create players
    dealer = Dealer('dealer', 1, deck)
    gumbler = Gumbler('player', 2, deck)
    print(f'{dealer.name}\'s hand: {dealer.hand}')
    print(show_hand(dealer))
    print(add_values(dealer))
    print(f'{gumbler.name}\'s hand: {gumbler.hand}')
    print(show_hand(gumbler))
    print(add_values(gumbler))
    print(deck)
    
    # ask = input('1. Ask card.\n2. Pass.\n')

    # if ask == '1':
    #     player.ask_card(deck)
        
    # print(player.hand)
    # print(player.hand_figure)
    
# Create Money
# Bet amount


# Double bet
# Choose separate cards
# if 2 A's give 1 card for each A
# Choose get other card
# Choose play again?

if __name__ == '__main__':
    start_game()