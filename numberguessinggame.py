# Example by Sharad Khare
# This project is a fun game that generates a random number in a certain specified range and the user must guess the number after receiving hints. Every time a user’s guessings is wrong they are prompted with more hints to make it easier — at the cost of reducing the score.

# The program also requires functions to check if an actual number is entered by the user or not, and finds the difference between the two numbers. 

import random
sharadlist = []
def show_score():
    if len(sharadlist) <=0:
        print("there is currently no high score, it's your starting so keep trying")
    else:
        print("The current high score is {} attempts".format(min(sharadlist)))
def start_game():
    random_number = int(random.randint(1,10))
    print("Hello gamer! welcome to the game made by sharad")
    player_name = input("What is your name?: ")

    want_play = input("Hi, {}, would you like to play the guessing game? (Enter yes/No) ".format(player_name))

# where the show_score function used to be:
    attempts = 0
    show_score() 
    while want_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10")
        if int(guess) <1 or int(guess) >10:
                raise ValueError("Please guess a number within the given range 1 to 10")
        if int(guess) == random_number:
                print("Very Nice, you got it")
        attempts +=1
        sharadlist.append(attempts)
        print("It took you {} attempts".format(attempts))
        play_again = input("Would you want to play again? (Enter yes/No) ")
        attempts = 0
        show_score()
        random_number = int(random.randint(1,10))
        if play_again.lower() == "no":
            print("wow, you have a good score")
            break
        elif int(guess) > random_number:
            print("It's lower")
            attempts +=1
        elif int(guess) < random_number:
            print("It's Higher")
            attempts +=1
        except ValueError as err:
            print("ohh no.. that is not the valid value")
            print("({})".format(err))
            else:
                print("Thats's Wow, you have a great score")
        if __name__ == '__main__':
            start_game()
            

