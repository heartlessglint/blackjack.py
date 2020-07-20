import Deck
#currently doesn't work (see comment at line 16)

class Computer(Deck.Deck):
  def __init__(self, number):
    self.number = number

  def start(deck):
    hand = []
    card = Deck.Deck.draw(deck)
    hand.append(card)
    print(hand)

computer = Computer("1")

test = computer.start(shuffled) #if "shuffled" there(taken from main example) it says has too many arugments. If not there says doesn't have enough

print(test)
