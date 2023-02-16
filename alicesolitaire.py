
import random

orderedDeck = []
deck = []

''' code i dont wanna delete

     secretTable = cleanTable(table)
     for i in range(len(secretTable)):
        li = ""
        for j in range(len(secretTable[i])):
            li += printPretty(secretTable[i],j)
        print(li)

             global properTable
     properTable = []
     for i in range(len(secretTable)): #rendered table
          properTable.append([])
          for j in range(i+1):
               properTable[i].append([4, 13])
     renderTable(properTable)
'''

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
     global secretTable
     secretTable = []
     for i in range(x): #cards that are hidden
        secretTable.append([])
        for j in range(i+1):
            secretTable[i].append(pullCard())
     global shownTable
     shownTable = []
     for i in range(x): ##shown cards
          shownTable.append([])
          for j in range(5):
               shownTable[i].append(pullCard())
     global properTable
     properTable = []
     for i in range(len(secretTable)): ##adding secret table
          properTable.append([])
          for j in range(i+1):
               properTable[i].append([4, 13])
     for i in range(len(shownTable)): ##adding shown table
          for j in range(len(shownTable[i])):
               properTable[i].append(shownTable[i][j])
     renderTable(properTable)

def renderTable(x):
     for i in range(len(x)):
          li = ""
          counter = 0
          for j in range(len(x[i])):
               if printPretty(x[i], j) == "「****」":
                    counter += 1
               else:
                    li += printPretty(x[i],j)
          if counter != 0:
               li = "「* " + str(counter) + "*」" + li
          print(li)

             
def cleanTable(x):
    ##reversing table
    tableFlipped = []
    tableSet = []
    for i in range(len(x)):
         for j in range(len(x[i])):
            tableFlipped.append([])
    for i in range(len(x)):
         for j in range(len(x[i])):
                print("i", i, "|j", j)
                print(x[j][i])
                tableFlipped[j].append(x[j][i])    
    ##now flipping table
    for i in reversed(range(len(tableFlipped))):
        prettyRow = []
        for j in range(len(tableFlipped[i])):
            prettyRow.append(tableFlipped[i])
        tableSet.append(prettyRow[i])
    return tableSet

def showRow(x):
     y = int(x)
     for i in range(len(shownTable[y])):
          print(y)
          printPretty(shownTable[y], i)
          print(i)


def printPretty(x, p=0):
    prettyCard = "「"
    card = x[p]
    if card[0] == 0:
        prettyCard += "♠ "
    elif card[0] == 1:
        prettyCard += "♡ "
    elif card[0] == 2:
        prettyCard += "♢ "
    elif card[0] == 3:
         prettyCard += "♣ "
    elif card[0] == 4:
         prettyCard += "**"
    else:
         prettyCard += "⌧"
    if card[1] == 13:
         prettyCard += "**」"
         return prettyCard
    elif len(str(card[1]+1)) == 1: 
         prettyCard += " "
    prettyCard += str(card[1]+1)
    prettyCard += "」"
    return prettyCard

def startGame():
     print("Pick a row [1:6]")
     rowInput = input("?")
     showRow(rowInput)
     print("Pick a col")

if __name__ == "__main__":
     generateDeck()
     setTable(6)
     startGame()

