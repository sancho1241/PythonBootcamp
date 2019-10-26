# import Player
# import Deck
from Bank import Deck
from Player import Player

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

# while Player wants to play
play = True
while play

    # create card deck
    deck = Deck()

    # create Players
    player = Player("Player")
    dealer = Player("Dealer")

    # Player needs to make an inital bet
    player.makeBet()


    # Assign first two cards to player
    player.addCard2Hand(deck.getCard(2),deck)
    player.showHand()
    # Assign next two cards to dealer:
    dealer.addCard2Hand(deck.getCard(2),deck)
    dealer.showHand()


    #  loop until  someone wins or busts
    gameOver=False
    while not gameOver:
        playerMove = input(f"{player.name}: (h)it or (s)tay? ")
        if playerMove == 'h': #hit
            player.addCard2Hand(deck.getCard(),deck)
            player.showHand()
            if player.is_busted():
                gameOver = True
            continue
        else: # stay, it's the dealer's turn until score is higher than the player's or the dealer is busted
            while deck.winner(player, dealer) == 'Player' and not dealer.is_busted():
                dealer.addCard2Hand(deck.getCard(),deck)
            gameOver = True

    print (f"The winner is {deck.winner(player, dealer)}")
    if input("Play again? (y)es or (n)o? ") == 'n'
        play = False