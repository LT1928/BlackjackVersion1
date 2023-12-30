from Cards import Card
import random

class DecksofCards():

    #constructor for the creation of a shoe of cards
    def __init__(self,numofdecks):
        deck = []
        while(numofdecks>0):
            count = 0
            ranklist = ['Ace','King','Queen','Jack','10','9','8','7','6','5','4','3','2']
            while count < 13:
                deck.append(Card(ranklist[count],'Spades'))
                deck.append(Card(ranklist[count],'Hearts'))
                deck.append(Card(ranklist[count],'Diamonds'))
                deck.append(Card(ranklist[count],'Clubs'))
                count += 1
            numofdecks -= 1
        self.deck = deck

    #shuffle method for decks
    def shuffle(self):
        i = 0
        while i < 2000:
            index = random.randint(0,len(self.deck)-1)
            x = self.deck[index]
            self.deck.remove(x)
            self.deck.append(x)
            i += 1

    def getDeck(self):
        i = 0
        deck = []
        while i < len(self.deck):
            deck.append(self.deck[i].getCard())
            i += 1
        return deck
