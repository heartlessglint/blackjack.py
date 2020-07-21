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

  def drawCard(self, total):
    if total == 21:
      print("I have 21, I will not draw")
      return False
    elif total > 21:
      print("I have lost, what a shame")
      return False
    elif 19 < total < 21:
      print("I am too close, I will not go again")
      return False
    elif total == 18 and random.randint(1,101) > 95:
      print("Very risky, but I'll take one")
      return True
    elif total == 17 and random.randint(1,101) > 80:
      print("I'll go for the risk, give me a card")
      return True
    elif total == 16 and random.randint(1,101) > 50:
      print("Risky, but I'll take another")
      return True
