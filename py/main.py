"""
I Started this project on Oct 26, 2020.
I wanted to create a automated character sheet, so people dont have to keep up with the stats, automatic rolling, levels, and general character inforamtion.

I need to implement some easy DMG/Heal systems so players can interact with it and with the world.
I will have to figure out the long term effect of making a skill tree that expands based on initial choices and usage of the weapon/magic.


The next big thing is how to create an expandable list for char inv and their values. 2d lists might be a thing in order to keep track of everything in the INV.
I created an inventory management console, please integrate it into any menu option


Use Discord as a multiplayer option?
"""
import os
import sys
import math
import random
from os import path
os.chdir(sys.path[0])  # TXT file path is the same location as this file.
# The primary list that handles everything about the character.
currentPlayerCharacterInfo = []
startingCharSkills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Barter", "Bluff", "Climb", "Combat", "Crafting", "Diplomacy", "Disguise", "Engineering", "Fabrication", "Flora", "History", "Insight", "Intimidate",
                      "Investigation", "Medicine", "Mining", "Perception", "Perform", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival", "Swim"]  # Current list of skills, can be expanded or contracted depending on desire for complexity.
availableWeapons = ["Axe", "Boomerang", "Bow", "Cane", "Club", "Crossbow", "Dagger", "Daibo", "Explosive", "Fist Weapon", "Flail", "Hammer", "Javelin", "Mace",
                    "Nun Chucks", "Pickaxe", "Pistol", "Polearm", "Rifle", "Scythe", "Shotgun", "Shovel", "Spear", "Staff", "Sword", "Unarmed", "Wand", "Whips"]  # list of available weapons
availableMagics = ["Acid", "AntiMagic", "Art", "Card", "Crystal", "Death", "Earth", "Electric", "Fire", "Gravity", "Hair", "Holy", "Ice", "Lava", "Life",
                   "Light", "Magiscript", "Metal", "Mind", "Music", "Plant", "Shadow", "Shield", "Sonic", "Tech", "Time", "Water", "Wind"]  # list of available magics
saveFile = "Stats.char"


def Autosave():  # Autosave is sprinkled throughout the code to make sure the TXT is updated promptly and if random exit happens you can pick up where you left off.
    # Saves the player data to a TXT for reference later.
    PlayerCharacterDatabase = open(saveFile, "w+")
    for PlayerCharacterData in currentPlayerCharacterInfo:
        # Writes the info to the file one line at a time.
        PlayerCharacterDatabase.write(str(PlayerCharacterData) + "\n")
    # Closes the file, don't need to keep this open.
    PlayerCharacterDatabase.close()


# Creates a new character based on user input and random numbers.
def newCharacterStats():
    highStat, lowStat = None, None  # Sets empty vars for While Compare on next line
    while highStat == lowStat:  # compares the variables before and after stat generation
        statRolls = []  # Sets up a list or clears the list for the rolls made for the stat generation
        while len(statRolls) < 5:  # Do this 5 times, sets up for the next section
            # Add a new random number between 2-10, originally I had this as a 1d10 dice roll and you reroll 1's but this makes it easier.
            statRolls.append(random.randint(2, 10))
        # Sorts the list of rolls you just made, lowest first.
        statRolls.sort()
        statRolls.pop(0)  # Removes the lowest number from the list.
        # 1st of the stat rolls that will be added together, this is the lowest number.
        firstStat = statRolls.pop(0)
        # 2nd of the stat rolls that will be added together.
        secondStat = statRolls.pop(0)
        # 3rd of the stat rolls that will be added together.
        thirdStat = statRolls.pop(0)
        # 4th of the stat rolls that will be added together, this is the highest number.
        fourthStat = statRolls.pop(0)
        # Adding the highest number and 3rd highest number.
        highStat = secondStat + fourthStat
        # Adding the lowest number and 3rd lowest number.
        lowStat = firstStat + thirdStat
    # If the initial input is specifically "magical" then they can have it and the stats are generated in the sheet.
    if enterNewPlayerCharacterDamageStyle == "magical":
        # If the list is an odd number itll even it out.
        if len(availableMagics) % 2 != 0:
            # adds the final blank item to even out the list.
            availableMagics.append(" ")
        # makes a int that is half the total length of the list.
        splitter = int(len(availableMagics)/2)
        AM1 = availableMagics[0:splitter]  # first half of the list.
        AM2 = availableMagics[splitter:]  # second half of the list.
        print()  # prints an empty line for ease of reading.
        # I have no idea how this works, I found it in an online thread asking for what I wanted to do.
        for key, value in zip(AM1, AM2):
            # I need to learn this so i can figure out 2d lists and integrate them into the skill section.
            print("{0:<15s} {1}".format(key, value))
        # asks user to choose from list, but can choose anything.
        chooseWeapon = str.title(input("\nChoose a Magic: "))
        magList = ["Magical Damage", chooseWeapon, "STR", str(lowStat), "INT", str(highStat), "Max Health", str(lowStat*2), "Max Energy", str(
            highStat*2), "Current Health", str(lowStat*2), "Current Energy", str(highStat*2)]  # Generates a new magical character with my pregen random stats
        currentPlayerCharacterInfo.extend(magList)  # Adds info to the sheet
    else:  # If the initial input is anything but "magical" they are a brute and dont deserve it.
        # If the list is an odd number itll even it out.
        if len(availableWeapons) % 2 != 0:
            # adds the final blank item to even out the list.
            availableWeapons.append(" ")
        # makes a int that is half the total length of the list.
        splitter = int(len(availableWeapons)/2)
        AW1 = availableWeapons[0:splitter]  # first half of the list.
        AW2 = availableWeapons[splitter:]  # second half of the list.
        print()  # prints an empty line for ease of reading.
        # I have no idea how this works, I found it in an online thread asking for what I wanted to do.
        for key, value in zip(AW1, AW2):
            # I need to learn this so i can figure out 2d lists and integrate them into the skill section.
            print("{0:<15s} {1}".format(key, value))
        # asks user to choose from list, but can choose anything.
        chooseWeapon = str.title(input("\nChoose a Weapon: "))
        physList = ["Physical Damage", chooseWeapon, "STR", str(highStat), "INT", str(lowStat), "Max Health", str(highStat*2), "Max Energy", str(
            lowStat*2), "Current Health", str(highStat*2), "Current Energy", str(lowStat*2)]  # Generates a new physical character with my pregen random stats
        currentPlayerCharacterInfo.extend(physList)  # Adds info to the sheet


# When you need to roll skills you type out "roll [skillname]" and this chunk executes.
def skillRolling():
    # this is for batch rolling, you type out "roll [skillname] [number of rolls]" to roll multiple times... this line checks if you have the energy to roll that many times in a row.
    if int(skillRollMultiplier) > int(currentPlayerCharacterInfo[20]):
        os.system('clear')  # Clears the screen to keep things clean.
        # self explanatory.
        print("\nYou don't have enough energy for that.\n")
    else:  # if you have the energy, do the roll
        # change to integer for use with following script.
        rollMultiSkill = int(skillRollMultiplier)
        # If a number was entered use that number for the number of rolls you are looking to do.
        while rollMultiSkill > 0:
            # As long as the roll count is above 0 it'll roll
            if int(currentPlayerCharacterInfo[20]) > 0:
                rollMultiSkill -= 1  # As long as there is at least one energy and a roll is entered it will remove that roll counter by one
                os.system('clear')  # Clears the screen to keep things clean.
                # Rollin, rollin, rollin...
                newSkillRoll = random.randint(1, 10)
                # divides by 100 for amount of skill xp gained from roll
                addSkillXPFromRoll = newSkillRoll/100
                # checks for the skill to increase and adds 1 to get the actual number instead of the skill name
                skillIndex = currentPlayerCharacterInfo.index(
                    str.title(stripSpacesOfSkill)) + 1
                # removes the skill xp from the Character data list
                currentSkillXP = float(
                    currentPlayerCharacterInfo.pop(skillIndex))
                # adds the old skill xp to the new skill xp gained from this roll
                currentSkillXP += addSkillXPFromRoll
                # inserts that number back into the list
                currentPlayerCharacterInfo.insert(
                    skillIndex, round(currentSkillXP, 2))
                # Takes the remainder of the roll (out of 10) and adds half of it to the player XP
                addPlayerXPFromRoll = math.floor((10 - newSkillRoll)/2)
                # removes the player xp from the Character data list
                currentPlayerXP = int(currentPlayerCharacterInfo.pop(6))
                # adds the old player xp to the new player xp gained from this roll
                currentPlayerXP += addPlayerXPFromRoll
                # inserts that number back into the list
                currentPlayerCharacterInfo.insert(6, currentPlayerXP)
                adjustCurrentEnergy = int(currentPlayerCharacterInfo.pop(
                    20)) - 1  # removes one point of energy
                # inserts that number back into the list
                currentPlayerCharacterInfo.insert(20, str(adjustCurrentEnergy))
                # Skill Score is the number that is presented after the roll. adds level and skill level, then takes the roll and creates a percentage of the total
                skillScore = (
                    float(currentSkillXP) + float(currentPlayerCharacterInfo[4])) * (newSkillRoll/10)
                skillScore = math.floor(skillScore)  # rounding down of course.
                # Print the roll number you got and the Skill Score.
                print("\nYou rolled a " + str(newSkillRoll) + " in " +
                      str.title(stripSpacesOfSkill) + " with a score of " + str(skillScore)+"\n")
                # Saving the character info directly to the TXT sheet.
                Autosave()


def levelUp():  # Oh hey you leveled up! this chunk is used when the current player XP exceeds the current level*10
    # The fancy pop up box that says you leveled up!
    print("┌───────────┐\n│ LEVEL UP! │\n└───────────┘\n")
    # get current level as integer
    currentLevel = int(currentPlayerCharacterInfo[4])
    # remove the XP from the total required to level up
    removedXPforLevelUp = (
        int(currentPlayerCharacterInfo.pop(6)) - (currentLevel*10))
    # inserts that number back into the list
    currentPlayerCharacterInfo.insert(6, removedXPforLevelUp)
    # straight up removes the level and adds 1 for re-insertion
    currentLevel = int(currentPlayerCharacterInfo.pop(4)) + 1
    # inserts that number back into the list
    currentPlayerCharacterInfo.insert(4, currentLevel)
    # If the level is a multiple of 5 it offers the option to increase your Int or Str
    if int(currentPlayerCharacterInfo[4]) % 5 == 0:
        # Does your input start with an "I"
        StrIntLvl = input(
            "Your Body and Mind are in sync...\nDo you focus on your Strength or Intelligence? ")
        if StrIntLvl[0:1] == "i":  # great! you did the thing!
            upgradeIntelligence = int(currentPlayerCharacterInfo.pop(
                12)) + 1  # pops the element and adds 1
            # inserts that number back into the list
            currentPlayerCharacterInfo.insert(16, str(upgradeIntelligence))
            upgradeEnergy = int(currentPlayerCharacterInfo.pop(
                16)) + 2  # pops the element and adds 2
            # inserts that number back into the list
            currentPlayerCharacterInfo.insert(16, str(upgradeEnergy))
            # says what you just did...
            print("\nYou have chosen to Focus on your Mind.\n")
        else:  # thats not an "I" so im guessing you wanted str instead
            upgradeStrength = int(currentPlayerCharacterInfo.pop(
                10)) + 1  # pops the element and adds 1
            # inserts that number back into the list
            currentPlayerCharacterInfo.insert(14, str(upgradeStrength))
            upgradeHealth = int(currentPlayerCharacterInfo.pop(
                14)) + 2  # pops the element and adds 2
            # inserts that number back into the list
            currentPlayerCharacterInfo.insert(14, str(upgradeHealth))
            # says what you just did...
            print("\nYou have chosen to Focus on your Body.\n")
    levelUpToken = 1  # Adjustable token for allowing the amount of health and energy upgrade points allowed during a level up
    Autosave()  # Saving the character info directly to the TXT sheet.
    while levelUpToken > 0:  # as long a token is allowed you can level up your health and energy too
        chooseStatToUpgrade = str.lower(
            input("Would you like more Health or more Energy? "))  # asking nicely
        # does the entry start with an E? well you just got +1 energy!
        if chooseStatToUpgrade[:1] == "e":
            upgradeEnergy = int(currentPlayerCharacterInfo.pop(
                16)) + 1  # pops the element and adds 1
            # inserts that number back into the list
            currentPlayerCharacterInfo.insert(16, str(upgradeEnergy))
            # says what you just did...
            print("\nYou have chosen to increase your Energy Reserves.\n")
            # removes an upgrade token counter so you dont get stuck here.
            levelUpToken -= 1
        # does the entry start with an H? well you just got +1 health!
        elif chooseStatToUpgrade[:1] == "h":
            upgradeHealth = int(currentPlayerCharacterInfo.pop(
                14)) + 1  # pops the element and adds 1
            # inserts that number back into the list
            currentPlayerCharacterInfo.insert(14, str(upgradeHealth))
            # says what you just did...
            print("\nYou have chosen to increase your Health Reserves.\n")
            # removes an upgrade token counter so you dont get stuck here.
            levelUpToken -= 1
        else:  # Answered completely wrong? That's not good, try again.
            print("That is not a valid entry.")  # says what you just did...
    Autosave()  # Saving the character info directly to the TXT sheet.
    os.system('clear')  # Clears the screen to keep things clean.
    print("Level Up Complete!")  # Oh hey you did the thing! Congrats!
    dailyReset()  # reset health and energy to max


def dailyReset():  # Did you sleep or level up? this resets your health and energy to max
    # gets the max health stat
    finalRestoreHealth = currentPlayerCharacterInfo[14]
    # straight up removes the current health
    currentPlayerCharacterInfo.pop(18)
    # inserts that number back into the list
    currentPlayerCharacterInfo.insert(18, str(finalRestoreHealth))
    # gets the max energy stat
    finalRestoreEnergy = currentPlayerCharacterInfo[16]
    # straight up removes the current energy
    currentPlayerCharacterInfo.pop(20)
    # inserts that number back into the list
    currentPlayerCharacterInfo.insert(20, str(finalRestoreEnergy))
    Autosave()  # Saving the character info directly to the TXT sheet.
    print("\nHealth and Energy Restored!\n")  # now you can use more skills!


# SCRIPT ACTUALLY STARTS HERE!
os.system('clear')  # Clears the screen to keep things clean.
if path.exists(saveFile) != True:  # Is there a sheet already made...
    PlayerCharacterDatabase = open(saveFile, "w+")  # No? make one!
else:  # yes, the sheet exists?
    # just read from it and dont overwrite it
    PlayerCharacterDatabase = open(saveFile, "r")
for PlayerCharacterData in PlayerCharacterDatabase.readlines():  # take the information from the sheet
    # place it into the list at the top called "currentPlayerCharacterInfo"
    currentPlayerCharacterInfo.append(PlayerCharacterData.rstrip("\n"))
# Close the TXT file, you dont need to keep it open.
PlayerCharacterDatabase.close()
# If there is nothing in the list called "currentPlayerCharacterInfo" even after the import of the sheet we start making a new character for you.
if not currentPlayerCharacterInfo:
    enterNewPlayerCharacterName = str.title(
        input("What is your character's name? "))  # New Name, who dis?
    enterNewPlayerCharacterRace = str.title(input(
        "What is the race of "+enterNewPlayerCharacterName+"? "))  # New Race, who dis?
    # Are you a brute or will you spell magical correctly?
    enterNewPlayerCharacterDamageStyle = str.lower(
        input("Are you Physical or Magical? "))
    # make a list of things that need to be at the top of the sheet
    newCharList = [enterNewPlayerCharacterName, "Race",
                   enterNewPlayerCharacterRace, "Level", 1, "XP", 0]
    # add it to the list at the top
    currentPlayerCharacterInfo.extend(newCharList)
    newCharacterStats()  # make new char stats
    Skillz = startingCharSkills.copy()  # Get the list of skills from the top
    while len(Skillz) > 0:  # check if the copied list isnt empty
        currentPlayerCharacterInfo.append(
            Skillz.pop(0))  # add the skill in line
        # add the level of a new skill which is 0
        currentPlayerCharacterInfo.append("0")
    Autosave()  # Saving the character info directly to the TXT sheet.
os.system('clear')  # Clears the screen to keep things clean.
# WELCOME TO AUTOMATICALY MATHING YOUR STATS
print("\n\nWelcome to your Super Basic RPG Character Sheet!\n\n")
Playing = True  # mainly here for making sure when you save and quit there is an actual exit condition
while Playing == True:  # obv if you're playing its going to be true lul
    Autosave()  # Saving the character info directly to the TXT sheet.
    # checking if the XP is higher than the level*10
    while int(currentPlayerCharacterInfo[6]) >= int(currentPlayerCharacterInfo[4])*10:
        levelUp()  # do the levelup dance!
    startScreenSelection = ""  # clears the start screen selector so you can do stuff
    # lastThing really isnt a last item or object, it just makes the bottom dashes equidistant to the top dashes when the name is inserted.
    lastThing = ""
    for _ in range(len(currentPlayerCharacterInfo[0])):
        # easy to watch in action, hard to explain. checks how long the name is and makes the bottom dashes equal to the top ones.
        lastThing += "-"
    print("------------ "+currentPlayerCharacterInfo[0]+" ------------\n\nLevel "+str(currentPlayerCharacterInfo[4])+" - "+str(currentPlayerCharacterInfo[6])+"/"+str(int(currentPlayerCharacterInfo[4])*10)+" XP\nRace: "+str(currentPlayerCharacterInfo[2])+"\n"+str(currentPlayerCharacterInfo[7]) + " - "+str(currentPlayerCharacterInfo[8])+"\n"+str(
        currentPlayerCharacterInfo[18])+"/"+str(currentPlayerCharacterInfo[14])+" Health"+"\n"+str(currentPlayerCharacterInfo[20])+"/"+str(currentPlayerCharacterInfo[16])+" Energy"+"\n"+"\nUse \"roll [skill]\" to use a skill"+"\n1. View Skills"+"\n2. Long Rest"+"\n3. Inventory Manager"+"\n4. Save and Quit"+"\n-------------"+lastThing+"-------------")  # ALL THE MAIN MENU INFO
    # time to put this thing to work! pick your poison below
    startScreenSelection = str.lower(
        input("\nPlease make a selection or roll a skill: "))
    # if you want to see your current skills and level stats for them
    if startScreenSelection == "1" or startScreenSelection == "view skills":
        os.system('clear')  # Clears the screen to keep things clean.
        print("Skills List:")  # you gotta know what you are looking at
        # get the skills and values
        unsplitter = currentPlayerCharacterInfo[21:]
        skillListFix = []  # Empty list for appending things in the next loop
        for i in range(0, len(unsplitter), 2):  # get every other items index
            # append the 1st and 2nd item to a new list, at the index of the previous list, together with a colon seperating them
            skillListFix.append(
                str(unsplitter[i]) + ": " + str(unsplitter[i+1]))
        # makes a int that is half the total length of the list.
        splitter = int(len(skillListFix)/2)
        SL1 = skillListFix[0:splitter]  # first half of the list.
        SL2 = skillListFix[splitter:]  # second half of the list.
        # I have no idea how this works yet, I found it in an online thread asking for what I wanted to do.
        for key, value in zip(SL1, SL2):
            # I need to learn this so i can figure out 2d lists and integrate them into the skill section.
            print("{0:<25s}{1}".format(key, value))
        print()  # empty space just cause it looks better
    elif startScreenSelection == "2" or startScreenSelection == "rest":  # gotta reset those energy points
        os.system('clear')  # Clears the screen to keep things clean.
        dailyReset()  # resets health and energy to max
    # inventory incomplete, dont ask because I dont know how im doing this yet.
    elif startScreenSelection == "3":
        os.system('clear')  # Clears the screen to keep things clean.
        # if you read this and still need a comment please see a psychiatrist
        print("\nView/Edit Inventory options are incomplete. Please try again later.\n")
    elif startScreenSelection == "4" or startScreenSelection == "quit" or startScreenSelection == "exit":  # simple save and quit option
        Autosave()  # Saving the character info directly to the TXT sheet.
        Playing = False  # quiting the game like every other RPG out there.
        # buh-bye! terminate program.
        print(currentPlayerCharacterInfo[0] +
              "'s Info Saved! Thanks for playing!")
    # ROLLS! the most important part of a dice and math game!
    elif startScreenSelection[0:1] == "r":
        # strips everything in the input away to just numbers
        skillRollMultiplier = ''.join(
            numberCheck for numberCheck in startScreenSelection if numberCheck.isnumeric())
        skillChosen = ''.join(numberCheck for numberCheck in startScreenSelection if numberCheck.isalpha(
        ) or numberCheck.isspace())  # gets everything that is a plan letter and space only
        # splits off the first word which is usually roll and turns them into a list
        splitFromFirstWord = (skillChosen.split(' ', 1))
        # choose the second item in the list which is the skill and removes excess spaces at the begining and end
        stripSpacesOfSkill = str.strip(splitFromFirstWord[1])
        if skillRollMultiplier == "":  # if no number was provided after the skill
            skillRollMultiplier = 1  # if no number was provided it defaults to 1
        # if the skill you put in is actually on the list.
        if str.title(stripSpacesOfSkill) in startingCharSkills:
            skillRolling()  # does the rolls that you input
        else:  # if you didnt put in a skill correctly you didnt roll anything
            os.system('clear')  # Clears the screen to keep things clean.
            # roll an actual skill please, there is a list for reference.
            print("\nThats not a Skill, Try harder.\n")
    else:  # nothing matches so you get accosted
        os.system('clear')  # Clears the screen to keep things clean.
        wrongList = ["\nEven electronic brain pancake crystal elderly.\n", "\nDo you even read, Bro?\n", "\nAre you even trying?\n", "\nThat wasn't useful, Try again.\n", "\nGG EZ Noob!\n", "\nMaybe you could use your fingers?\n", "\nDidn't see that coming... But it did.\n", "\nNext time roll for intelligence, you might need it.\n", "\nRead first, then type.\n", "\nHold on, let me just NOT do that...\n", "\nHappens to the best of us, but clearly you're not one of us.\n", "\nCan you at least use the last 2 brain cells you have?\n",
                     "\nNo...\n", "\nI know, the first 30 years of childhood are the hardest.\n", "\nAnd this is why batman works alone.\n", "\nHow do I put this? You need to be \"not dumb.\"\n", "\nYou disgust me...\n", "\nI'm gunna smack you!\n", "\nUser faulty; please replace.\n", "\nI'm smarter than you and I dont even have a brain.\n", "\nError lies between keyboard and chair.\n", "\nID-10T report will be available shortly.\n", "\n\n"]  # What? you cant read basic instructions!
        # chooses one of the previous lines
        print(wrongList[random.randint(0, len(wrongList)-1)])
# End of the line...
