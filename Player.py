class Player:

    def __init__ (self,stacksize):
        self.stack = int(stacksize)
        self.playercards1 = []
        self.playercards2 = []
        self.playercards3 = []
        self.playercards4 = []
        self.hasblackjack = False
        self.playerbet1 = 0
        self.playerbet2 = 0
        self.playertotal1 = 0
        self.playertotal2 = 0

    def getCards(self,hand):
        i = 0
        player_cards = 'Player Cards: '
        while i < len(hand):
            player_cards += hand[i].getCard()
            player_cards += '. '
            i += 1
        return player_cards

    #adds the values of the cards in the player's hand
    def getPlayerTotal(self,splithandnumber):
        index1 = 0
        index2 = 0
        handtotal = 0
        if splithandnumber == 1:
            while index1 < len(self.playercards1):
                handtotal += self.playercards1[index1].value
                index1 += 1
            return handtotal

        elif splithandnumber == 2:
            while index2 < len(self.playercards2):
                handtotal += self.playercards2[index2].value
                index2 += 1
            return handtotal

    #checks player cards for blackjack
    def checkBlackjack(self):
        if self.playercards1[0].rank == 'Ace' and self.playercards1[1].value == 10:
            return True
        elif self.playercards1[1].rank == 'Ace' and self.playercards1[0].value == 10:
            return True
        else:
            return False

