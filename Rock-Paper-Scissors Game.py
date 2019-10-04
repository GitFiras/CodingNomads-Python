'''
Rock-Paper-Scissors Game
Code a game of rock paper scissors.

Instructions
take in a number 0-2 from the user that represents their hand
generate a random number 0-2 to use for the computer's hand
call the function get_hand to get the string representation of the user's hand
call the function get_hand to get the string representation of the computer's hand
call the function determine_winner to figure out who won
print out the player hand and computer hand
print out the winner

Some Tips
Creating a function that gets a "hand" based on a number.

The function should take in a number and return the string representation of the hand. E.g.:

def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper

    # for example if the variable hand is 0, it should return the string "scissor"
    pass

'''
import random
user_input = input("Welcome to a game of Rock-Paper-Scissors! Please choose a number from the following three: 0, 1, 2: ")
comp_input = randint(0,2)

def get_hand(user_input):
    scissor = 0
    rock = 1
    paper = 2
#    hand_user = user_input
    return

def get_hand(comp_input):
    comp_input = randint(0,2)
    return comp_input

def determine_winner(input_):
    #boolean

print("Your input is: ",get_hand(user_input))
print("The computer's input is: ",get_hand(comp_input))
print("And the winner is: ",determine_winner(input_))