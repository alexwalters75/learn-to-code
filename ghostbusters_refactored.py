import time
import random

backpack = []

baddie = ["Vinz Clortho The Keymaster", "Zuul The Gatekeeper",
          "Stay Puft the Marshmallow Man",
          "Gozer The Destroyer", "Vigo The Carpathian"]

random_baddie = random.choice(baddie)


def print_pause(message):
    print(message)
    time.sleep(1)


def intro():
    print_pause("\n"
                "'We\'re there!', screams Egon.\n")
    print_pause("The Ectomobile screeches to a halt in front of City Hall "
                "and the four of you run through the front door.\n")
    print_pause("'I really hate tall buldings' moans Venkman\n")
    print_pause("Your stomach sinks as you realise that you have left the "
                "ghost trap in the car\n")
    print_pause("'Guys, I think we have a bit of a problem....'\n")
    print_pause("'There's no time and we have to get to the roof' "
                "insists Egon")
    print_pause("'The elevator is broken so let's take the stairs!!'")


def choose_car():
    print_pause("You run back out the doors and scramble through the "
                "rubbish in the boot of the ectomobile")
    if "ghost_trap" in backpack:
        print_pause("What are you doing back here?! "
                    "It looks like you have everything that you need.")
        print_pause("You hurry back up to City Hall and run "
                    "back into the lobby at the bottom of "
                    "the stairs.")
    else:
        print_pause("You run back out the doors and scramble through the "
                    "rubbish in the boot of the ectomobile.")
        print_pause("And there it is, tucked away underneath "
                    "last night's pizza boxes.")
        backpack.append("ghost_trap")
        print_pause("You hurry back up to City Hall and run "
                    "back into the lobby at the bottom of "
                    "the stairs.")


def choose_stairs():
    print_pause("You run up 25 flights of stairs and "
                "reappear on the roof")
    print_pause(f"'Holy moly, its {random_baddie}!'")


def fight():
    print_pause("You start fighting")
    if "ghost_trap" in backpack:
        print_pause("You have the ghost trap")
        print_pause("You kill the baddie\n")
        play_again()
    else:
        print_pause("You don't have the ghost trap")
        print_pause("You are defeated by the baddie")
        play_again()


def flight():
    print_pause("You run back down to the lobby")
    print_pause("It all looks a bit familiar down here")


def play_again():
    play_again = input("Would you like to play again?\n"
                       "Please enter y or n\n").lower()
    if play_again == 'y':
        print_pause("OK great, let me load that back up for you")
        # I want this next line to be the main function eg. play_game()
        exit()
    elif play_again == 'n':
        print_pause("No problem - hope you enjoyed the game!")
        exit()


intro()

while True:
    print_pause("\n"
                "What would you like to do?\n")
    print_pause("Enter 1 to head back to the car")
    print_pause("Enter 2 run up the stairs")
    car_or_stairs = input("Please enter 1 or 2\n")
    if car_or_stairs == '1':
        choose_car()
    elif car_or_stairs == '2':
        choose_stairs()
        print_pause("\n"
                    "What would you like to do?\n")
        print_pause("Enter 1 to fight to the death")
        print_pause("Enter 2 to retreat back down the stairs")
        fight_or_flight = input("Please enter 1 or 2\n")
        if fight_or_flight == '1':
            fight()
        elif fight_or_flight == '2':
            flight()
