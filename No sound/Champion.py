import time
import random
import os

score_file = "score.txt"
def add_score():
    global score
    score += 1
score = 0

def easy():
        Bot = input("What number do you wanna be? (1-6)")
        input("Press enter to try")
        print("Your number is\n", Bot, "\n")
        if Bot == "1":
            Bullet = (random.randint(1, 6))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet)
            if Bullet == 1:
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")

        if Bot == "2":
            Bullet = (random.randint(1, 6))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet)
            if Bullet == 2:
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")

        if Bot == "3":
            Bullet = (random.randint(1, 6))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet)
            if Bullet == 3:
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")

        if Bot == "4":
            Bullet = (random.randint(1, 6))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet)
            if Bullet == 4:
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")

        if Bot == "5":
            Bullet = (random.randint(1, 6))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet)
            if Bullet == 5:
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)

                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")

        if Bot == "6":
            Bullet = (random.randint(1, 6))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet)
            if Bullet == 6:
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")





#Meduim
def medium():
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
                Bot55 = input(
                    "You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")

        if Bot == "2":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3)
            if Bullet1 == 2 or Bullet2 == 2 or Bullet3 == 2:
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")

        if Bot == "3":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3)
            if Bullet1 == 3 or Bullet2 == 3 or Bullet3 == 3:
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")

        if Bot == "4":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3)
            if Bullet1 == 4 or Bullet2 == 4 or Bullet3 == 4:
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")

        if Bot == "5":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3)
            if Bullet1 == 5 or Bullet2 == 5 or Bullet3 == 5:
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")

        if Bot == "6":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3)
            if Bullet1 == 6 or Bullet2 == 6 or Bullet3 == 6:
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")




#Hard
def hard():
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
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")

        if Bot == "2":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            Bullet4 = (random.choice(Bullet4_list))
            Bullet5 = (random.choice(Bullet5_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3, Bullet4, Bullet5)
            if Bullet1 == 2 or Bullet2 == 2 or Bullet3 == 2 or Bullet4 == 2 or Bullet5 == 2:
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")

        if Bot == "3":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            Bullet4 = (random.choice(Bullet4_list))
            Bullet5 = (random.choice(Bullet5_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3, Bullet4, Bullet5)
            if Bullet1 == 3 or Bullet2 == 3 or Bullet3 == 3 or Bullet4 == 3 or Bullet5 == 3:
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")

        if Bot == "4":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            Bullet4 = (random.choice(Bullet4_list))
            Bullet5 = (random.choice(Bullet5_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3, Bullet4, Bullet5)
            if Bullet1 == 4 or Bullet2 == 4 or Bullet3 == 4 or Bullet4 == 4 or Bullet5 == 4:
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")

        if Bot == "5":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            Bullet4 = (random.choice(Bullet4_list))
            Bullet5 = (random.choice(Bullet5_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3, Bullet4, Bullet5)
            if Bullet1 == 5 or Bullet2 == 5 or Bullet3 == 5 or Bullet4 == 5 or Bullet5 == 5:
                Bot55 = input("You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                if Bot55 == "Yes":
                    with open(score_file, "w") as f:
                        f.write(str(score))
                        print("Score saved.")
                        time.sleep(3)
                        exit()
                elif Bot55 == "No":
                    exit()
            else:
                print("You Won!")
                add_score()
                print("\n")

        if Bot == "6":
            Bullet1 = (random.choice(Bullet1_list))
            Bullet2 = (random.choice(Bullet2_list))
            Bullet3 = (random.choice(Bullet3_list))
            Bullet4 = (random.choice(Bullet4_list))
            Bullet5 = (random.choice(Bullet5_list))
            print("( -_•)╦̵̵̿╤─ PEW", Bullet1, Bullet2, Bullet3, Bullet4, Bullet5)
            if Bullet1 == 6 or Bullet2 == 6 or Bullet3 == 6 or Bullet4 == 6 or Bullet5 == 6:
                if score > 3:
                    Bot55 = input(
                        "You died\n" + f"You got: {score} points\n" + "Would you like to save the score? (Yes or No)")
                    if Bot55 == "Yes":
                        with open(score_file, "w") as f:
                            f.write(str(score))
                            print("Score saved.")
                            time.sleep(3)
                            exit()
                    elif Bot55 == "No":
                        exit()
            else:
                print("You Won!")
                add_score()
                print("\n")


List = [easy, medium, hard]

def champion():
    while True:
        options = [easy, medium, hard]
        func = random.choice(options)
        func()











