
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

    if player.value == bank.BLACKJACK: # black jack right away with two cards
        gameOver = True
    else:
        #  loop until  someone wins or busts
        gameOver=False
    while not gameOver:
        while True:
            try:
                playerMove = str(input(f"{player.name}: (h)it or (s)tay? "))
                if playerMove != 'h' and playerMove != 's':
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter h  or s. ")

        if playerMove == 'h': #hit
            player.addCard2Hand(bank.getCard(),bank)
            player.showHand()
            if player.is_busted() or player.value == bank.BLACKJACK:
                gameOver = True
            continue
        else: # stay, it's the dealer's turn until score is higher than the player's or the dealer is busted
            while bank.winner(player, dealer) == 'Player' and not dealer.is_busted():
                dealer.addCard2Hand(bank.getCard(),bank)
            gameOver = True


    winner = bank.winner(player, dealer)
    print (f"The winner is {winner}")
    player.settle_bet(winner)

    while True:
        try:
            playerMove = str(input("Play again? (y)es or (n)o? "))
            if  playerMove == 'n':
                play = False
                break
            elif playerMove == 'y': # reset player ojects -> hand and hand value
                player.reset()
                dealer.reset()
                break
            else:
                raise ValueError
        except ValueError:
            print ("Invalid input. Please enter y or n")


print ("Thanks for playing Sancho's Blackjack. We hope  you had some fun")