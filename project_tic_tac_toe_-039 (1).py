
print("----------WELCOME TO TIC TAC TOE----------")
# Ask user how many person wants to play game or want to exit game
# Display pop up
print("\nPress Y/y to play game\nPress n/N to exit game\n")
while True:
    u = input("User option selected :")
    if u not in ['y', 'Y', 'n', 'N']:
        print ("Wrong input, ", end ='')
        continue
    break

if u == 'n' or u == 'N':
    print  ("End game")
    exit()

while True:
    print("\nPress 1 for single player\nPress 2 for multiplayer\nPress 3 to exit game\n")
    while True:
        u = input("User option selected:")
        if u not in ['1', '2', '3']:
            print ("Wrong input, ", end ='')
            continue
        break
    single_player = '1'
    multiplayer = '2'
    exit = '3'

    while u == single_player:
        print("\n\n----------WELCOME TO SINGLE PLAYER GAME----------\n")
        import random
        def displayBoard(board):

            # Printing board of the game
            print(board[1] + '|' + board[2] + '|' + board[3])
            print('_|_|_')
            print(board[4] + '|' + board[5] + '|' + board[6])
            print('_|_|_')
            print(board[7] + '|' + board[8] + '|' + board[9])
            print('', '|', '|')
            print("\n")

        def isSpaceFree(board, move):
            # Returns true if the passed move is free on the board.
            if board[move] == ' ':
                return True
            else:
                return False


        def selectPlayerLetter():
            # Asking the player if they want to be X or O.
            letter = ''
            while not (letter == 'X' or letter == 'O'):
                letter = input('\nDo you want to be X or O?')
                letter = letter.upper()
            # The first letter in the list is players letter and the second one is the computers.
            if letter == 'X':
                return ['X', 'O']
            else:
                return ['O', 'X']


        def whoGoesFirst():
            # Having a toss between player and computer for the first move.
            select_toss = int(input("\nEnter 1: for heads or  Enter 0: for tails: "))

            while True:
                if select_toss not in [1, 0]:   # If input is not in 1 or 0, looping it until player enters valid input.
                    select_toss = int(
                        input("Incorrect input\nPlease Enter 1: for heads or Enter 0: for tails: "))
                    continue
                break
            toss = random.randint(0, 1)
            if toss == 1:
                print("Heads came.")
            else:
                print("Tails came.")
            if toss == select_toss:
                print("So player goes first\n")
                return 'player'
            else:
                print("So computer goes first\n")
                return 'computer'
        
        
        def handleTurn(board, letter, move):
            # making move and checking if the input is valid and the position is open
            if isSpaceFree(board, move):
                board[move] = letter
            else:
                print("Can't insert there!")       # Checking if the position entered is not available.
                move = int(input("Please enter new position:  "))
                handleTurn(board,letter, move)
                return



        def checkForWinner(board, letter):
            # Given a board and a player’s letter, this function returns True if that player has won.
            #Checking if any rows have all the same value
            return ((board[1] == letter and board[2] == letter and board[3] == letter) or #Checking row number 1 (across the top)
            (board[4] == letter and board[5] == letter and board[6] == letter) or #Checking row number 2 (across the middle)
            (board[7] == letter and board[8] == letter and board[9] == letter) or #Checking row number 3 (across the bottom)
            #Checking if any columns have all the same value
            (board[1] == letter and board[4] == letter and board[7] == letter) or #Checking column number 1 (down the left side)
            (board[2] == letter and board[5] == letter and board[8] == letter) or #Checking column number 2 (down the middle)
            (board[3] == letter and board[6] == letter and board[9] == letter) or #Checking column number 3 (down the right side)
            #Checking if any diagonals have all the same value
            (board[1] == letter and board[5] == letter and board[9] == letter) or #Checking diagonal
            (board[3] == letter and board[5] == letter and board[7] == letter))   #Checking diagonal



        def getBoardCopy(board):
            # Make a duplicate copy of the board list on which computer can check winning moves.
            board_copy = []

            for i in board:                      # This copy will not effect the original board.
                board_copy.append(i)
            return board_copy



        def getPlayerMove(board):
            # Taking input from the player to make their move.
            move = ' '
            # Checking if the player has entered valid input.
            while move not in '1 2 3 4 5 6 7 8 9'.split():
                enter_move = input('Choose a position from (1-9): ')
                try:
                    enter_move = int(enter_move)
                except ValueError:
                    print("\nYou entered wrong input\n")
                    continue
                move = enter_move
                if move>0 and move<10 :
                     return move
                while True:
                     if move < 0 or move > 10:
                         enter_move = int(input('Choose a position from (1-9): '))
                         if enter_move>0 and enter_move<10 :
                             move = enter_move
                             return move
                             break
                         
            
                else:
                    print(name,"choose correct option")



        def chooseRandomMove(board, movesList):
            # Returns a valid move from the passed list on the passed board.
            # Returns None if there is no valid move.
            possibleMoves = []
            for i in movesList:
                if isSpaceFree(board, i):
                    possibleMoves.append(i)

            if len(possibleMoves) != 0:
                return random.choice(possibleMoves)
            else:
                return None



        def computerMove(board, computerLetter):
            # Given a board and the computer's letter, determine where to move and return that move.
            if computerLetter == 'X':
                playerLetter = 'O'
            else:
                playerLetter = 'X'

             # Algorithm for the computers move
             # First, checking if computer can win in the next move
            for i in range(1, 10):
                copy = getBoardCopy(board)
                if isSpaceFree(copy, i):
                    handleTurn(copy, computerLetter, i)
                    if checkForWinner(copy, computerLetter):
                        return i


             # Check if the player could win on his next move, and blocking them.
            for i in range(1, 10):
                copy = getBoardCopy(board)
                if isSpaceFree(copy, i):
                    handleTurn(copy, playerLetter, i)
                    if checkForWinner(copy, playerLetter):
                        return i


             # Try to take the center, if it is free.
            if isSpaceFree(board, 5):
                return 5


             # Try to take one of the corners, if they are free.
            move = chooseRandomMove(board, [1, 3, 7, 9])
            if move != None:
                return move


             # Move on one of the sides.
            return chooseRandomMove(board, [2, 4, 6, 8])



        def playAgain():
            # Returns true if player wants to play again.
            u = input('Enter y to play again or press any other key to exit: ')
            if u == 'y' or u == 'Y':
                return True
            else:
                return False



        def isBoardFull(board):
            # Return True if every space on the board has been taken. Otherwise return False.
            for i in range(1, 10):
                if isSpaceFree(board, i):
                    return False
            return True


        # Asking the player to enter his/her name.
        name = input("Please enter your name: ")
        name = name.upper()



        while True:
            # Reset the board
            the_board = [' '] * 10     # setting up the main Tic Tac Toe board in variable named the_board.
            # selectPlayerLetter(), this function lets the player decide whether they want to be X or an O.
            playerLetter, computerLetter = selectPlayerLetter()
            turn = whoGoesFirst()

            # gameStillGoing variable keeps track of whether the game is still going on or if someone has won or the game is tied.
            gameStillGoing = True


            while gameStillGoing:
                if turn == 'player':
                    # Player's turn.
                    displayBoard(the_board)  # Printing the board in the output.
                    move = getPlayerMove(the_board)    # Letting the player enter their move.
                    handleTurn(the_board, playerLetter, move)  # handleTurn() adds players letter to the_board.

                    #Checking if the player has won.
                    if checkForWinner(the_board, playerLetter):
                        displayBoard(the_board)
                        print('CONGRATS!', name, ',YOU HAVE WON THE GAME.')
                        gameStillGoing = False

                    else:
                        #Checking if the game is tied.
                        if isBoardFull(the_board):
                            displayBoard(the_board)
                            print('The game is tied!')
                            break


                        # If the player hasn't won or tied the game then it will execute the code for computer's turn.
                        else:
                            turn = 'computer'


                else:
                    # Computer's turn.
                    move = computerMove(the_board, computerLetter)
                    handleTurn(the_board, computerLetter, move)


                    # Checking if the computer has won.
                    if checkForWinner(the_board, computerLetter):
                        displayBoard(the_board)
                        print('COMPUTER HAS WON! You lose.\nBETTER LUCK NEXT TIME,', name)
                        gameStillGoing = False

                    else:
                        # Checking if the game is tied
                        if isBoardFull(the_board):
                            displayBoard(the_board)
                            print('The game is tied!')
                            break


                        else:
                            turn = 'player'

            # Breaking from the loop if player does not want to play the game again.
            if playAgain():
                break
            else:
                print("Thankyou! for playing Tic Tac Toe")
                exit()
        break

    while u == multiplayer:
        print("\n\n--------WELCOME TO MULTI PLAYER GAME---------\n")
        # Ask players to enter their name
        player_1=input("Enter name of player1 :")
        player_1=player_1.upper()
        player_2=input("Enter name of player2 :")
        player_2=player_2.upper()

        # Display toss option
        # player_1 call first


        import random

        print("\n------TOSS------")

        print(player_1,"calls first")
        select_toss = input("Enter 1: for heads or  Enter 0: for tails: ")

        while True:
            if select_toss not in ['0' , '1'] :   # If input is not in 1 or 0, looping it until player enters valid input.
                select_toss = input("Incorrect input\nPlease Enter 1: for heads or Enter 0: for tails: ")
                continue
            break
            
        toss = random.randint(0, 1)
        if toss == 1:
            print("Heads came.")
        else:
            print("Tails came.")
        if toss == select_toss:
            print(player_1,"goes first")
            current_player = player_1
            former_player = player_2

        else:
            print(player_2," goes first")
            current_player = player_2
            former_player = player_1
        


        print("\n--------CHOOSE SYMBOL--------")

        s1="X"
        s2="O"
        while True:
            print(current_player," choose symbol x,o :", end = '')
            symbol=input()
            symbol = symbol.upper()
            print (symbol)
            if symbol != 'X' and symbol != 'O':
                print ("Wrong choice, ", end= '')
                continue
            break

        if symbol==s1 and current_player==player_1:
            a1=s1
            a2=s2
            print(current_player,"has ",a1,"\n",former_player,"has ",a2)


        elif symbol==s2 and current_player==player_1:
            a1=s2
            a2=s1
            print(current_player,"has ",a1,"\n",former_player,"has ",a2)


        elif symbol==s1 and current_player==player_2:
            a1=s1
            a2=s2
            print(current_player,"has ",a1,"\n",former_player,"has ",a2)




        elif symbol==s2 and current_player==player_2:
            a1=s2
            a2=s1
            print(current_player,"has ",a1,"\n",former_player,"has ",a2)







        n1,n2,n3,n4,n5,n6,n7,n8,n9=1,2,3,4,5,6,7,8,9

        print("\n\n----------GAME STARTED---------")

        print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
        count=0
        while count<=9 and count>=0 :
            count=count+1


            if (n1==n2==n3==a1) or (n4==n5==n6==a1) or (n7==n8==n9==a1) or (n1==n5==n9==a1) or (n3==n5==n7==a1) or (n1==n4==n7==a1) or (n2==n5==n8==a1) or (n3==n6==n9==a1):

                print(current_player,"CONGRAGULATIONS YOU WON")
                break


            elif (n1==n2==n3==a2) or (n4==n5==n6==a2) or (n7==n8==n9==a2) or (n1==n5==n9==a2) or (n3==n5==n7==a2) or (n1==n4==n7==a2) or (n2==n5==n8==a2) or (n3==n6==n9==a2):
                print(former_player,"CONGRAGULATIONS YOU WON")
                break

            if count% 2 != 0:
                print(current_player ,"your turn")
                move =input(" Enter 10 to quit the match.\n Enter your current position :")
                try:
                    move = int(move)
                except ValueError:
                    print("\nYou entered wrong input\n")
                    count=count-1
                    continue
                if move == 10:
                    break

                if move>9 or move<0:
                    count=count-1
                    print("Incorrect input given\n")
                    continue
                if move==1 and n1==1:
                    n1 = a1
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==1 and n1 !=1 :
                    print("This position is already occupied choose another option\n")
                    count=count-1
                    continue


                if move==2 and n2==2:
                    n2 = a1
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==2 and n2 !=2 :
                    print("This position is already occupied choose another option")
                    count=count-1
                    continue

                if move == 3 and n3==3:
                    n3 =a1
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==3 and n3 !=3 :
                     print("This position is already occupied choose another option")
                     count=count-1
                     continue

                if move == 4 and n4==4:
                    n4 = a1
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)

                elif move==4 and n4 !=4 :
                     print("This position is already occupied choose another option")
                     count=count-1
                     continue


                if move==5 and n5==5:
                    n5 =a1
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==5 and n5 !=5 :
                     print("This position is already occupied choose another option")
                     count=count-1
                     continue


                if move==6 and n6==6:
                    n6 = a1
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==6 and n6 !=6 :
                     print("This position is already occupied choose another option")
                     count=count-1
                     continue



                if move==7 and n7==7:
                    n7= a1
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==7 and n7 !=7 :
                    print("This position is already occupied choose another option")
                    count=count-1
                    continue


                if move == 8 and n8==8:
                    n8 = a1
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==8 and n8 !=8 :
                     print("This position is already occupied choose another option")
                     count=count-1
                     continue


                if move==9 and n9==9:
                    n9 = a1
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==9 and n9 !=9 :
                     print("This position is already occupied choose another option")
                     count=count-1
                     continue

            if count% 2 == 0:
                print(former_player," your turn")
                move=eval(input(" Enter 10 to quit the match.\n Enter your former position :"))
                if move==10:
                    break


                if move>9 or move<0:
                    count=count-1
                    print("incorrect input given")
                    continue


                if move==1 and n1==1:
                    n1 = a2
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)

                elif move==1 and n1 !=1 :
                    print("This position is already occupied choose another option")
                    count=count-1
                    continue

                if move==2 and n2==2:
                    n2 = a2
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==2 and n2 !=2 :
                     print("This position is already occupied choose another option")
                     count=count-1
                     continue


                if move==3 and n3==3:
                    n3 =a2
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==3 and n3 !=3 :
                     print("This position is already occupied choose another option")
                     count=count-1
                     continue


                if move==4 and n4==4:
                    n4 = a2
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==4 and n4 !=4 :
                     print("This position is already occupied choose another option")
                     count=count-1
                     continue


                if move==5 and n5==5:
                    n5 = a2
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==5 and n5 !=5 :
                     print("This position is already occupied choose another option")
                     count=count-1
                     continue


                if move==6 and n6==6:
                    n6 = a2
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==6 and n6 !=6 :
                     print("This position is already occupied choose another option")
                     count=count-1
                     continue


                if move==7 and n7==7:
                    n7 = a2
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==7 and n7 !=7 :
                     print("This position is already occupied choose another option")
                     count=count-1
                     continue

                if move==8 and n8==8:
                    n8 =a2
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==8 and n8 !=8 :
                     print("This position is already occupied choose another option")
                     count=count-1
                     continue


                if move==9 and n9==9:
                    n9 = a2
                    print("", n1, "|", n2, "|", n3, '\n', "----------", "\n", n4, "|", n5, "|", n6, "\n", "----------","\n",n7, "|", n8, "|", n9)
                elif move==9 and n9 !=9 :
                    print("This position is already occupied choose another option")
                    count=count-1
                    continue

            if count==9:
                print("----------GAME DRAW----------")
                break

        print("\n\nUser option selected if wants to play game again or wants to exit","\n","press n,N to exit","\n","press y,Y to play again")
        while True:
            u=input("Enter your option")
            if u=='y' or u=='Y':
                break
            elif u=='n' or u=='N':
                exit()
            else:
                print ("Wrong input, ", end='')
                continue
    
    if u == 'n' or u == 'N':
        print  ("End game")
        break

    print ("Thanks for playing again")
