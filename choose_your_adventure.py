import art
import time
from art import sword
from art import cave
from art import halberd
from art import castle
from art import death
from art import enemies
from art import choice
from art import win
wpn_sword = ''
wpn_halberd = ''
lose_txt = "You are shunned and exiled from your settlement for your cowardice. \n \t \tYOU LOSE"
retreat_txt = "You retreat to the clearing but are tired.\nDo you comtinue to run or do you fight? F/R \t"
seperate = "\n-----------------------------------------------------------------------------------------------\n"

def you_died():
    time.sleep(5)
    print(seperate)
    death()
    print(seperate)
    print(f"Rest in Peace {name} \n \t \t YOU LOSE")

def you_win():
    time.sleep(5)
    print(seperate)
    win()
    print(seperate)
    print(f"Congratulations {name}, you rescued your townsfolk and are regarded as a hero \n \t \t YOU WIN")

def escaped():
    print("\nYou have escaped with your life but failed at your task")
    print(lose_txt)

castle()
print(seperate)
time.sleep(3)
print("Welcome to Choose Your Adventure!")
name = input("What is your name adventurer? \t")
print(f"{name}, members of our hamlet have been kidnapped by goblins, if they aren't rescued they'll surely die")
will_help = input(f"Please {name}, will you help them? Y/N \t")

if will_help.upper() == "Y":
    print(seperate)
    choice()
    print(seperate)
    time.sleep(3)
    print("You are presented with two weapons, which will you take?")
    wpn_choice = input("Please type: sword/halberd/none \t")
    if wpn_choice.lower() == "sword":
        wpn_sword = True
        time.sleep(3)
        print(seperate)
        sword()
        print(seperate)
    elif wpn_choice.lower() == "halberd":
        wpn_halberd = True
        time.sleep(3)
        print(seperate)
        halberd()
        print(seperate)
    elif wpn_choice.lower() == "none":
        wpn_choice = False
    elif wpn_choice.lower() == "both":
        print("you are unable to carry both so you leave without either.")
        wpn_choice = False
    else:
        print("invalid response")

    time.sleep(5)
    print(seperate)
    cave()
    print(seperate)
    print("Having set off on your quest, you come to a cave.")
    enter = input("You were told this was the last place the goblins were sighted. Do you enter? Y/N \t")

    if enter.upper() == "Y":
        print("You enter the cave and begin searching, you hardly breath as you creep through the dimly lit cavern.")
        print("You hear many footsteps approaching. They are likely hostile.")
        fight_flight = input("do you stand and fight or retreat? F/R \t")
        print(seperate)
        enemies()
        print(seperate)
        time.sleep(3)
        if fight_flight.upper() == "F":
            if wpn_choice == False:
                print("You are a fool, you are unarmed and were immediately overwhelmed")
                you_died()
            elif wpn_sword == True:
                print("A hoard of goblins emerge from the dark.\nYou cut them down with ferocious skill.")
                you_win()
            elif wpn_halberd ==True:
                print("You don't have enough room to swing your weapon and are overwhelmed.")
                you_died()
            else:
                print("an error occurred")
        elif fight_flight.upper() == "R":
            if wpn_choice == False:
                print("You packed light and are fast on your feet.\nYou have escaped")
                escaped()
            elif wpn_sword == True:
                fight_flight = input(retreat_txt)
                if fight_flight.upper() == "F":
                    print("You cut down a few but the hoard quickly surrounds you.")
                    you_died()
                elif fight_flight.upper() == "R":
                    escaped()
                else:
                    print("invalid response")
            elif wpn_halberd == True:
                fight_flight = input(retreat_txt)
                if fight_flight.upper() == "F":
                    print("Your weapons range is advantageous. You cut down the hoard with ferocious skill")
                    you_win()
                elif fight_flight.upper() == "R":
                    print("You are slow and heavy, they quickly catch up.")
                    you_died()
                else:
                    print("invalid input")
            else:
                print("an error occurred")
    else:
        death()
        print(seperate)
        print(lose_txt)

elif will_help.upper() == "N":
    print(lose_txt)
else:
    print("invalid response")