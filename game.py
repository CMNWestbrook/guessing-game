# Put your code here
import random

print "Hi Friend!"

player = raw_input("What is your name? ")

ran_num = random.randint(1,100)

print ran_num

print "Hi, " + player + ". I am thinking of a number between 1 and 100."
print "Try to guess my number."


guess = int(raw_input("What number do you guess?"))

while (guess != ran_num):
    if (guess > ran_num):
        print "Your number is too big!"
        guess = int(raw_input("What number do you guess?"))
    elif (guess < ran_num):
        print "Your number is too small!"
        guess = int(raw_input("What number do you guess?"))

print "You got it"
