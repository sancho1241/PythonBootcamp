class Player():

    def __init__(self,name):
        self.name=name
        self.account=1000
        self.hand=[]
        self.value = 0
        pass

    def addCard2Hand(self,cards,deck):
        # add card to hand
        for card in cards:
            self.hand.append(card)
            self.value += deck.getCardValue(card, self.value)
        #self.hand +=[x for x in card]
        # calculate hand value
        #self.value += deck.addCardValue(card, self.value)


    def showHand(self):
        print(f"{self.name} hand:")
        #if self.name == 'Dealer' and len(self.hand) == 2:
            # inital run: show only one card
        #    print(f"{self.hand[0]} and a hidden card")
        #else:
            # subsequent run -> show all cards
        print(self.hand)
        print("hand value: {}".format(self.value))

    def makeBet(self):
        #bet = int(input(f"Your account shows {self.account}. How much to bet? "))
        #self.account -= bet
        pass

    def is_busted(self):
        if self.value > 21:
            print(f"{self.name} is busted !!!!!")
            return True
        else:
            return False