import os
import random
import math
import time
from pprint import pprint

import player
import checks
import grafx
import status
import interface


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()
grafx.splash()
time.sleep(2)
clear()
genCharacter = player.pc(5, 5, 5, 5, 5, 5, 5, "Player",
                         "Character", 1, 1, 25, "the Protagonist")
# pprint(vars(genCharacter))


def characterCreate(character):
    print("What is your First name?")
    firstName = input("\n> ")
    character.SetFirstName(firstName)
    clear()
    print("What is your Last name?")
    lastName = input("\n> ")
    character.SetLastName(lastName)
    clear()


def nameCheck(genCharacter):
    # ? Question
    print("Are you " + genCharacter.GetName() +
          ", "+genCharacter.GetDescritpion()+"?[Y/N]")
    # ? Input
    a = input("\n> ").capitalize()
    clear()
    while a != "Yes" and a != "No" and a != "N" and a != "Y" and a != "1" and a != "2" and a != "A" and a != "B":
        # ? Question
        print(
            "I don't understand. This game accepts a range of inputs, often prompted, and generally not case-sensitive.")
        print()
        print("Are you " + genCharacter.GetName() +
              ", "+genCharacter.GetDescritpion()+"?[Y/N]")
        # ? Input
        a = input("\n> ").capitalize()
        clear()

    if a == "Yes" or a == "Y" or a == "1" or a == "A":
        print("Understood. Welcome to the world, " +
              genCharacter.GetFirstName()+".", sep="")
    elif a == "No" or a == "N" or a == "2" or a == "B":
        print("Oh. Well Let's try that again.")
        characterCreate(genCharacter)
        nameCheck(genCharacter)


nameCheck(genCharacter)

# print(checks.genderCheck1(genCharacter).capitalize() +
#       "? "+checks.genderCheck1(genCharacter)+".", sep="")
strength = checks.StrengthCheck(genCharacter, 6)
if strength != True:
    print("You're scrawny!")
status.playerCard(genCharacter)
# with open('lastNames.txt', encoding="utf8") as fileinput:
#     for line in fileinput:
#         line = line.lower().capitalize()
#         print(line)
