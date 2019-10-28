import itertools  # required for list comprehension in deck creation based  on Symbol, card
from random import randint  # required to randomly select a card from the 52 cards in blackjack deck


class Bank:
    """
        This is the Player class of the milestone project one "BlackJack" of the "Complete Python Bootcamp" by Jose  Portilla
        It includes the functionalities: add cards to hand, calculate hand value, show player's hand, make bet, settle bet, is busted and reset of the object on replay
    """

    # class constant
    BLACKJACK = 21

    def __init__(self):
        """
        constructur
        creates deck as list of symbol,card tuples
        """
        self.faces = ['Jack', 'Queen', 'King']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        colors = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
        self.deck = [x for x in itertools.product(colors, values)]
         #print(f"deck:{self.deck}")

        pass

    def get_card(self, number=1):
        """
        retrieves the number o cards randomly from the deck and returns them as list
        :param number: number of cards to be retrieved from the deck, default value is 1
        :return: cards as list of Symbol,value pairs
        """
         # select random cards, return them and remove them from deck
        cards = []
         #print(f"deck length before getting cards: {len(self.deck)}")

         # delete selected  card from deck and add it to list to be returned
        for x in range(0, number):
            cards.append(self.deck.pop(randint(0, len(self.deck)-1)))
             # print(f"random card given: {value}")
         #eprint("deck  length after getting cards: {} ".format(len(self.deck)))
        return cards
        pass

    def get_cardvalue(self, card, handvalue):
        """
        returns the card value of the card based on the handvalue provided. This methds handles the special case of an Ace  that can count either 11 or 1 whatever
        is more favourable for the player
        :param card: card as Symbol, value pair provided
        :param handvalue: value of existing hand prior to the new card added
        :return:
        """
        if card[1] in self.faces:
                return 10
        elif card[1] == 'Ace':
                 # check value of Ace which is more favourable for user
            if (handvalue + 11) <= 21:
                return  11
            else:
                return 1
        else:
                 # first item in tuple is Symbol, second is value -> assign value
                return int(card[1])


    def winner(self, player, dealer):
        """
        shows hands of each player and returns the winner of the game
        :param player: reference to player object
        :param dealer: reference to dealer object
        :return: String 'Player' or 'Dealer'
        """
        player.showHand()
        dealer.showHand()

        if player.is_busted():
            player.winner = False
            return 'Dealer'
        elif dealer.is_busted():
            player.winner = True
            return 'Player'
        elif player.value >= dealer.value:
            player.winner = True
            return 'Player'
        else:
            player.winner = False
            return 'Dealer'
