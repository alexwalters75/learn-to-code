import time
import random

backpack = []

baddie = ["Vinz Clortho The Keymaster", "Zuul The Gatekeeper",
          "Stay Puft the Marshmallow Man",
          "Gozer The Destroyer", "Vigo The Carpathian"]

random_baddie = random.choice(baddie)

flights = random.randint(10, 75)


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
    print_pause("'Guys, I think we have a problem....'\n")
    print_pause("'There's no time and we have to get to the roof' "
                "insists Egon")
    print_pause("'The elevator is broken so let's take the stairs!!'")


def choose_car():
    print_pause("You run back out the doors and scramble through the "
                "rubbish in the boot of the ectomobile\n")
    if "ghost_trap" in backpack:
        print_pause("What are you doing back here?! "
                    "It looks like you have everything that you need.\n")
        print_pause("You hurry back up to City Hall and run "
                    "back into the lobby at the bottom of "
                    "the stairs.")
        play_game()
    else:
        print_pause("And there it is, tucked away underneath "
                    "last night's pizza boxes.\n")
        backpack.append("ghost_trap")
        print_pause("You stick the ghost trap in your back pack hurry "
                    "back into the City Hall lobby")
        play_game()


def choose_stairs():
    print_pause(f"You run up {flights} flights of stairs and "
                "reappear on the roof\n")
    print_pause(f"Holy moly, its {random_baddie}!")


def fight():
    print_pause("You open up your proton packs and "
                "unleash a century's worth of plasma")
    print_pause("The New York skyline lights up like "
                "it's New Year's Eve all over again")
    print_pause("Now all you need to do is throw open the "
                "ghost trap")
    if "ghost_trap" in backpack:
        print_pause("You slide the ghost pack across the floor "
                    " and fire it up.\n")
        print_pause("....................\n")
        print_pause("And you've done it!!\n")
        print_pause("Another victory for the Ghostbusters\n")
        play_again()
    else:
        print_pause("You fumble around in your backpack but "
                    "deep down you know something has gone wrong.\n")
        print_pause("....................\n")
        print_pause("Your eyes meet and you know that this is the end.\n")
        print_pause(f"{random_baddie} towers over you for the last time\n")
        print_pause("Splat!!!")
        play_again()


def flight():
    print_pause("You run back down to the lobby\n")
    print_pause("It all looks a bit familiar down here")
    play_game()


def play_again():
    play_again = input("Would you like to play again?\n"
                       "Please enter y or n\n").lower()
    if play_again == 'y':
        print_pause("OK great, let me load that back up for you")
        ghostbusters()
    elif play_again == 'n':
        print_pause("No problem - hope you enjoyed the game!")
        exit()
    else:
        play_again()


def play_game():
    print_pause("\n"
                "What would you like to do?\n")
    print_pause("Enter 1 to head back to the car")
    print_pause("Enter 2 run up the stairs")
    car_or_stairs = input("Please enter 1 or 2\n")
    if car_or_stairs == '1':
        choose_car()
    elif car_or_stairs == '2':
        choose_stairs()
        play_game2()
    else:
        play_game()


def play_game2():
    print_pause("\n"
                "What would you like to do?\n")
    print_pause("Enter 1 to fight to the death")
    print_pause("Enter 2 to retreat back down the stairs")
    fight_or_flight = input("Please enter 1 or 2\n")
    if fight_or_flight == '1':
        fight()
    elif fight_or_flight == '2':
        flight()
    else:
        play_game2()


def ghostbusters():
    intro()
    play_game()


ghostbusters()

# A note: I couldn't figure out how to persist with the number of floors
# or the name of the baddie across the game once it had started.
# Is there an obvious way of doing this do you think?
