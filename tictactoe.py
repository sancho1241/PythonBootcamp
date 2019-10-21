from random import randint

class TicTacToe():

    playGrid = [['','',''] for x in range(0,3)]
    namePlayer1='Sancho'
    namePlayer2='Pancho'
    player1Symbol='x'
    player2Symbol='o'
    playerNames = [namePlayer1,namePlayer2]

    def __init__(self):
        pass

    # set Player Names
    def setPlayers(self):    
        self.namePlayer1  = input('Name Spieler 1: ')
        self.namePlayer2  = input('Name Spieler 2: ')
        self.playerNames = [self.namePlayer1,self.namePlayer2]
        print(f'{self.namePlayer1}, du spielst mit dem Symbol x')
        print(f'{self.namePlayer2}, du spielst mit dem Symbol o')
    
    def are3inaRow(self,playerSymbol):
        # check if player has 3 in a row
        #print(self.playGrid)
        for i in range(0,len(self.playGrid)):
            if [playerSymbol,playerSymbol,playerSymbol] == self.playGrid[i]:
                #3 equal symbols in a row
                return True
            if [playerSymbol,playerSymbol,playerSymbol] == [self.playGrid[0][i],self.playGrid[1][i],self.playGrid[2][i]]:
                #3 equal symbols in column
                return True
        
        if  [playerSymbol,playerSymbol,playerSymbol] == [self.playGrid[0][0],self.playGrid[1][1],self.playGrid[2][2]]:
                #3 equal symbols diagonal
                return True
        
        if  [playerSymbol,playerSymbol,playerSymbol] == [self.playGrid[0][2],self.playGrid[1][1],self.playGrid[2][0]]:
                #3 equal symbols reverse diagonal
                return True
        
        # nno equals symbols found -> go ahead
        return False
    
    def playGame(self,beginner):
        player = beginner
        #print(f'player: {player}')
        # aks for input 9 times -> max number of moves
        for i in range(0,9):
            #row = (int input(f'Welche Zeile {self.playerNames[player-1]}: '))
            #col = (int input(f'Welche Spalte {self.playerNames[player-1]}: '))
            invalidInput=True
            while invalidInput:
                
                try:
                    row = int(input(f'Welche Zeile {self.playerNames[player-1]}: '))
                    col = int(input(f'Welche Spalte {self.playerNames[player-1]}: '))
                
                    if self.playGrid[row-1][col-1] != '':  
                        print("Dort ist schon ein Symbol. Wähle bitte ein freies Feld aus.")
                        invalidInput=True
                        continue
                except:
                    print("Ungültiger Wert. Wähle bitte ein freies Feld aus.")
                    invalidInput=True
                    continue

            invalidInput=False           
            if player==1: 
                self.playGrid[row-1][col-1]='x'
            elif player==2:
                self.playGrid[row-1][col-1]='o'
            #show updated grid 
            if self.are3inaRow(self.playGrid[row-1][col-1]):
                print ("Player {} you won!".format(self.playerNames[player-1]))
                exit()
            
            #toggle player
            if player==1:
                player=2
            elif player==2:
                player=1
            self.printGrid()    

    # create random int to determine beginner
    def determineBeginner(self):
        beginner = randint(1,2)
        print (f'Ich habe gewürfelt, es beginnt Spieler {beginner} {self.playerNames[beginner-1]}')
        return beginner

    #print grid
    def printGrid(self):
        print("The new grid looks like this:")
        m = map(str,self.playGrid)
        #print ("".join(m))
        #for 
        for items in self.playGrid:
            n = map(str,items)
            print ("  | ".join(n))
            print("----------")
        #print (str(self.playGrid))

# create new object
myTicTacToe = TicTacToe()

#print the grid
myTicTacToe.printGrid()

#read player names and assgin symbols
myTicTacToe.setPlayers()

#play the game with random beginner
myTicTacToe.playGame(myTicTacToe.determineBeginner())

#print the grid
myTicTacToe.printGrid()
