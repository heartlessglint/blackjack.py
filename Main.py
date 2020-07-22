from DeckOfCards import Deck
from Computer import Computer
from Human import Player
import re

class Game(Computer, Deck, Player):
  def __init__(self):
    pass

  def buildDeck():
    game = Deck("1")
    deck = game.createDeck()
    shuffled = game.shuffle(deck)
    return shuffled

  def totalInHand(self, computer):
    types = ("King", "Queen", "Jack", "Ace") #Ace can be one or 11, need to add in #somewhere for it to split as needed (show both options) Do after completed
    stringOfHand = " ".join(computer)
    numbersInHand = re.findall(r'(\d+)', stringOfHand)
    for items in types:
      X = re.findall(items, stringOfHand)
      numbersInHand.extend(X)
    for pos, number in enumerate(numbersInHand):
      if number in types:
        numbersInHand[pos] = 10
    totalHand = 0
    for items in numbersInHand:
      totalHand = totalHand + int(items)
    return totalHand

  def checkIfBust(self, total):
    print(f'The dealer says:\n"Your total is {total}"')
    if total == 21:
      print('"You have 21 well done"')
    elif total < 21:
      print('"You can draw another card if you want"')
    else:
      print('"You have gone bust"')
  
  def loop(self, choice, test, shuffled):
    while choice:
      test = Computer.drawCardLoop(self, choice, test, shuffled)
      total = self.totalInHand(test)
      choice = Computer.drawCardChoice(self, total)

  def computerPlay(self):
    shuffled = Game.buildDeck()
    computer = Computer("1")
    test = computer.start(shuffled)
    print(f"The computers opening hand is {test}")
    game = Game()
    total = game.totalInHand(test)
    game.checkIfBust(total)
    choice = game.drawCardChoice(total)
    game.loop(choice, test, shuffled)




Game().computerPlay()

#shuffled = Game.buildDeck()
