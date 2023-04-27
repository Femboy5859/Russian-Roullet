import time
import random
import pygame

pygame.mixer.init()


gun_sound = pygame.mixer.Sound("gun_fire.wav")
gun_empty = pygame.mixer.Sound("gun_empty.wav")

def easy():
    bullet = input("1-6: ")
    die = random.randint(1,6)
    bullet = int(bullet)
    if bullet != die:
        gun_empty.play()
        print("\n( -_•)╦̵̵̿╤─ Pew!!", die)
        print("\nYou win")
    else:
        gun_sound.play()
        print("\n( -_•)╦̵̵̿╤─ Pew!!", die)
        print("You loset....")

def medium():
    bullet = input("1-6: ")
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    die3 = random.randint(1,6)
    
    bullet = int(bullet)
    if bullet != die1 and bullet != die2 and bullet != die3:
        gun_empty.play()
        print("\n( -_•)╦̵̵̿╤─ Pew!!", die1, die2, die3)
        print("\nYou win")
    else:
        gun_sound.play()
        print("\n( -_•)╦̵̵̿╤─ Pew!!", die1, die2, die3)
        print("You loset....")

def hard():
    bullet = input("1-6: ")
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    die3 = random.randint(1,6)
    die4 = random.randint(1,6)
    die5 = random.randint(1,6)
    
    bullet = int(bullet)
    if bullet != die1 and bullet != die2 and bullet != die3 and die4 != bullet and die5 != bullet:
        gun_empty.play()        
        print("\n( -_•)╦- Pew!!", die1, die2, die3, die4, die5)
        print("\nYou win")
    else:
        gun_sound.play()      
        print("\n( -_•)╦- Pew!!", die1, die2, die3, die4, die5)
        print("You loset....")


while True:
    print("\nMade by Shy Guy#4993\nYes a Femboy :3\n")
    bot = input("Easy, Medium or Hard?: ")

    if bot.lower() == "easy":
        easy()
    elif bot.lower() == "medium":
        medium()
    elif bot.lower() == "hard":
        hard()
    elif bot.lower() == "x games":
        bot55 = input("What game mode?: ")
        
        if bot55.lower() == "easy":
            bot66 = input("How many times?")
            bot66 = int(bot66)
            for i in range(bot66):
                easy()
        
        if bot55.lower() == "medium":
            bot66 = input("How many times?")
            bot66 = int(bot66)
            for i in range(bot66):
                medium()
       
        if bot55.lower() == "hard":
            bot66 = input("How many times?")
            bot66 = int(bot66)
            for i in range(bot66):
                hard()