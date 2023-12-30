class Card(object):

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

        #sets the blackjack value of the cards
        if rank == '2':
            self.value = 2
        elif rank == '3':
            self.value = 3
        elif rank == '4':
            self.value = 4
        elif rank == '5':
            self.value = 5
        elif rank == '6':
            self.value = 6
        elif rank == '7':
            self.value = 7
        elif rank == '8':
            self.value = 8
        elif rank == '9':
            self.value = 9
        elif rank == '10' or rank == 'Jack' or rank == "Queen" or rank == "King":
            self.value = 10
        elif rank == 'Ace':
            self.value = 11
    #retrieves rank
    def getRank(self):
        return self.rank

    #retrieves suit
    def getSuit(self):
        return self.suit

    #prints a string representation of the Card
    def getCard(self):
        return self.rank + " of " + self.suit



