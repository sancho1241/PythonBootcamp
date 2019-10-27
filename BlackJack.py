
from Bank import Bank
from Player import Player

# create Players
player = Player("Player")
dealer = Player("Dealer")

print ("Welcome to Sancho's Blackjack. Have fun.")

# while Player wants to play
play = True

while play:

    # create bank object with card deck
    bank = Bank()

    # Player needs to make an inital bet
    player.makeBet()


    # Assign first two cards to player
    player.addCard2Hand(bank.getCard(2),bank)
    player.showHand()
    # Assign next two cards to dealer:
    dealer.addCard2Hand(bank.getCard(2),bank)
    dealer.showHand(True)


    #  loop until  someone wins or busts
    gameOver=False
    while not gameOver:
        playerMove = input(f"{player.name}: (h)it or (s)tay? ")
        if playerMove == 'h': #hit
            player.addCard2Hand(bank.getCard(),bank)
            player.showHand()
            if player.is_busted():
                gameOver = True
            continue
        else: # stay, it's the dealer's turn until score is higher than the player's or the dealer is busted
            while bank.winner(player, dealer) == 'Player' and not dealer.is_busted():
                dealer.addCard2Hand(bank.getCard(),bank)
            gameOver = True


    winner = bank.winner(player, dealer)
    print (f"The winner is {winner}")
    player.settle_bet(winner)

    if input("Play again? (y)es or (n)o? ") == 'n':
        play = False
    else: # reset player ojects -> hand and hand value
        player.reset()
        dealer.reset()

print ("Thanks for playing Sancho's Blackjack. We hope  you had some fun")