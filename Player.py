class Player():

    def __init__(self,name):
        self.name=name
        self.account=1000
        self.hand=[]
        pass

    def addCard2Hand(self,card):
        # add card to hand
        self.hand.append(card)
        #print(self.hand[0][0])
        #print(self.hand[0][1])

    def showHand(self):
        print(f"{self.name} hand:")
        print(self.hand)

        #if self

    def makeBet(self):
        bet = int(input(f"Your account shows {self.account}. How much to bet? "))
        self.account -= bet
