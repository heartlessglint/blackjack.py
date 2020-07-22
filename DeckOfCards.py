import random

class Deck:
  def __init__(self, numberOfPlayers):
    self.numberOfPlayers = numberOfPlayers
  
  def createDeck(self): # change so makes whole deck. Nested for statment using list of names?
    suits = ["Heart", "Spade", "Dimond", "Club"]
    fullCards = []
    for suit in suits:
      for i in range(1, 12):
        if i == 1:
          fullCards.append(f"{suit} - Ace")
        elif i > 1 and i < 11:
          i = str(f'{suit} - {i}')
          fullCards.append(i)
        else:
          fullCards.extend((f"{suit} - Jack", f"{suit} - Queen", f"{suit} - King"))
    return fullCards

  def shuffle(self, deck):
    random.shuffle(deck)
    return deck

  def draw(self, deck):
    card = deck.pop(0)
    return card
