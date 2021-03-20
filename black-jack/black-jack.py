import random
from random import seed

# Create Class Player
class Hand:
    def __init__(self, name, initial_cards, deck):
        self.name = name
        self.initial_cards = initial_cards
        self.hand = self.deal_cards(deck)
        self.value_1 = None
        self.value_2 = None


# Deal cards
    def deal_cards(self, deck):
        hand = {}
        for i in range(self.initial_cards):
            # Secure random
            seed()
            # Get random card from deck
            card, value = random.choice(list(deck.items()))
            # Delete given card from deck
            deck.pop(card)
            hand[card] = value
        return hand


    def count_a(self):
        counter = 0
        for key in self.hand.keys():
            if 'A' in key:
                counter += 1
        return counter


    def add_values(self):
        player_total = 0
        second_player_total = 0
        a_quantity = self.count_a()
        if a_quantity > 0 :
            second_player_total += 10 * a_quantity
            for value in self.hand.values():
                player_total += value
                second_player_total += value 
        else:
            for value in self.hand.values():
                player_total += value
                second_player_total = 0
                
                
        self.value_1 = player_total
        self.value_2 = second_player_total
        return player_total,second_player_total
            

    def ask_card(self, deck):
        # Check value
        if self.value_1 <= 21 or self.value_2 <= 21:
            # Secure random
            seed()
            # Get random card from deck
            card, value = random.choice(list(deck.items()))
            # Delete given card from deck
            deck.pop(card)
            # Update values
            self.hand[card] = value
            self.value_1, self.value_2 = self.add_values()
        else:
            return


    def over_21(self):
        if self.value_1 > 21:
            self.value_1 = 'Over 21'
        if self.value_2 > 21:
            self.value_2 = 'Over 21'


class DealerHand(Hand):
    def __init__(self, name, initial_cards, deck):
        super().__init__(name, initial_cards, deck)
        self.value_1 = None
        self.value_2 = None
    
    def ask_card(self, deck):
        # Secure random
        #seed(6)
        seed()
        # Get random card from deck
        card, value = random.choice(list(deck.items()))
        # Delete given card from deck
        deck.pop(card)
        # Update values
        self.hand[card] = value
        self.value_1, self.value_2 = self.add_values()


class GumblerHand(Hand):
    def __init__(self, name, initial_cards, deck):
        super().__init__(name, initial_cards, deck)


# Show the cards
def show_hand(player):
    figures = ''
    for i in player.hand.keys():
        figures += i
        figures += ' '
    return figures

def show_values(player):
    if player.value_2 == 0 or player.value_2 > 21:
        return player.value_1
    else:
       return f'{player.value_1} || {player.value_2}'

def last_hand(player):
    if player.value_2 == 0 or player.value_2 > 21:
        return player.value_1


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
    dealer = DealerHand('Dealer', 1, deck)
    gumbler = GumblerHand('Player', 2, deck)

# GAME LOGIC 

    print('DEALER HAND:')
    print(show_hand(dealer))
    dealer.add_values()
    print(show_values(dealer))
    

    print('YOUR HAND:')
    print(show_hand(gumbler))
    gumbler.add_values()
    print(show_values(gumbler))
    
    
# Ask card
    while True:
        if gumbler.count_a() > 0:
            if gumbler.value_1 > 21 and gumbler.value_2 > 21:
                print('You Lose')
                return 
        else:
            if gumbler.value_1 > 21:
                print('You Lose')
                return

        ask = input('1. Ask card. \n2. Pass. \n3. Double bet. \n') 
        gumbler_hand = 0
        dealer_hand = 0

        if ask == '1':
            gumbler.ask_card(deck)
            print(show_hand(gumbler))
            # gumbler.over_21()
            print(show_values(gumbler))
            
            continue
        else:
            print('Dealer\'s turn')
            if dealer.count_a() > 0:
                while dealer.value_1 <= 16 and dealer.value_2 <= 16:
                    dealer.ask_card(deck)
                    print(show_hand(dealer))
                    

            else: 
                while dealer.value_1 <= 16:
                    dealer.ask_card(deck)
                    print(show_hand(dealer))
                    print(dealer.value_1)
                    
        gumbler_hand = last_hand(gumbler)
        dealer_hand = last_hand(dealer)

        if dealer_hand > 21:
            print('You Win')
            break

        if gumbler_hand > dealer_hand:
            print('You Win')
        elif gumbler_hand < dealer_hand:
            print('You Lose')
        else:
            print('Tie')

        break

# Valuate hands
    

    # if dealer_hand 
    
# Create Money
# Bet amount


# Double bet
# Choose separate cards
# if 2 A's give 1 card for each A
# Choose get other card
# Choose play again?

if __name__ == '__main__':
    start_game()