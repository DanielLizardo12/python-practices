###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random

digits = list(range(10))
random.shuffle(digits)
randimized = (digits[:3])
print(randimized)
correct = False
print("Welcome to the random number game, i will think of a number of 3 digits")
print("You will try to guess te correct sequence of numbers, if one or more of")
print("the numbers you typed are close to the position one of the numbers i")
print("thoght then i'll say 'Close', if one or more of your numbers match the ")
print("correct position i'll say match, and if you guess all numbers correctly")
print("you will WIN THE GAME!... Good luck! :D")
print("press 'q' to quit")

def loppit(number, place):
    count = 0
    while count < 3:
        if int(randimized[count]) == int(number):
            if count == place:
                return 5
            else:
                return 1
        else:
            count += 1
    return 0


while correct == False:
    guess = input("Guess: ")

    if guess == "q":
        print("Bye :D")
        correct = True
    else:
        guess_array = (guess[0], guess[1], guess[2])
        guess_rate = 0
        guess_rate += loppit(guess_array[0], 0)
        guess_rate += loppit(guess_array[1], 1)
        guess_rate += loppit(guess_array[2], 2)



        if guess_rate == 15:
            print("You Won!")
            correct = True
        elif guess_rate > 4 and guess_rate < 14:
            print("Match")
        elif guess_rate > 0 and guess_rate < 4:
            print("Close")
        else:
            print("Nope")







# while correct == False:
#     guess = input("What is your guess? ")
#     for item in guess:
#         item =


# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
