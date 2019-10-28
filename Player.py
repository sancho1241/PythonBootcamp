class Player:
    '''
    This is the Player class of the milestone project one "BlackJack" of the "Complete Python Bootcamp by Jose  Portilla
    It includes the functionalities: add cards to hand, calculate hand value, show player's hand, make bet, settle bet, is busted and reset of the object on replay
    '''


    def __init__(self,name):
        '''
        creation of initial values and attributes for each player
        :param name: the player's name
        :return: n/a
        '''
        self.name=name
        self.account=1000
        self.hand=[]
        self.value = 0
        self.bet=0
        self.winner = False


    def add_card2hand(self,cards,deck):
        '''
        adds cards to the player's hand and calculates the value
        :param cards: list of cards to be added to player's hand
        :param deck: reference to the card deck to get the value
        :return: n/a
        '''
        # add card to hand
        for card in cards:
            self.hand.append(card)
            self.value += deck.getCardValue(card, self.value)


    def show_hand(self, initialShow = False):
        '''
        show the player's hand and the appropriate value
        :param initialShow: initially there is only one of the two dealer's cards shown
        :return: n/a
        '''
        print(f"{self.name} hand:")
        if self.name == 'Dealer' and initialShow:
            # initial run: show only one card
            print(f"{self.hand[0]} and a hidden card")
        else:
            # subsequent run -> show all cards
            print(self.hand)
            if self.value != 21:
                print("hand value: {}".format(self.value))
            else:
                print (f"{self.name} has BLACK JACK !!!!")

    def make_bet(self):
        '''
        player to place bet based on available funds
        :return: n/a
        '''
        while True:
            try:
                self.bet = int(input(f"Your account shows {self.account}. How much to bet? "))
                if self.bet > self.account or self.bet < 1:
                    raise  ValueError
                break
            except ValueError:
                print ("Please enter a valid number")


    def settle_bet(self):
        '''
        calculate new player's account once game is over
        :param winner:
        :return:
        '''
        if self.winner: # receive double amount if winner
            self.account += self.bet
        else: #reduce bet from account
            self.account -= self.bet
        print("Player's bet {}, Player's account: {}".format(self.bet,self.account))

    def is_busted(self):
        '''
        sets busted status if hand value is greater than 21
        :return: n/a
        '''
        if self.value > 21:
            print(f"{self.name} is busted !!!!!")
            self.status = 'Loser'
            return True
        else:
            return False

    def reset(self):
        '''
        resets player values once game is over and player wants to play again
        :return: n/a
        '''
        self.hand=[]
        self.value=0
        self.bet=0
        self.winner = False
