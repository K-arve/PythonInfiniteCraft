import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import os
import time
menu = True
game = False
elementwindow = False
loop = True
saveexists = os.path.isfile("./KEY.dat")
timer = 4
while timer >= 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n----------- INFINITE CRAFT PYTHON -----------")
    print("|      total knock off of infinite craft      |")
    print("|  credit goes to neal.fun for original idea  |")
    print("-------------- MADE BY RED LASER --------------")
    print("         LAUNCHING GAME IN " + str(timer) + " SECONDS.         ")
    time.sleep(1)
    timer -= 1
del timer
if saveexists == True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n----------- INFINITE CRAFT PYTHON -----------")
    print("|      total knock off of infinite craft      |")
    print("|  credit goes to neal.fun for original idea  |")
    print("-------------- MADE BY RED LASER --------------")
    print("               LOADING USER DATA               ")
    testingkey = open("./KEY.dat", "r")
    testingkey = testingkey.readlines()
    print("checking key file")
    if len(testingkey) >= 2:
        print("confirming key (IF THIS DOESNT WORK DELETE YOUR KEY FILE AND RESTART)")
        testingkey = testingkey[1]
        genai.configure(api_key=testingkey)
        model = genai.GenerativeModel('gemini-1.5-flash')
        answer = model.generate_content("Hello World!")
        if answer.text != "":
            print("key confirmed")
        else:
            print("\nWhy did you change your key to" + testingkey + "\nDelete your key file and you should be good.") 
            quit()
    else:
        print("\nCan you not just leave the key file as it is?\nDelete your key file and you should be good.")
        quit()
else:
    print("First time launching game")
    print("Creating a save file")
    createkey = open("./KEY.dat", "w")
    createkey.write("# hey if you're reading this it'd be sick if you didn't edit your elements manually, thanks. #\n")
    createlements = open("./elements.dat", "w")
    createlements.write("fire \nwater \nearth \nwind \n")
    createlements.close()
    print("Generate a Gemini API key at https://aistudio.google.com/app/apikey")
    correctkey = False
    while correctkey == False:
        testkey = input("Copy and past the key here")
        genai.configure(api_key=testkey)
        model = genai.GenerativeModel('gemini-1.5-flash')
        answer = model.generate_content("Hello World!")
        if answer.text != "":
            correctkey = True
            createkey.write(testkey)
        else:
            print("It appears there was an error, try again!")
    createkey.close()
del saveexists
key = open("./KEY.dat", "r+")
elements = open("./elements.dat", "r+")
key = key.readlines()
key = key[1]
model = genai.GenerativeModel('gemini-1.5-flash')
genai.configure(api_key=key)
def ToList(path, removespace):
    file = open("./elements.dat", "r")
    file = file.readlines()
    if removespace:
        file = [s.replace("\n", "").rstrip(" ") for s in file]
    else:
        file = [s.replace("\n", "") for s in file]
    return file
def AddElement(element):
    file = open("./elements.dat", "r+")
    file = file.readlines()
    
while loop == True:
    while game == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n----------- INFINITE CRAFT PYTHON -----------")
        print("|      total knock off of infinite craft      |")
        print("|  credit goes to neal.fun for original idea  |")
        print("-------------- MADE BY RED LASER --------------")
        print("            ELEMENT CRAFTING WINDOW            ")
        elements.close()
        elements = open("./elements.dat", "r+")
        while True:
            question = input("(type 'menu' to go to the menu) What element do you want to craft with: \n")
            if question.lower() == 'menu':
                print("Entering Menu Window")
                menu = True
                game = False
                elementwindow = False
                break
            if question.lower() in ToList(elements, True):
                break
            else:
                print("You must have the element you want to craft with.")
        if game == True:
            while True:
                question2 = input("(type 'menu' to go to the menu) Combining " + question + " and: \n")
                if question2.lower() == 'menu':
                    print("Entering Menu Window")
                    menu = True
                    game = False
                    elementwindow = False
                    break
                if question2.lower() in ToList(elements, True):
                    break
                else:
                    print("You must have the element you want to craft with.")
        if game == True:
            print("Generating Result (2-5 seconds)")
            time.sleep(1.5)
            answer = model.generate_content("(ONLY RESPOND WITH THE ELEMENT) Make an infinite craft style element that is a result of crafting " + question + " and " + question2 + " together without any emojis.")
            print("Verifying result")
            if answer.candidates[0].finish_reason == 1:
                if len(answer.text) < 25:
                    if answer.text.lower() != "menu":
                        check = answer.text.lower()
                        if check.endswith(' '):
                            check = check.replace("\n", "").rstrip(" ")
                        othercheck = answer.text.lower()
                        if not othercheck.endswith(' '):
                            othercheck = othercheck.replace("\n", "") + ' '
                        elements.close()
                        elements = open("./elements.dat", "r+")
                        inlist = answer.text.lower() in elements.readlines()
                        inlist2 = answer.text.lower() in ToList(elements, True)
                        inlist3 = othercheck in elements.readlines()
                        inlist4 = othercheck in ToList(elements, True)
                        inlist5 = check in elements.readlines()
                        inlist6 = check in ToList(elements, True)
                        if str(inlist) + str(inlist2) + str(inlist3) + str(inlist4) + str(inlist5) + str(inlist6) == "FalseFalseFalseFalseFalseFalse":
                            print("You discovered: " + answer.text.lower())
                            if elements.read().endswith('\n'):
                                elements.write('\n')
                            elements.write((answer.text.lower().rstrip(" ").replace("\n", "") + '\n'))
                        else:
                            print("You created: " + answer.text.lower())
                    else:
                        print("You cannot get menu as an element, sorry.")
                else:
                    print("Result too long")
            else:
                print("It appears there was an error, try again!")
            os.system('pause') 
    while elementwindow == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n----------- INFINITE CRAFT PYTHON -----------")
        print("|      total knock off of infinite craft      |")
        print("|  credit goes to neal.fun for original idea  |")
        print("-------------- MADE BY RED LASER --------------")
        print("              ELEMENT VIEW WINDOW              ")
        elements.close()
        elements = open("./elements.dat", "r+")
        print(''.join(elements.readlines()))
        with open("./elements.dat", 'r') as elem:
            counter = 0
            for line in elem:
                counter += 1
        choice = input("'exit' to exit the game \n'play' to start the game \nYou have " + str(counter) + " elements\n")
        if choice.lower() == 'exit':
            print("Exitting...")
            print("Saving Data")
            elements.close()
            print("Data Saved")
            loop = False
            break
        if choice.lower() == 'play':
            print("Entering Elements Window")
            menu = False
            game = True
            elementwindow = False
    while menu == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n----------- INFINITE CRAFT PYTHON -----------")
        print("|      total knock off of infinite craft      |")
        print("|  credit goes to neal.fun for original idea  |")
        print("-------------- MADE BY RED LASER --------------")
        print("                   MAIN MENU                   ")
        choice = input("\n'exit'\n\n'elements'\n\n'play'\n\n")
        if choice.lower() == 'exit':
            print("Exitting...")
            print("Saving Data")
            elements.close()
            print("Data Saved")
            loop = False
            break
        if choice.lower() == 'elements':
            print("Loading Elements")
            menu = False
            game = False
            elementwindow = True
        if choice.lower() == 'play':
            print("Loading Game")
            menu = False
            game = True
            elementwindow = False
print("Thanks for playing")
