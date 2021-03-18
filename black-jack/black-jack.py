import random
from random import seed

# Create Class Player
class Player:
    def __init__(self, name, initial_cards):
        self.name = name
        self.initial_cards = initial_cards
        
    
# Deal cards
    def deal_cards(self, deck):
        hand = {}
        for i in range(self.initial_cards):
            seed()
            # Get random card from deck
            card, value = random.choice(list(deck.items()))
            # Delete given card from deck
            deck.pop(card)
            hand.update({card: value})
        return hand

        


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
    dealer = Player('dealer', 1)
    player = Player('player', 2)
    print(deck)
    
# Create Money
# Bet amount

# Check value
# Double bet
# Choose separate cards
# if 2 A's give 1 card for each A
# Choose get other card
# Choose play again?

if __name__ == '__main__':
    start_game()