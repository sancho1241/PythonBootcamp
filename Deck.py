import itertools
from random import randint

class Deck():

    def __init__(self):
        self.faces=['Jack','Queen','King']
        #values=['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        values=['2','3','4','5','6','7','8','9','10',self.faces,'Ace']
        colors=["Diamonds","Hearts","Spades","Clubs"]
        self.deck= [x for x in itertools.product(colors,values)]
        print(f"deck:{self.deck}" )
        #print("deck  length: {} ".format(len(self.deck)))
        pass

    def getCard(self):
        #select random card, return it and remove it from deck
        return self.deck.pop(randint(0,len(self.deck)))
        print(f"random card: {value}")
        pass

    def handValue(self,hand):
        value = 0
        for card in hand:
            if card[1] in self.faces:
                value += 10
            elif card[1] == 'Ace':
                value += 11
            else:
                value += int(card[0])