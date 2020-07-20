class Computer(Deck.Deck):
  def __init__(self, number):
    self.number = number


  def start(self, deck):
    hand = []
    card = self.draw(deck)
    hand.append(card)
    return hand

computer = Computer("1")

test = computer.start(shuffled)

print(test)
