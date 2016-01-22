import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print('I don not know such name ' + name)
    return number

def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print('There are not matching number')
    return name


def rpsls(player_choice):
    print ""
    print('Player chooses ' + player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choise = number_to_name(comp_number)
    print('Computer chooses ' + comp_choise)
    delta = player_number - comp_number
    if delta < 0:
        delta = delta + 5
        if delta == 1 or delta == 2:
            winner = player_number
            print('Player wins!')
        elif delta == 3 or delta == 4:
            winner = comp_number
            print('Computer wins!')
    elif delta == 0:
        winner = None
        print('No winner sorry')
    else:
        if delta == 1 or delta == 2:
            winner = player_number
            print('Player wins!')
        elif delta == 3 or delta == 4:
            winner = comp_number
            print('Computer wins!')
    return winner
