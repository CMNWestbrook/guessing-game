# Put your code here
import random

print "Hi Friend!"

player = raw_input("What is your name? ")

ran_num = random.randint(1, 100)

print ran_num

print "Hi, %s. I am thinking of a number between 1 and 100." % player
print "Try to guess my number. "

while True: 
    try:
        guess = int(raw_input("What number do you guess? "))
        break
    except ValueError:
        print "You did not enter an integer"

tries = 1


while guess != ran_num:
    if guess < 2 or guess > 99:
        side = "out of range"
    elif guess > ran_num:
        side = "big"
    elif guess < ran_num:
        side = "small"

    print "Your number is too %s!" % side
    guess = int(raw_input("What number do you guess? "))
    tries = tries + 1

print "You got it in %d attemps" % tries

