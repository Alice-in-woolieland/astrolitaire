
import random

orderedDeck = []
deck = []

def generateDeck():
    for j in range(4):
        for i in range(13):
                orderedDeck.append([j, i])

def shuffleDeck():
     for i in range(len(orderedDeck)):
          card = random.choice(orderedDeck)
          deck.append(card)
          orderedDeck.remove(card)

def pullCard():
     card = deck[0]
     deck.remove(card)
     return card

def setTable(x = 7):
     shuffleDeck()
     table = []
     for i in range(x):
        table.append([])
        table[i].append(pullCard())

        
def printPretty(x):
    prettyCard = "「"
    card = x[0]
    if card[0] == 0:
        prettyCard += "♠ "
    elif card[0] == 1:
        prettyCard += "♡ "
    elif card[0] == 2:
        prettyCard += "♢ "
    elif card[0] == 3:
         prettyCard += "♣ "
    else:
         prettyCard += "⌧"
    if len(str(card[1]+1)) == 1: 
         prettyCard += " "
    prettyCard += str(card[1]+1)
    prettyCard += "」"
    return prettyCard
    

if __name__ == "__main__":
     generateDeck()
     setTable()

