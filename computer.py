from DeckOfCards import Deck

class Computer(Deck):
  def __init__(self, number):
    self.number = number


  def start(self, deck):
    hand = []
    while len(hand) < 2:
      card = self.draw(deck)
      hand.append(card)
    return hand
