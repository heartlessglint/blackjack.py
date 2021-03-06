from DeckOfCards import Deck
import random

class Computer(Deck):
  def __init__(self, number):
    self.number = number


  def start(self, deck):
    hand = []
    while len(hand) < 2:
      card = self.draw(deck)
      hand.append(card)
    return hand

  def drawCardChoice(self, total):
    print(f'My current total is {total}')
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
    elif total == 15 and random.randint(1,101) > 30:
      print("There is a little risk, but I'm feeling lucky, I'll draw")
      return True
    elif 11 < total < 15 and random.randint(1,101) > 20:
      print("It's a small risk, so I'll do it")
      return True
    elif total <= 11:
      print("There is not risk, I will draw")
      return True
    else:
      print("I will not draw.")
      return False

  def drawCardLoop(self, choice, hand, currentDeck):
    if choice:
      card = self.draw(currentDeck)
      hand.append(card)
    print(f"My new hand is {hand}")
    return hand
