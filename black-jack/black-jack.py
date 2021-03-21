import random
from random import seed

# Create Class Player
class HandPlayer:
    def __init__(self, name, initial_cards, deck):
        self.name = name
        self.initial_cards = initial_cards
        self.hand = self.deal_cards(deck)
        self.value_1 = None
        self.value_2 = None


# Deal cards
    def deal_cards(self, deck):
        """
        Deal the cards to the players
        
        param dict deck dictionary with all cards
        return a dict, the hand with the correspondent number of cards
        """
        hand = {}
        for i in range(self.initial_cards):
            # Secure random
            #seed()
            seed(5)
            # Get random card from deck
            card, value = random.choice(list(deck.items()))
            # Delete given card from deck
            deck.pop(card)
            hand[card] = value
        return hand


    def count_a(self):
        """
        Count the quantity of A's in player's hand

        no param
        return int, number of A's in player's hand
        """
        counter = 0
        for key in self.hand.keys():
            if 'A' in key:
                counter += 1
        return counter


    def add_values(self):
        """
        Add all the card's values in player's hand

        no param
        return int, hand's value and optional value if there's a A
        """
        player_total = 0
        second_player_total = 0
        a_quantity = self.count_a()

        if a_quantity > 0 :
            # Takes A value as 11
            second_player_total += 10 * a_quantity
            for value in self.hand.values():
                player_total += value
                second_player_total += value 
        else:
            # Take A value as 1
            for value in self.hand.values():
                player_total += value
                second_player_total = 0
        
        self.value_1 = player_total
        self.value_2 = second_player_total
        return player_total,second_player_total
            

    def ask_card(self, deck):
        """
        Ask for another card

        param dict, collection of every card
        void function, add a card to the player's hand
        """
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


class DealerHand(HandPlayer):
    def __init__(self, name, initial_cards, deck):
        super().__init__(name, initial_cards, deck)
        self.value_1 = None
        self.value_2 = None
    
    def ask_card(self, deck):
        """
        Ask for another card

        param dict, collection of every card
        void function, add a card to the player's hand
        """
        # Secure random
        #seed()
        #seed(99) A A
        seed(70)
        # Get random card from deck
        #card, value = random.choice(list(deck.items()))
        # Delete given card from deck
        #deck.pop(card)
        # Update values
        self.hand['K'] = 10
        #self.hand[card] = value
        self.value_1, self.value_2 = self.add_values()


class GumblerHand(HandPlayer):
    def __init__(self, name, initial_cards, deck):
        super().__init__(name, initial_cards, deck)


# Show the cards
def show_hand(player):
    """
    Convert hand's key into string

    param HandPlayer, player hand
    return string with every hand's key
    """
    figures = ''
    for i in player.hand.keys():
        figures += i
        figures += ' '
    return figures

def show_values(player):
    """
    Filter value to show

    param HandPlayer, player hand
    return int or str, value or values to show
    """
    if player.value_2 == 0 or player.value_2 > 21:
        return player.value_1
    else:
       return f'{player.value_1} || {player.value_2}'

def last_hand(player):
    """
    Filter final hand's value

    param HandPlayer, player hand
    return int, last hand's value
    """
    if player.value_2 == 0 or player.value_2 > 21:
        return player.value_1
    else:
        return max(player.value_1, player.value_2)


def start_game():
    """
    Game flow

    no param
    void funtion
    """
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
    

#    print('YOUR HAND:')
#    print(show_hand(gumbler))
    gumbler.add_values()
#    print(show_values(gumbler))
    
    
# Ask card
    while True:
        print('YOUR HAND:')
        print(show_hand(gumbler))
        print(show_values(gumbler))
        # Base case if your hand is over 21
        if gumbler.count_a() > 0:
            if gumbler.value_1 > 21 and gumbler.value_2 > 21:
                
                # print(show_hand(gumbler))
                # print(show_values(gumbler))
                print('You Lose')
                return 
        else:
            if gumbler.value_1 > 21:
                
                # print(show_hand(gumbler))
                # print(show_values(gumbler))
                print('You Lose')
                return

        # print(show_hand(gumbler))
        # print(show_values(gumbler))

        # Player imput to control game flow
        ask = input('1. Ask card. \n2. Pass. \n3. Double bet. \n') 

        # Final hand's values
        gumbler_hand = 0
        dealer_hand = 0

        # Ask for other card
        if ask == '1':
            gumbler.ask_card(deck)
            #print(show_hand(gumbler))
            #print(show_values(gumbler))
            continue
        else:
        # Automated dealer's move
            print('Dealer\'s turn')
            if dealer.count_a() > 0:
                
                # Rule: Dealer ask with 16 Case with A
                while dealer.value_1 <= 17 and dealer.value_2 <= 17:
                    dealer.ask_card(deck)
                    # Case dealer have BlackJack
                    if dealer.value_2 == 21:
                        
                        print(show_hand(dealer))
                        print(dealer.value_2)

                    elif dealer.value_1 > 21 and dealer.value_2 > 21:
                        print(show_hand(dealer))
                        print(dealer.value_1)
                        return
                    
                    print(show_hand(dealer))
                    print(show_values(dealer))
            else: 
                # Rule: Dealer ask with 
                while dealer.value_1 <= 16:
                    dealer.ask_card(deck)
                    print(show_hand(dealer))
                    print(show_values(dealer))
                
        # Giving final value
        gumbler_hand = last_hand(gumbler)
        dealer_hand = last_hand(dealer)

        # If Dealer hand is over 21 you win
        if dealer_hand > 21:
            print('You Win')
            break
        
        # If your hand is higher than dealer's hand you win
        if gumbler_hand > dealer_hand:
            print(dealer_hand)
            print('You Win')
        # If your hand is lower than dealer's hand you lose
        elif gumbler_hand < dealer_hand:
            print(dealer_hand)
            print('You Lose')
        # If both hand's are equal
        else:
            print(dealer_hand)
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