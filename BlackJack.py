
'''
This is the main file of the milestone project one "BlackJack" of the "Complete Python Bootcamp by Jose  Portilla
'''


# Bank and Player classes are stored in own modules
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

    # Player needs to make an initial bet
    player.make_bet()


    # Assign first two cards to each player and show hands
    player.add_card2hand(bank.get_card(2),bank)
    player.show_hand()

    dealer.add_card2hand(bank.get_card(2),bank)
    dealer.show_hand(True) # initially only one card is shown for the dealer, indicated by the flag for "initial"

    if player.value == bank.BLACKJACK: # if Player has black jack right away with two cards the game is over and player has won
        gameOver = True
    else:
        #  ... otherwise loop until  someone wins or busts
        gameOver=False

    # while loop for actual game. Repeat as long as nobody has won
    while not gameOver:
        while True:
            try: # ask Player if he wants to receive another card or is fine
                playerMove = str(input(f"{player.name}: (h)it or (s)tay? "))
                if playerMove != 'h' and playerMove != 's':
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter h  or s. ")

        if playerMove == 'h': #hit
            player.add_card2hand(bank.get_card(),bank)
            player.show_hand()
            if player.is_busted() or player.value == bank.BLACKJACK:
                gameOver = True
            continue
        else: # stay, it's the dealer's turn until score is higher than the player's or the dealer is busted
            while bank.winner(player, dealer) == 'Player' and not dealer.is_busted():
                dealer.add_card2hand(bank.get_card(),bank)
            gameOver = True


    winner = bank.winner(player, dealer) # calculate the winner based on the hand values
    print (f"The winner is {winner}")
    player.settle_bet() # add or subtract player's bet to from account

    # "Play again" section
    while True:
        try:
            playerMove = str(input("Play again? (y)es or (n)o? "))
            if  playerMove == 'n': # player wants to exit
                break
            elif playerMove == 'y': # reset player objects -> hand and hand value
                # for next game reset player's hands and reset values
                player.reset()
                dealer.reset()
                break
            else:
                raise ValueError
        except ValueError:
            print ("Invalid input. Please enter y or n")


print ("Thanks for playing Sancho's Blackjack. We hope  you had some fun")