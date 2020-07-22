#leave until understand inheritance first 
from DeckOfCards import Deck

class Player(Deck):
  def __init__(self):
    pass
  
  def start(self, deck):
    hand = []
    while len(hand) < 2:
      card = self.draw(deck)
      hand.append(card)
    return hand
  
  def validInput(self, choice):
    while choice != "y" or choice != "yes" or choice != "n" or choice != "no":
      choice = input("Please choose Y/N: ")
  
  def drawCard(self, hand, total):
    print(f'Your hand is: {hand}')
    print(f'Your total is: {total}')
    choice = input("Do you want to draw a card? Y/N").lower()
    choice = self.validInput(choice)
    if choice == "n" or choice == "no":
      return False
    elif choice == "y" or choice == "yes":
      card = self.draw(deck)
      hand.append(card)
      return True, hand
