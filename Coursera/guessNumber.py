# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

counter = 7
range = 'range is from 1 to 100'

#secret_number = random.randrange(0,100)


# helper function to start and restart the game
def new_game():
    
    global counter
    global range
    print 'New game. The', range
    print 'Number of remaining attempts is', counter
    counter = 7
    global secret_number
    secret_number = random.randrange(0,100)
    

       
    
    
def attempt_counter():
    global counter
    counter = counter - 1
    print 'Number of remaining attempts is', counter
   


def range100():
    new_game()
    global range
    range = 'from 1 to 100'
    global secret_number
    secret_number = random.randrange(0,100)
    
    

    
    

def range1000():   
    global range
    range = 'the range is from 1 to 1000'
    new_game()
    global secret_number
    secret_number = random.randrange(0,1000)
    
    
def input_guess(guess):
    inp = int(guess)
    print 'Guess was', guess
    if counter > 1:
        if inp > secret_number:
            print 'Lower!'
            attempt_counter()
        elif inp < secret_number:
            print 'Higher!'
            attempt_counter()
        else:
            print 'Correct!'
    else:
        print 'Geme over, dude!'
        new_game()
   

    
# create frame
frame = simplegui.create_frame('Guess The Number', 300, 200)
button_up_to_100 = frame.add_button('Range is [0 - 100)',range100, 200)
button_up_to_1000 = frame.add_button('Range is [0 - 1000)',range1000, 200)
inp = frame.add_input('Enter a guess', input_guess, 200)
frame.start


# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
