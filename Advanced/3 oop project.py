#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """


    def __init__(self, user):
        self.user = user
        print("CREATING DECK")


    def create_deck(self):
        new_deck = []
        for item in SUITE:
            for number in RANKS:
                new_deck.append(item + "_" + number)

        shuffle(new_deck)
        splited_deck = [new_deck[:26], new_deck[26:]]

        if self.user == 1:
            return splited_deck[0]
        elif self.user == 2:
            return splited_deck[1]





class Hand(Deck):
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''



    def add_card(self, deck, new_card, user_card):
        deck.append(user_card)
        deck.append(new_card)
        deck.pop(0)
        return deck


    def remove_card(self, deck):
        deck.pop(0)
        return deck




class Player():
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    pass



def convert(num):
    if num == "J":
        return 11
    elif num == "Q":
        return 12
    elif num == "K":
        return 13
    elif num == "A":
        return 14
    else:
        return int(num)


def compare(num1, num2):
    computer_c = convert(num1)
    player_c = convert(num2)

    if computer_c > player_c:
        return "computer"
    elif player_c > computer_c:
        return "player"
    else:
        return "tie"
######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
deck_1 = Hand(1)
deck_2 = Hand(2)
player_deck = deck_1.create_deck()
computer_deck = deck_2.create_deck()
# print(player_deck[0].split("_")[1])
# print(computer_deck[0].split("_")[1])

# print(len(player_deck))

keep_playing = input("next play")
num = 0
count = 1

while keep_playing == "":
    player_card = player_deck[num]
    computer_card = computer_deck[num]
    player_num = convert(player_card.split("_")[1])
    computer_num = convert(computer_card.split("_")[1])
    print("-------------------------------------------------")
    print("Round number: ", count)
    print("-------------------------------------------------")
    print("you have " , len(player_deck) , " cards")
    print("the computer has " , len(computer_deck) , " cards")
    print("your card is: " + player_card)
    print("computers card is: " + computer_card)
    print("-------------------------------------------------")


    comparing = compare(computer_num, player_num)


    if comparing == "computer":
        for item in computer_deck[:num + 1]:
            computer_deck = deck_2.add_card(computer_deck, player_card, computer_card)
            player_deck = deck_1.remove_card(player_deck)
        num = 0
        print("Computer won this round")
        print("-------------------------------------------------")
        print()
    elif comparing == "player":
        for item in computer_deck[:num + 1]:
            player_deck = deck_1.add_card(player_deck, computer_card, player_card)
            computer_deck = deck_2.remove_card(computer_deck)
        num = 0
        print("You won this round")
        print("-------------------------------------------------")
        print()
    else:
        num += 3
        print("WARRRRRRRRRRRRRRRRRRRR")
        if len(player_deck) <= num:
            print("You Lose!!!")
        elif len(computer_deck) <= num:
            print("You Won!!!")





    if len(player_deck) == 0:
        print ("You Lose!!!")
        break
    elif len(computer_deck) == 0:
        print("You Won!!!")
        break


    count += 1
    keep_playing = input("next play")















# player_deck = deck_1.add_card(player_deck, "C_A")
# print(player_deck)
# computer_deck = deck_2.add_card(player_deck, "H_A")
# print(player_deck)












# Use the 3 classes along with some logic to play a game of war!
