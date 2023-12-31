from BlackjackGame import BlackjackGame

#creates the game and starting stack
buyin = int(input("Select your buy-in: "))
game1 = BlackjackGame(2,buyin)
print("Player Stack: " + str(game1.player1.stack))

#game continues until either the player runs out of money or the deck runs out of cards
while game1.player1.stack > 0 and len(game1.shoe.deck) > 10:
    #var to make sure players are not allowed to double after hitting
    game1.hitcount = 0

    #initializes the bet by taking in player's bet and dealing the cards
    playerbet = int(input("Select your bet: "))
    game1.startdeal(playerbet)

    #allows player to take insurance if Dealer has an Ace upcard
    if game1.dealer.dealercards[1].rank == 'Ace':
        insurancechoice = input("Would you like to take insurance?: ")
        if insurancechoice == 'Yes':
            game1.player1.stack -= playerbet
            game1.takeInsurance()
        elif insurancechoice == 'No':
            pass
    game1.checkBlackjack()

    #actions for the player if no blackjack is present
    while game1.player1.playertotal1 <= 21 and game1.player1.hasblackjack == False and game1.dealer.hasblackjack == False:
        playerdecision = input("What is your decision?: ")
        game1.splithandnumber = 1
        #Player hits
        if playerdecision == 'Hit':
            game1.playerHit(game1.player1.playercards1)
            if game1.player1.playertotal1 > 21:
                print(game1.player1.getCards(game1.player1.playercards1))
                print("Player total is " + str(game1.player1.playertotal1) + " and Player Busts" + "\nStack Size:" + str(game1.player1.stack))
            else:
                game1.hitcount += 1
                print(game1.player1.getCards(game1.player1.playercards1))
                print("Player total is " + str(game1.player1.playertotal1))

        #checks to make sure double is allowed
        elif playerdecision == 'Double' and game1.hitcount != 0:
            print("Doubling down after hitting is not allowed.")

        #Player doubles down
        elif playerdecision == 'Double' and game1.hitcount == 0:
            game1.playerDoubleDown(playerbet)
            game1.playerHit(game1.player1.playercards1)
            print(game1.player1.getCards(game1.player1.playercards1))
            print("Player total is " + str(game1.player1.playertotal1))
            break

        #Player Stands
        elif playerdecision == 'Stand':
            break

        #determines if split is allowed
        elif playerdecision == 'Split' and game1.player1.playercards1[0].value != game1.player1.playercards1[1].value:
            print("Splitting two different cards is not allowed.")

        #Player splits
        elif playerdecision == 'Split':
            game1.playerSplit()
            game1.player1.playertotal1 = game1.player1.getPlayerTotal(1)
            if game1.player1.playercards1[0].rank == 'Ace' and game1.player1.playercards1[1].rank == 'Ace':
                game1.player1.playertotal1 = 12
            #determines the player's series of actions on the first hand
            while game1.player1.playertotal1 <= 21:
                playersplit1decision = input("What is your decision for Hand 1 after split?: ")
                #Player hits on the first hand
                if playersplit1decision == 'Hit':
                    game1.playerHit(game1.player1.playercards1)
                    if game1.player1.playertotal1 > 21:
                        splithandnumber = 2
                        game1.splithandnumber = splithandnumber
                        print(game1.player1.getCards(game1.player1.playercards1))
                        print("Player total is " + str(game1.player1.playertotal1) + " on Hand 1 and Player Busts" + "\nStack Size: " + str(game1.player1.stack))
                    else:
                        print(game1.player1.getCards(game1.player1.playercards1))
                        print("Player total is " + str(game1.player1.playertotal1) + " on Hand 1")

                #Player doubles down on the first hand
                elif playersplit1decision == 'Double':
                    game1.playerDoubleDown(playerbet)
                    game1.playerHit(game1.player1.playercards1)
                    print(game1.player1.getCards(game1.player1.playercards1))
                    print("Player total is " + str(game1.player1.playertotal1) + " on Hand 1")
                    splithandnumber = 2
                    game1.splithandnumber = splithandnumber
                    break

                #Player stands on the first hand after split
                elif playersplit1decision == 'Stand':
                    print("Player total is " + str(game1.player1.playertotal1) + " on Hand 1")
                    splithandnumber = 2
                    game1.splithandnumber = splithandnumber
                    break

            #determines the player's series of actions on the second hand
            if game1.player1.playercards2[0].rank == 'Ace' and game1.player1.playercards2[1].rank == 'Ace':
                game1.player1.playertotal2 = 12
            game1.player1.playertotal2 = game1.player1.getPlayerTotal(2)
            while game1.player1.playertotal2 <= 21:
                playersplit1decision = input("What is your decision for Hand 2 after split?: ")

                #Player hits on the first hand
                if playersplit1decision == 'Hit':
                    game1.playerHit(game1.player1.playercards2)
                    if game1.player1.playertotal2 > 21:
                        print(game1.player1.getCards(game1.player1.playercards2))
                        print("Player total is " + str(game1.player1.playertotal2) + " on Hand 2 and Player Busts" + "\nStack Size: " + str(game1.player1.stack))
                    else:
                        print(game1.player1.getCards(game1.player1.playercards2))
                        print("Player total is " + str(game1.player1.playertotal2))

                #Player doubles down on the first hand
                elif playersplit1decision == 'Double':
                    game1.playerDoubleDown(playerbet)
                    game1.playerHit(game1.player1.playercards2)
                    print(game1.player1.getCards(game1.player1.playercards2))
                    print("Player total is " + str(game1.player1.playertotal2) + " on Hand 2")
                    break

                #Player stands on the first hand
                elif playersplit1decision == 'Stand':
                    print("Player total is " + str(game1.player1.playertotal2) + " on Hand 2")
                    break
            break
        else:
            print("Please pick a valid action")

    #prints the dealer's cards and hits the dealer hand until its value is over 17 or the hand busts
    print(game1.dealer.getCards())
    print("Dealer Total: " + str(game1.dealer.dealertotal))
    game1.dealerHit()

    #pays out players when blackjack is not present
    if game1.player1.hasblackjack != True and game1.dealer.hasblackjack != True:
        game1.payout()
    print("Player Stack: " + str(game1.player1.stack))
    game1.clearHands()

print("End of shoe.")









