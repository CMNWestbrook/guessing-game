# Put your code here
import random

print "Hi Friend!"

player = raw_input("What is your name? ")

ran_num = random.randint(1,100)

print ran_num

print "Hi, " + player + ". I am thinking of a number between 1 and 100."
print "Try to guess my number."

guess = raw_input("What number do you guess?")

if guess > ran_num:
    print "Your number is too big!"