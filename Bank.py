import itertools
from random import randint


class Deck():

    def __init__(self):
        self.faces = ['Jack', 'Queen', 'King']
        values=['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        # values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', self.faces, 'Ace']
        colors = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
        self.deck = [x for x in itertools.product(colors, values)]
        print(f"deck:{self.deck}")

        pass

    def getCard(self, number=1):
        # select random cards, return them and remove them from deck
        cards = []
        for x in range(0, number):
            cards.append(self.deck.pop(randint(0, len(self.deck))))
            # print(f"random card given: {value}")
        print("deck  length: {} ".format(len(self.deck)))
        return cards
        pass

    def getCardValue(self, card, handValue):
        '''

        :param hand:
        :param handValue:
        :return:
        '''
        if card[1] in self.faces:
                return 10
        elif card[1] == 'Ace':
                # check value of Ace which is more favourable for user
            if (handValue + 11) <= 21:
                return  11
            else:
                return 1
        else:
                # first item in tuple is Symbol, second is value -> assign value
                return int(card[1])


    def winner(self, player, dealer):
        player.showHand()
        dealer.showHand()

        if player.is_busted():
            return 'Dealer'
        elif dealer.is_busted():
            return 'Player'
        elif player.value >= dealer.value:
            return 'Player'
        else:
            return 'Dealer'
