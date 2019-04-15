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

numberOfCharacters = len(wordChoice)
hangmanNumber = 0
spaces = ["_" for i in range(numberOfCharacters)]
guessed = ""

while True:
    print(hangmen[hangmanNumber])
    print(*spaces)
    engine.say("What letter do you want to guess?")
    engine.runAndWait()
    letter = input("What letter do you want to guess? ").lower()
    if letter == "jaxatax is a 1337 haxor wizard":
        print("You're correct. Here's a hint: the first 3 letters are " + wordChoice[0] + wordChoice[1] + wordChoice[2] + ".")
        engine.say("You're correct. Here's a hint: the first 3 letters are " + wordChoice[0] + " " + wordChoice[1] + " and " + wordChoice[2] + ".")
        engine.runAndWait()
        spaces[0] = wordChoice[0]
        spaces[1] = wordChoice[1]
        spaces[2] = wordChoice[2]
    elif len(letter) != 1:
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
        print("You got it wrong. Get rekt m8.")
        engine.say("You got it wrong. Get rekt mate.")
        engine.runAndWait()
        hangmanNumber += 1
        guessed += letter
    if "_" not in spaces:
        print(hangmen[hangmanNumber])
        print(*spaces)
        print("Good job! You won!")
        engine.say("Good job! You won!")
        engine.runAndWait()
        break
    elif hangmanNumber == 6:
        print("You lose. Get rekt m8. The word you had so much trouble guessing was " + wordChoice + ". You were just beaten by a program written by a 13 year-old.")
        engine.say("You lose. Get rekt mate. The word you had so much trouble guessing was " + wordChoice + ". You were just beaten by a program written by a 13 year-old.")
        engine.runAndWait()
        break
