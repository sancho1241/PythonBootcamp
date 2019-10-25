import Player
import Deck

'''
Computer Dealer
Human Player
Deck 52 cards
1. Player makes a bet
2. Player gets 2 cards
3. Dealer gets 2 cards, 1 showing
4. Players turn: Hit or Stay
5.Dealer: if player is under 1 dealer hits until 21 or bust
Rules: face cards = 10
Ace: 1 or 11 whatever is more favourable for the player
'''

#input("Welcome to Sven's BlackJack. Press Key to continue! ")
deck = Deck.Deck()
#print ("Card given:{} ".format(deck.getCard()))
player = Player.Player("Sven")
#Player needs to make a bet
player.makeBet()

dealer = Player.Player("Dealer")
# Assign first two cards to player
for x in range(0,2):
    player.addCard2Hand(deck.getCard())
player.showHand()
#Assign next two cards to dealer:
for x in range(0,2):
    dealer.addCard2Hand(deck.getCard())
dealer.showHand()

#  loop until  someone busts
while True:
    playerMove = input(f"{player.name}: (H)it or (S)tay? ")
