import random
from time import sleep

class GuessGame:
    def Intro(self):
        '''sleep(1)
        print("\nWelcome to the Guessing Game! ",end="")
        sleep(1.5)
        contributors = "Designed by Karl and Subhman."
        for char in contributors:
            print(char,end="")
            sleep(0.21)
        sleep(2)
        print("\nThe purpose of the game is simple, the algorithm will randomly pick up a number into a certain range of number "
              "that you will be aware of.")
        sleep(4)
        print("Afterward your will have to guess what is the secret number that was picked up. If you get stuck you can access "
            "to a hint by pressing 'H'.")
        sleep(4)
        print("Then let's start and Good Luck!")'''
        start = input("Ready to start? (Press Enter) or (Esc to exit the program)")
        return start

    def pick_up(self):
        n1 = random.choice(range(1,501))
        n2 = random.choice(range(501,1001))
        ranges = range(n1,n2)
        number = random.choice(ranges)
        return number,n1,n2


class Main(GuessGame):
   
    number = 0
    count = 0
    n1 = 0
    n2 = 0
    guesses = ''
    guess_of_count = 10
    out_of_guesses = True
    user = GuessGame().Intro()
    def scoring(count):
        if count == 0:
            score = 1000
        else:
            score = (10 - count) * 100
        return score
    
    if user == "y":
        lst = GuessGame().pick_up()
        number = lst[0]
        x = number
        x -= x % -100
        print(number)
        n1 = lst[1]
        n2 = lst[2]
        print("\nSuper! Let's go!")
        print(f"The number selected is between {n1} to {n2}. Time to guess!")
    elif user == "n":
        exit()
    else:
        print("Please enter a valid input.")
    while count <= guess_of_count:
        while True:
            try:
                guesses = input("Please enter your guess: ")
                break
            except:
                print("Invalid guesses! Try again.")
        if guesses == "H":
            print("The number rounded up to the closest 100 is: ", x)
        elif int(guesses) <= n1:
            print("This number is lower than the min!")
        elif int(guesses) >= n2:
            print("This number is higher than the max!")
        elif int(guesses) < number:
            count += 1
        elif int(guesses) > number:
            count += 1
        else:
            out_of_guesses = False
            break
    
    if out_of_guesses:
        print(f"Sorry you run out of guesses.The number was {number}.Try again!")
    else:
        print(f"Congratulations you win! The number was '{number}'.")
        print("Your Final Score of the game is:",scoring(count))


Main()
