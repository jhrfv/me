"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("/nWlecome to the advancedguessing game!")
    print("Please type 2 numbers to start:")

    lowerbound= super_asker(-200000, 200000, "Enter a lower bound:")
    upperbound =super_asker(
        lowerbound + 2, 200000, f"Enter a upper bound, {lowerbound +2} or  above: "
    )

    print(f"OK Then, a number between {lowerbound} and  {upperbound} ?")
    actualnumber = random.randint(lowerbound, upperbound)

    while True:
        guessednumber = super_asker(lowerbound, upperbound, "guess a number: ")
        print(f"You guessed {guessednumber},")
        if guessednumber == actualnumber:
            print(f"You got it! It was {actualnumber},") 
            return "You got it!"
        elif guessednumber < actualnumber:
            print("Too small, try again :")

            

    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
