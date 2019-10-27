class Player():

    def __init__(self,name):
        self.name=name
        self.account=1000
        self.hand=[]
        self.value = 0
        self.bet=0
        self.winner = False
        pass

    def addCard2Hand(self,cards,deck):
        # add card to hand
        for card in cards:
            self.hand.append(card)
            self.value += deck.getCardValue(card, self.value)
        #self.hand +=[x for x in card]
        # calculate hand value
        #self.value += deck.addCardValue(card, self.value)


    def showHand(self, initialShow = False):
        print(f"{self.name} hand:")
        if self.name == 'Dealer' and initialShow:
            # inital run: show only one card
            print(f"{self.hand[0]} and a hidden card")
        else:
            # subsequent run -> show all cards
            print(self.hand)
            if self.value != 21:
                print("hand value: {}".format(self.value))
            else:
                print (f"{self.name} has BLACK JACK !!!!")

    def makeBet(self):
        while True:
            try:
                self.bet = int(input(f"Your account shows {self.account}. How much to bet? "))
                if self.bet > self.account or self.bet < 1:
                    raise  ValueError
                break
            except ValueError:
                print ("Please enter a valid number")


    def settle_bet(self,winner):
        if self.winner: # receive double amount if winner
            self.account += self.bet
        else: #reduce bet from account
            self.account -= self.bet
        print("Player's bet {}, Player's account: {}".format(self.bet,self.account))

    def is_busted(self):
        if self.value > 21:
            print(f"{self.name} is busted !!!!!")
            self.status = 'Loser'
            return True
        else:
            return False

    def reset(self):
        self.hand=[]
        self.value=0
        self.bet=0
        self.winner = False
