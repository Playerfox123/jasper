import pygame
import random
import time
Patk = 55
Pdef = 40
Php = 30
Pgold = 500

print("You are a pokemon trainer with your Pikachu on an island.")
time.sleep(1)
print("However, you are trapped on this island in alola. being in the alola reigon is important later")
time.sleep(1)
print("If you complete the quest, your Pikachu will have enough experince to become")
time.sleep(1)
print("a Richu. Then, you will find a master ball and be able to catch Mewtwo,")
time.sleep(1)
print("who is nearly unseen.")
time.sleep(1)
print("First, you must battle 20 different pokemon.")
battlesDone = 0

while battlesDone < 20:
    choosePokemon = random.randint(1, 15)

    if choosePokemon == 1:
        spawn = ' Pidgey'
        shp = 14
        satk = 9
        sdef = 10

    if choosePokemon == 2:
        spawn = ' Rattata'
        shp = 16
        satk = 8
        sdef = 10

    if choosePokemon == 3:
        spawn = ' Zubat'
        shp = 15
        satk = 7
        sdef = 8

    if choosePokemon == 4:
        spawn = ' Caterpie'
        shp = 14
        satk = 9
        sdef = 5

    if choosePokemon == 5:
        spwan = ' Spearow'
        shp = 14
        satk = 9
        sdef = 7

    if choosePokemon == 6:
        spawn = ' Weedle'
        shp = 15
        satk = 9
        sdef = 8

    if choosePokemon == 7:
        spawn = ' Paras'
        shp = 14
        satk = 8
        sdef = 7

    if choosePokemon == 8:
        spawn = ' Magikarp'
        shp = 13
        satk = 10
        sdef = 9

    if choosePokemon == 9:
        spawn = ' Eevee'
        shp = 15
        satk = 9
        sdef = 10

    if choosePokemon == 10:
        spawn = ' Krabby'
        shp = 16
        satk = 9
        sdef = 10

    if choosePokemon == 11:
        spawn = ' Jigglypuff'
        shp = 15
        satk = 9
        sdef = 10

    if choosePokemon == 12:
        spawn = ' Clefairy'
        shp = 15
        satk = 8
        sdef = 9

    if choosePokemon == 13:
        spawn = ' Pidgeotto'
        shp = 17
        satk = 8
        sdef = 11

    if choosePokemon == 14:
        spawn = ' NidoranF'
        shp = 16
        satk = 8
        sdef = 9

    if choosePokemon == 15:
        spawn = ' NidoranM'
        shp = 15
        satk = 8
        sdef = 10

    while Php > 0 and shp > 0:
        choice = ('z')
        while choice != ('a'):
            print('What will you do against the' + spawn + '?')
            print('    a) Fight like a champion.')
            print('    b) Run like a coward.')
            print('    c) Analyze the situation first.')
            print('    d) Atempt to heal.')
            choice = input()
            if choice == ('a'):
                print('Alright Pikachu! Lets do this!')
            if choice == ('b'):
                print(
                    'You attempt to flee, but the ' + spawn + ' hits Pikachu anyway, knocking him out in one blow.')
                print('You are out of revives.  Please insert $.50 to play again.')
                Php = 0
                break
            if choice == ('c'):
                print('Pikachu stats:')
                print('Attack = ' + str(Patk) + '   Defense = ' + str(Pdef) + '   Health = ' + str(
                    Php) + '     Gold = ' + str(Pgold))
                print('The wild' + spawn + ' has stats of:')
                print('Attack = ' + str(satk) + '   Defense = ' + str(sdef) + '   Health = ' + str(shp))
            if choice == ('d'):
                print(
                    "You can choose to either pay 500 gold and get a guarranteed heal, or take your chances with berries. Note- berries CAN kill you. (Pick 'pay' or 'berries'")
                time.sleep(.5)
                print("And don't abuse the healing system, you can't get higher than 30 Hp.")
                if Php > 30:
                    print(
                    "No HP for you.")
                heal = input("Will you take your chances, or pay 500 gold?")
                if heal == ("berries"):
                    healing = random.randint(1, 20)
                    if healing < 11:
                        print(
                        "You got real lucky, kid.  + 5 hp")
                        Php = Php + 5
                    if healing > 11:
                        print(
                        "You lost 5 HP...")
                        Php = Php - 5

                if heal == ("pay"):
                    if Pgold < 500:
                        print("You don't have the money to pay for it.")
                    if Pgold > 500:
                        Pgold == Pgold - 500
                        print('+5 HP. You have ' + (int(Pgold)) + ' remaining.')
                        Php == Php + 5
                    if Pgold > 500 and Php > 30:
                        print("You reached the maximum health.")

            if choice == ('a'):
                Pattroll = random.randint(1, 20)
                if Pattroll >= sdef:
                    damage = random.randint(2, 8)
                    print('Pikachu, use thunder shock! ' + spawn + ' took ' + str(damage) + ' damage!')
                    shp = shp - damage
                if Pattroll < sdef:
                    print('The shock missed!')

                if shp > 0:
                    Sattroll = random.randint(1, 20)
                    if Sattroll >= Pdef:
                        damage = random.randint(2, 7)
                        print('The ' + spawn + ' hits pikachu for ' + str(damage) + '!')
                        Php = Php - damage
                    if Sattroll < Pdef:
                        print('Pikachu dodged the attack!')
            if Php <= 0:
                print('Pikachu fainted, and the ' + spawn + ' has knocked him out.')
                battlesDone = 0
            if shp <= 0:
                reward = random.randint(200, 900)
                print('You win! For your troubles, you find ' + str(reward) + ' PP.')
                Pgold = Pgold + reward
                Php = 25
                print('You find an Oran berry tree and are able to heal.')
                battlesDone = battlesDone + 1
                print('You are on battle number' + str(battlesDone) + ', so keep having fun there.')
                break

    if battlesDone == 20:
        print(
        "Woah! Pikachu is evolving!")
        time.sleep(3)
        print(
        " Pikachu evolved into Richu! Awesome!")
        print("What's this? Richu is alolan form and can fly!")
        print(
        "You find a master ball and catch the legendary pokemon, mewtwo.")
        print(
        " You fly off the island with Richu, and are greeted home as a hero.")
        print(
        " The end!")
        print
        "Thanks for playing! All credit goes to the Pokemon Company. I take no ownership for anything in this game whatsoever (except for the code)."
        print
        "Credits"
        time.sleep(1)
        print
        "Pokemon names and ideas- The Pokemon Co."





