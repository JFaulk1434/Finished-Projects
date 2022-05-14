import sys
import time
import random

TYPESPEED = .025
rannum = 0
guesses = 0
name = ''
game = 0
score = 0
playagain = True


def getname():
    name = input(slowprint("\nWhat is your name? "))
    return name


def getgame():
    "returns game from input of player"
    game = 0
    print(
        slowprint(f'Hello {name.title()}, there are three different games to choose from: '))
    print(slowprint("1 - Guess the number between 1-10"))
    print(slowprint("2 - Guess the number between 1-100"))
    print(slowprint("3 - Guess the number between 1-1000"))
    while True:
        try:
            game = int(
                input(slowprint("Which game would you like to play? ")))
            print(slowprint(f'{name.title()}, you entered {game}'))
            if game < 1 or game > 3:
                if game < 1:
                    print(slowprint("I chose game 1 for you"))
                    game = 1
                else:
                    print(slowprint("I chose game 3 for you"))
                    game = 3
            break
        except:
            print(slowprint("Invalid entry: Must choose between 1 - 3"))
            continue

    return game


def slowprint(s):
    "prints like a person is typing"
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(TYPESPEED)
    return ""


def getnum(game):
    "returns random number based off game type: 1 = 1-10, 2 = 1-100, 3 = 1-1000"
    if game == 1:
        num = 10
    elif game == 2:
        num = 100
    else:
        num = 1000

    print(slowprint(
        f"I'm picking a number between 1 and {num}\nOk {name} I have my number and it's a good one. Good luck!"))
    randomnumber = random.randint(1, num)
    return randomnumber


def getguesscount(game):
    "returns amount of guesses based off game"
    if game == 1:
        guesses = 4
    elif game == 2:
        guesses = 10
    else:
        guesses = 20
    return guesses


def youwin(name, game, rannum, guesscount, playerguesses):
    print(slowprint(f'You did it {name.title()}!'))
    print(slowprint(
        f'You only had {guesses} chances to get my guess my number : {rannum}'))
    print(slowprint(f'You did it in {guesscount} guesses!!!'))
    print(slowprint(
        f'Your guesses where : {playerguesses}'))
    if game == 1:
        print(
            slowprint(f'Maybe next time {name.title()} you will try a harder challenge'))
    if game == 2:
        print(slowprint(
            f'Maybe next time {name.title()} you will try the hardest challenge'))
    if game == 3:
        print(slowprint(
            f'That was my hardest challenge {name.title()}. You are just to good for me!'))


def youlose(name, game, rannum, guesscount, playerguesses):
    print(slowprint(f'Oh, I\'m sorry {name.title()}, but you lose.'))
    print(slowprint(
        f'You had {guesses} chances to get my guess my number : {rannum}'))
    print(slowprint(
        f'You guessed {guesscount} times and still didn\'t guess my number'))
    print(slowprint(
        f'Your guesses where : {playerguesses}'))
    if game == 1:
        print(
            slowprint(f'Maybe next time {name.title()} you will try a harder challenge'))
    if game == 2:
        print(slowprint(
            f'Maybe next time {name.title()} you should try an easier challenge'))
    if game == 3:
        print(slowprint(
            f'That was my hardest challenge {name.title()}. you should try an easier challenge'))


def playgame():
    print(slowprint(f'You have {guesses} guesses to figure out my number'))
    guesscount = 0
    guess = None
    playerguesses = []
    while guesscount < guesses:
        try:
            guess = int(
                input(slowprint(f"Guess number {guesscount + 1}? ")))
            if guess > rannum:
                print(
                    slowprint(f'{guess} is higher than my number.'))
                playerguesses.append(guess)
                guesscount += 1
            elif guess < rannum:
                print(
                    slowprint(f'{guess} is lower than my number.'))
                playerguesses.append(guess)
                guesscount += 1
            else:
                break
        except:
            print(slowprint("Invalid Entry"))

    if guess == rannum:
        youwin(name, game, rannum, guesscount, playerguesses)
        guesscount = 0
    else:
        youlose(name, game, rannum, guesscount, playerguesses)
        guesscount = 0


while playagain == True:
    if name == '':
        name = getname()
    game = getgame()
    guesses = getguesscount(game)
    rannum = getnum(game)
    playgame()

    print(slowprint("Would you like to play again?"))
    while True:
        playerinp = input(slowprint('Enter y or n: '))
        if playerinp == 'y' or playerinp == 'Y':
            playagain = True
            break
        elif playerinp == 'n' or playerinp == 'N' or playerinp == 'quit' or playerinp == 'Quit':
            playagain = False
            break
        else:
            print(slowprint("Invalid Entry try again"))
            continue
