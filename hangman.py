from random import *
import pyttsx3
engine = pyttsx3.init()

words = ["knob","jazz","water","awkward","bungler","caterpillar","supercalifragilisticexpialidocious","phlegm","twelfth","liquidize","twisty","cellular","jelly","graze","fences","geese","ogre","dwarves","squid","fjord","croquet"]
wordChoice = words[randint(0,20)]

hangmen = [''' ___
/   |
|
|
|
''',''' ___
/   |
|   O
|
|
''',''' ___
/   |
|   O
|   |
|
''',''' ___
/   |
|   O
|  /|
|
''',''' ___
/   |
|   O
|  /|\\
|
''',''' ___
/   |
|   O
|  /|\\
|  /
''',''' ___
/   |
|   O
|  /|\\
|  / \ ''']

choose()
numberOfCharacters = len(wordChoice)
hangmanNumber = 0
spaces = ["_" for i in range(numberOfCharacters)]
guessed = ""

while True:
    print(hangmen[hangmanNumber])
    print(*spaces)
    engine.say("What letter do you want to guess?")
    engine.runAndWait()
    letter = input("What letter do you want to guess? ")
    if len(letter) != 1:
        print("Please enter a single letter.")
        engine.say("Please enter a single letter.")
        engine.runAndWait()
    elif letter in guessed:
        print("You've guessed that letter.")
        engine.say("You've guessed that letter.")
        engine.runAndWait()
    elif letter in wordChoice:
        print("You got it right! Good job!")
        engine.say("You got it right! Good job!")
        engine.runAndWait()
        index = 0
        while index < len(wordChoice):
            index = wordChoice.find(letter,index)
            if index == -1:
                break
            letterPosition = index
            spaces[letterPosition] = letter
            index += 1
        guessed += letter
    else:
        print("You got it wrong. Get rekt.")
        engine.say("You got it wrong. Get rekt.")
        engine.runAndWait()
        hangmanNumber += 1
        guessed += letter
    if "_" not in spaces:
        print("Good job! You won!")
        engine.say("Good job! You won!")
        engine.runAndWait()
        break
    elif hangmanNumber == 6:
        print("You lose. Get rekt m8.")
        engine.say("You lose. Get rekt mate")
        engine.runAndWait()
        break
