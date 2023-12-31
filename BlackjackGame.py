from DeckofCards import DecksofCards
from Player import Player
from Dealer import Dealer

class BlackjackGame:
    #constructs a blackjack game
    def __init__(self,numofdecks,playerstack):
        self.numofdecks = numofdecks
        shoe = DecksofCards(self.numofdecks)
        shoe.shuffle()
        self.shoe = shoe
        self.player1 = Player(playerstack)
        self.dealer = Dealer()
        self.splitstatus = False
        self.splithandnumber = 1
        self.hitcount = 0
    #prints out the current cards in the shoe
    def getShoe(self):
        return self.shoe.getDeck()

    #deals the starting cards of the hand to player and dealer
    def startdeal(self,playerbet):
        #takes in player's bet
        self.player1.stack -= playerbet
        self.player1.playerbet1 = playerbet

        card0 = self.shoe.deck[0]
        card1 = self.shoe.deck[1]
        card2 = self.shoe.deck[2]
        card3 = self.shoe.deck[3]

        #deals out cards to player and dealer
        self.shoe.deck.remove(card0)
        self.shoe.deck.remove(card1)
        self.shoe.deck.remove(card2)
        self.shoe.deck.remove(card3)

        self.player1.playercards1.append(card0)
        self.dealer.dealercards.append(card1)
        self.player1.playercards1.append(card2)
        self.dealer.dealercards.append(card3)

    def takeInsurance(self):
        if self.dealer.checkBlackjack() == True:
            self.player1.stack += 3 * self.player1.playerbet1
            print("Insurance Wins! \nPlayer Stack: " + str(self.player1.stack))
        if self.dealer.checkBlackjack() == False:
                print("Insurance loses. \nPlayer Stack: " + str(self.player1.stack))

    def checkBlackjack(self):
        self.player1.hasblackjack = self.player1.checkBlackjack()
        self.dealer.hasblackjack = self.dealer.checkBlackjack()

        #checks and pays out blackjacks
        if self.dealer.hasblackjack == True and self.player1.hasblackjack == False:
            print("Dealer has Blackjack and Player Loses")
        elif self.dealer.hasblackjack == True and self.player1.hasblackjack == True:
            print("Both Player and Dealer have Blackjack, Player pushes")
            self.player1.stack += self.player1.playerbet1
        elif self.dealer.hasblackjack == False and self.player1.hasblackjack == True:
            print("Player has Blackjack!")
            self.player1.stack += 2.5 * self.player1.playerbet1

        #automatically adjusts value of ace from 11 to 1 for Ace Ace starting hand
        if self.player1.playercards1[0].rank == 'Ace' and self.player1.playercards1[1].rank == 'Ace':
            self.player1.playertotal1 = 12
        else:
            self.player1.playertotal1 = self.player1.playercards1[0].value + self.player1.playercards1[1].value

        if self.dealer.dealercards[0].rank == 'Ace' and self.dealer.dealercards[1].rank == 'Ace':
            self.dealer.dealertotal = 12
        else:
            self.dealer.dealertotal = self.dealer.dealercards[0].value + self.dealer.dealercards[1].value


        #prints the dealer's cards and player's cards
        print("Dealer upcard: " + self.dealer.dealercards[1].getCard() + "\nYour cards: " + self.player1.playercards1[0].getCard() + ", " + self.player1.playercards1[1].getCard() + "\nYour total: " + str(self.player1.playertotal1))


    #creates a hit player for the player
    def playerHit(self,currenthand):
        hitcard = self.shoe.deck[0]
        self.shoe.deck.remove(hitcard)
        currenthand.append(hitcard)
        #updates player total
        if self.splithandnumber == 1:
            self.player1.playertotal1 = self.player1.getPlayerTotal(1)
        if self.splithandnumber == 2:
            self.player1.playertotal2 = self.player1.getPlayerTotal(2)

        #makes sure that aces do not bust the player
        index = 0
        while index < len(currenthand) and self.player1.playertotal1 > 21:
            if currenthand[index].rank == 'Ace':
                currenthand[index].value = 1
            index += 1
            if self.splithandnumber == 1:
                self.player1.playertotal1 = self.player1.getPlayerTotal(1)
            if self.splithandnumber == 2:
                self.player1.playertotal2 = self.player1.getPlayerTotal(2)

    #creates double down for the player
    def playerDoubleDown(self,bet):
        self.player1.stack -= bet
        if self.splithandnumber == 1:
            self.player1.playerbet1 = bet * 2
        if self.splithandnumber == 2:
            self.player1.playerbet2 = bet * 2

    #creates a split for player
    def playerSplit(self):
        self.splitstatus = True
        self.player1.playerbet2 = self.player1.playerbet1
        self.player1.stack -= self.player1.playerbet2
        print("Player Stack: " + str(self.player1.stack))
        self.player1.playercards2 = [self.player1.playercards1.pop()]
        self.player1.playercards1.append(self.shoe.deck.pop())
        self.player1.playercards2.append(self.shoe.deck.pop())
        print("Hand 1 After Splitting: ")
        print(self.player1.getCards(self.player1.playercards1))
        print("Hand 2 After Splitting: ")
        print(self.player1.getCards(self.player1.playercards2))

    #creates a stand for the player
    def playerStand(self):
        print("Player Stands")

    #decisions for dealer
    def dealerHit(self):

        while self.dealer.dealertotal < 17 and (self.player1.playertotal1 <= 21 or self.player1.playertotal2 <= 21) and self.player1.hasblackjack == False and self.dealer.hasblackjack == False:
            hitcard = self.shoe.deck[0]
            self.shoe.deck.remove(hitcard)
            self.dealer.dealercards.append(hitcard)
            #updates the dealer total
            self.dealer.getDealerTotal()

            #makes sure that aces do not bust the dealer
            index = 0
            while index < len(self.dealer.dealercards) and self.dealer.dealertotal > 21:
                if self.dealer.dealercards[index].rank == 'Ace':
                    self.dealer.dealercards[index].value = 1
                index += 1
                self.dealer.getDealerTotal()

            print(self.dealer.getCards())
            print("Dealer Total: " + str(self.dealer.dealertotal))

    #posts results of the blackjack hand
    def payout(self):

        #pays out for the player's first hand
        if self.dealer.dealertotal > 21 and self.player1.playertotal1 <= 21:
            print("Dealer busts and Player wins " + str(2*self.player1.playerbet1) + " on Hand 1.")
            self.player1.stack += 2*self.player1.playerbet1
        elif self.dealer.dealertotal <= 21 and self.dealer.dealertotal < self.player1.playertotal1 and self.player1.playertotal1 <= 21:
            print("Player wins " + str(2*self.player1.playerbet1) + " on Hand 1.")
            self.player1.stack += 2*self.player1.playerbet1
        elif self.dealer.dealertotal == self.player1.playertotal1:
            print("Player pushes on Hand 1.")
            self.player1.stack += self.player1.playerbet1
        elif self.dealer.dealertotal <= 21 and self.dealer.dealertotal > self.player1.playertotal1:
            print("Dealer Wins on Hand 1.")

        #pays out for the player's second hand
        while self.splitstatus == True:
            if self.dealer.dealertotal > 21 and self.player1.playertotal2 <= 21:
                print("Dealer busts and Player wins " + str(2*self.player1.playerbet2) + " on Hand 2.")
                self.player1.stack += 2*self.player1.playerbet2
            elif self.dealer.dealertotal <= 21 and self.dealer.dealertotal < self.player1.playertotal2 and self.player1.playertotal2 <= 21:
                print("Player wins " + str(2*self.player1.playerbet2) + " on Hand 1.")
                self.player1.stack += 2*self.player1.playerbet2
            elif self.dealer.dealertotal == self.player1.playertotal2:
                print("Player pushes on Hand 1.")
                self.player1.stack += self.player1.playerbet2
            elif self.dealer.dealertotal <= 21 and self.dealer.dealertotal > self.player1.playertotal2:
                print("Dealer Wins on Hand 2.")
            self.splitstatus = False

    #clears both player and dealer hands for next round
    def clearHands(self):
        self.player1.playercards1 = []
        self.player1.playercards2 = []
        self.dealer.dealercards = []




