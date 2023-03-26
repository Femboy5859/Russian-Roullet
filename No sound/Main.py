import time
import random
from Champion import *
import numpy as np


print("Made by Shy Guy#4993\nYes a Femboy :3\n")
# Easy
Bot1 = input(
    "Easy, Medium, Hard, Champion?\nEasy = 5 in 6 chance to live\nMedium = 3 in 6 chance to live\nHard = 1 in 6 chance to live\nChampion = Will randomly choose the difficulty every round and save your score\nThe game will continue until you die and end after 3 seconds after you die\n\n")
if Bot1 == "Easy":
    while True:
        Bot = input("What number do you wanna be? (1-6)")
        input("Press enter to try")
        print("Your number is\n", Bot, "\n")
        if Bot == "1":
            Bullet = (random.randint(1, 6))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet)
            if Bullet == 1:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

        if Bot == "2":
            Bullet = (random.randint(1, 6))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet)
            if Bullet == 2:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

        if Bot == "3":
            Bullet = (random.randint(1, 6))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet)
            if Bullet == 3:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

        if Bot == "4":
            Bullet = (random.randint(1, 6))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet)
            if Bullet == 4:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

        if Bot == "5":
            Bullet = (random.randint(1, 6))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet)
            if Bullet == 5:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

        if Bot == "6":
            Bullet = (random.randint(1, 6))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet)
            if Bullet == 6:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")






# Meduim
elif Bot1 == "Medium":
    while True:
        Bullet1_list = [1, 2]
        Bullet2_list = [3, 4]
        Bullet3_list = [5, 6]
        Bot = input("What number do you wanna be? (1-6)")
        input("Press enter to try")
        print("Your number is\n", Bot, "\n")
        if Bot == "1":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3)
            if Bullet1 == 1 or Bullet2 == 1 or Bullet3 == 1:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

        if Bot == "2":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3)
            if Bullet1 == 2 or Bullet2 == 2 or Bullet3 == 2:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

        if Bot == "3":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3)
            if Bullet1 == 3 or Bullet2 == 3 or Bullet3 == 3:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

        if Bot == "4":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3)
            if Bullet1 == 4 or Bullet2 == 4 or Bullet3 == 4:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

        if Bot == "5":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3)
            if Bullet1 == 5 or Bullet2 == 5 or Bullet3 == 5:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

        if Bot == "6":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3)
            if Bullet1 == 6 or Bullet2 == 6 or Bullet3 == 6:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")





# Hard

elif Bot1 == "Hard":
    while True:
        Bullet1_list = [1, 2, 3, 4, 5, 6]
        Bullet2_list = [1, 2, 3, 4, 5, 6]
        Bullet3_list = [1, 2, 3, 4, 5, 6]
        Bullet4_list = [1, 2, 3, 4, 5, 6]
        Bullet5_list = [1, 2, 3, 4, 5, 6]
        Bot = input("What number do you wanna be? (1-6)")
        input("Press enter to try")
        print("Your number is\n", Bot, "\n")
        if Bot == "1":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            Bullet4 = (random.choice(Bullet4_list))
            Bullet5 = (random.choice(Bullet5_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3, Bullet4, Bullet5)
            if Bullet1 == 1 or Bullet2 == 1 or Bullet3 == 1 or Bullet4 == 1 or Bullet5 == 1:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

        if Bot == "2":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            Bullet4 = (random.choice(Bullet4_list))
            Bullet5 = (random.choice(Bullet5_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3, Bullet4, Bullet5)
            if Bullet1 == 2 or Bullet2 == 2 or Bullet3 == 2 or Bullet4 == 2 or Bullet5 == 2:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

        if Bot == "3":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            Bullet4 = (random.choice(Bullet4_list))
            Bullet5 = (random.choice(Bullet5_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3, Bullet4, Bullet5)
            if Bullet1 == 3 or Bullet2 == 3 or Bullet3 == 3 or Bullet4 == 3 or Bullet5 == 3:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

        if Bot == "4":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            Bullet4 = (random.choice(Bullet4_list))
            Bullet5 = (random.choice(Bullet5_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3, Bullet4, Bullet5)
            if Bullet1 == 4 or Bullet2 == 4 or Bullet3 == 4 or Bullet4 == 4 or Bullet5 == 4:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

        if Bot == "5":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            Bullet4 = (random.choice(Bullet4_list))
            Bullet5 = (random.choice(Bullet5_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3, Bullet4, Bullet5)
            if Bullet1 == 5 or Bullet2 == 5 or Bullet3 == 5 or Bullet4 == 5 or Bullet5 == 5:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

        if Bot == "6":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            Bullet4 = (random.choice(Bullet4_list))
            Bullet5 = (random.choice(Bullet5_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3, Bullet4, Bullet5)
            if Bullet1 == 6 or Bullet2 == 6 or Bullet3 == 6 or Bullet4 == 6 or Bullet5 == 6:
                print("You died")

                time.sleep(3)
                exit()
            else:
                print("You Won!")
                print("\n")

import os

# Done
# Adding and printing score
# score += 1
# print(f"Score: {score}")


# Save Score
# elif user_input == "Save Score":
# with open(score_file, "w") as f:
# f.write(str(score))
# print("Score saved.")

import tkinter as tk
from tkinter import *
import random

colors = ["red", "blue", "green", "yellow", "orange", "purple"]


def spam():
    while True:
        window = Tk()
        window.configure(background=random.choice(colors))
        window.geometry("300x200+" + str(random.randint(0, 1500)) + "+" + str(random.randint(0, 500)))
        window.overrideredirect(True)
        label = Label(window, text="CONGRATULATIONS!!\nWait 10 seconds don't close", font=("Arial Bold", 15),
                      fg="black")
        label.place(relx=0.5, rely=0.5, anchor=CENTER)
        window.after(1, spam)
        window.after(10000, window.destroy)
        window.mainloop()


# Print Score
if Bot1 == "Score":
    if os.path.isfile(score_file):
        with open(score_file, "r") as f:
            score = int(f.read())
            print(f"Score: {score}")
            time.sleep(2)
    else:
        print("No score saved.")

    if score >= 30:
        print("****YOU!! YOU HUMAN!!!! YOUR A CHEATER >:c, I will find you and i will hug you O-o****")
        print("Activating spam in 8 seconds **WARNING CLOSE THE APP**")
        time.sleep(8)
        call = spam()
        time.sleep(10)

# Champion
if Bot1 == "Champion":
    champion()






