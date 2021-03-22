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
            seed()
            #seed(5)
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
        seed()
        #seed(99) A A
        #seed(70)
        # Get random card from deck
        card, value = random.choice(list(deck.items()))
        # Delete given card from deck
        deck.pop(card)
        # Update values
        #self.hand['K'] = 10
        self.hand[card] = value
        self.value_1, self.value_2 = self.add_values()

        return


class GumblerHand(HandPlayer):
    def __init__(self, name, initial_cards, deck, money):
        super().__init__(name, initial_cards, deck)
        self.money = money


    def bet(self, bet, pot):
        """
        Bet and rest the bet of money

        param int bet, ammount of bet
        param int pot, hole bet of dealer and gumbler
        return pot
        """
        self.money -= bet
        # Increasing the money by two players
        pot += bet * 2
        return pot


    def win(self, pot):
        """
        Add the pot to gumbler's money and print WIN

        param int pot, hole bet of dealer and gumbler
        return money, gumbler's money
        """
        print('\t\t\tYOU WIN!!!')
        self.money += pot
        return self.money


    def lose(self):
        """
        Print LOSE

        no param
        return money, gumbler's money
        """
        print('\t\t\tYOU LOSE!!!')
        return self.money
    

    def tie(self, bet):
        """
        Add gumbler's bet to his money

        param int bet, gumbler's bet
        return money, gumbler's money
        """
        print('\t\t\tTIE!!!')
        self.money += bet
        return self.money


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
    dealer.add_values()
    gumbler = GumblerHand('Player', 2, deck, 500)
    gumbler.add_values()

# Bet
    bet = 10
    pot = 0

# Print gyumbler money
    print(f'your money: {gumbler.money}$')

# Counter for double bet
    counter = 0

# GAME LOGIC 
# Ask card
    while True:
        # Bet only in the first turn
        if counter == 0:
            pot = gumbler.bet(bet, pot)

        # Print Money and Pot
        print(f'Your Bet: {bet}')
        print(f'Your Money: {gumbler.money}')
        print(f'POT: {pot}')
        # Print hands
        print(f"""\tYOUR HAND:\t\tDEALER HAND:
        {show_hand(gumbler)}\t\t\t{show_hand(dealer)}
        {show_values(gumbler)}\t\t\t{show_values(dealer)}
        """)
        

        # Base case if your hand is over 21
        if gumbler.count_a() > 0:
            # Two hand's options over 21
            if gumbler.value_1 > 21 and gumbler.value_2 > 21:
                gumbler.lose()
                break
        else:
            # Hand over 21
            if gumbler.value_1 > 21:
                gumbler.lose()
                break

        # Player imput to control game flow
        ask = input(f'1. Ask card. \n2. Pass. \n{"3. Double bet. " if counter == 0 else ""} \n')

        # Final hand's values
        gumbler_hand = 0
        dealer_hand = 0
        # Pass
        if ask == '1':
            # Disable Double bet option
            counter += 1
            # Ask for other card
            gumbler.ask_card(deck)
            continue
        elif ask == '2':
            # Disable Double bet option
            counter += 1
            # Automated dealer's move
            print('\t\t     DEALER\'S TURN')

            while dealer.value_1 <= 16:

                    # Ask for card
                    print('\t\t     DEALER HAND:')
                    dealer.ask_card(deck)
                    print(f'\t\t     {show_hand(dealer)}')

                    # Case dealer have BlackJack
                    if dealer.value_2 == 21:
                        print(f'\t\t     {dealer.value_2}')
                        break
                    
                    print(f'\t\t     {show_values(dealer)}')
        # Double bet
        elif ask == '3' and counter == 0:
                # Disable Double bet option
                counter += 1
                # Double bet
                pot = gumbler.bet(bet, pot)
                bet *= 2
                continue
        # Giving final value
        gumbler_hand = last_hand(gumbler)
        dealer_hand = last_hand(dealer)

        print(f"""\n\tYOUR HAND:\t\tDEALER HAND:
        {show_hand(gumbler)}\t\t\t{show_hand(dealer)}
        {show_values(gumbler)}\t\t\t{show_values(dealer)}
        """)

        # If Dealer hand is over 21 you win
        if dealer_hand > 21:
            gumbler.win(pot)
        # If your hand is higher than dealer's hand you win
        elif gumbler_hand > dealer_hand:
            gumbler.win(pot)
        # If your hand is lower than dealer's hand you lose
        elif gumbler_hand < dealer_hand:
            gumbler.lose()
        # If both hand's are equal
        else:
            gumbler.tie(bet)

        break

    print(f'Your money: {gumbler.money}$')


if __name__ == '__main__':
    start_game()