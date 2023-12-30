class Dealer:

    def __init__(self):
        self.dealertotal = 0
        self.dealercards = []
        self.hasblackjack = False

    #returns a list of strings showing player cards
    def getCards(self):
        i = 0
        dealer_cards = 'Dealer Cards: '
        while i < len(self.dealercards):
            dealer_cards += self.dealercards[i].getCard()
            dealer_cards += '. '
            i += 1
        return dealer_cards

    #adds the values of the cards in the dealer's hand
    def getDealerTotal(self):
        index = 0
        self.dealertotal = 0
        while index < len(self.dealercards):
            self.dealertotal += self.dealercards[index].value
            index += 1

    #checks dealer cards for blackjack
    def checkBlackjack(self):
        if self.dealercards[0].rank == 'Ace' and self.dealercards[1].value == 10:
            self.hasblackjack = True
        elif self.dealercards[1].rank == 'Ace' and self.dealercards[0].value == 10:
            self.hasblackjack = True
        else:
            self.hasblackjack = False
