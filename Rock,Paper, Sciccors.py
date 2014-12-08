#Tony & Tavonga
#04/12/2014
#Rock,Paper,Scissors

import random

#Functions

#loop in for
def loop():
    won = 0
    for count in range(1,5):
        #generate number
        random_number = random.randrange(0,3)
        if random_number == 1:
            computer = "Rock"
        elif random_number == 2:
            computer = "Paper"
        else:
            computer = "Scissors"
        #Ask User for Answer
        human_guess = input("Please enter your guess(Rock, Paper, Scissors): ")
        print()
        human_guess = human_guess.upper()
        human_guess = human_guess[0]
        if human_guess == "R":
            human_guess = "Rock"
        elif human_guess == "P":
            human_guess = "Paper"
        elif human_guess == "S":
            human_guess = "Scissors"
        else:
            print("You have entered a invalid guess")
        #Check if Answer is correct
        if human_guess == computer:
            won = won + 1
            print("You guessed correctly, Well done!")
            print("So far you have guessed {0} correct".format(won))
            print()
        else:
            print("You have not guessed the right answer, the right answer was {0}".format(computer))
            print("So far you have guessed {0} correct".format(won))
            print()
    return won

#Check if won
def check_if_won(won):
    if won >= 3:
        print("You have beaten the computer")
        print("Can you beat it again?")
        print()
    else:
        print("The computer beat you, Try again")
        print()
    print("Thank you for Playing")


#main
def main():
    user_name = input("Please enter your name: ")
    print("Rock, Paper, Scissors Game -(Best of five games)")
    print("Rock breaks Scissors, Scissors cuts Paper, Paper beats Rock")
    print()
    call = loop()
    final = check_if_won(won)



    
