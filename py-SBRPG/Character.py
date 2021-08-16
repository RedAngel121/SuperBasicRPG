"""
    I Started this project on Oct 26, 2020.
    I wanted to create a automated character sheet, so people dont have to keep up with the stats, automatic rolling, levels, and general character inforamtion.
    The next big thing is how to create an expandable list for char inv and their values. 2d lists might be a thing in order to keep track of everything in the INV.
    """
import os, sys, math, random
from os import path
os.chdir(sys.path[0]) # TXT file path is the same location as this file.
currentPlayerCharacterInfo = [] # The primary list that handles everything about the character.
startingCharSkills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Barter", "Bluff", "Climb", "Combat", "Crafting", "Diplomacy", "Disguise", "Engineering", "Fabrication", "Flora", "History", "Insight", "Intimidate", "Investigation", "Medicine", "Mining", "Perception", "Perform", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival", "Swim"] # Current list of skills, can be expanded or contracted depending on desire for complexity.
availableWeapons = ["Axe", "Boomerang", "Bow", "Cane", "Club", "Crossbow", "Dagger", "Daibo", "Explosive", "Fist Weapon", "Flail", "Hammer", "Javelin", "Mace", "Nun Chucks", "Pickaxe", "Pistol", "Polearm", "Rifle", "Scythe", "Shotgun", "Shovel", "Spear", "Staff", "Sword", "Unarmed", "Wand", "Whips"] # list of available weapons
availableMagics = ["Acid", "AntiMagic", "Art", "Card", "Crystal", "Death", "Earth", "Electric", "Fire", "Gravity", "Hair", "Holy", "Ice", "Lava", "Life", "Light", "Magiscript", "Metal", "Mind", "Music", "Plant", "Shadow", "Shield", "Sonic", "Tech", "Time", "Water", "Wind"] # list of available magics
saveFile = "Stats.char"
def Autosave(): # Autosave is sprinkled throughout the code to make sure the TXT is updated promptly and if random exit happens you can pick up where you left off.
    PlayerCharacterDatabase = open(saveFile, "w+") # Saves the player data to a TXT for reference later.
    for PlayerCharacterData in currentPlayerCharacterInfo:PlayerCharacterDatabase.write(str(PlayerCharacterData) + "\n") # Writes the info to the file one line at a time.
    PlayerCharacterDatabase.close() # Closes the file, don't need to keep this open.
def newCharacterStats(): # Creates a new character based on user input and random numbers.
    highStat, lowStat = None, None # Sets empty vars for While Compare on next line
    while highStat == lowStat: # compares the variables before and after stat generation
        statRolls = [] # Sets up a list or clears the list for the rolls made for the stat generation
        while len(statRolls) < 5: # Do this 5 times, sets up for the next section
            statRolls.append(random.randint(2, 10)) # Add a new random number between 2-10, originally I had this as a 1d10 dice roll and you reroll 1's but this makes it easier.
        statRolls.sort() # Sorts the list of rolls you just made, lowest first.
        statRolls.pop(0) # Removes the lowest number from the list.
        firstStat = statRolls.pop(0) # 1st of the stat rolls that will be added together, this is the lowest number.
        secondStat = statRolls.pop(0) # 2nd of the stat rolls that will be added together.
        thirdStat = statRolls.pop(0) # 3rd of the stat rolls that will be added together.
        fourthStat = statRolls.pop(0) # 4th of the stat rolls that will be added together, this is the highest number.
        highStat = secondStat + fourthStat # Adding the highest number and 3rd highest number.
        lowStat = firstStat + thirdStat # Adding the lowest number and 3rd lowest number.
    if enterNewPlayerCharacterDamageStyle == "magical": # If the initial input is specifically "magical" then they can have it and the stats are generated in the sheet.
        if len(availableMagics) % 2 != 0: # If the list is an odd number itll even it out.
            availableMagics.append(" ") # adds the final blank item to even out the list.
        splitter = int(len(availableMagics)/2) # makes a int that is half the total length of the list.
        AM1 = availableMagics[0:splitter] # first half of the list.
        AM2 = availableMagics[splitter:] # second half of the list.
        print() # prints an empty line for ease of reading.
        for key, value in zip(AM1,AM2): # I have no idea how this works, I found it in an online thread asking for what I wanted to do.
            print("{0:<15s} {1}".format(key, value)) # I need to learn this so i can figure out 2d lists and integrate them into the skill section.
        chooseWeapon = str.title(input("\nChoose a Magic: ")) # asks user to choose from list, but can choose anything.
        magList = ["Magical Damage", chooseWeapon, "STR", str(lowStat), "INT", str(highStat), "Max Health", str(lowStat*2), "Max Energy", str(highStat*2), "Current Health", str(lowStat*2), "Current Energy", str(highStat*2)] # Generates a new magical character with my pregen random stats
        currentPlayerCharacterInfo.extend(magList) # Adds info to the sheet
    else: # If the initial input is anything but "magical" they are a brute and dont deserve it.
        if len(availableWeapons) % 2 != 0: # If the list is an odd number itll even it out.
            availableWeapons.append(" ") # adds the final blank item to even out the list.
        splitter = int(len(availableWeapons)/2) # makes a int that is half the total length of the list.
        AW1 = availableWeapons[0:splitter] # first half of the list.
        AW2 = availableWeapons[splitter:] # second half of the list.
        print() # prints an empty line for ease of reading.
        for key, value in zip(AW1,AW2): # I have no idea how this works, I found it in an online thread asking for what I wanted to do.
            print("{0:<15s} {1}".format(key, value)) # I need to learn this so i can figure out 2d lists and integrate them into the skill section.
        chooseWeapon = str.title(input("\nChoose a Weapon: ")) # asks user to choose from list, but can choose anything.
        physList = ["Physical Damage", chooseWeapon, "STR", str(highStat), "INT", str(lowStat), "Max Health", str(highStat*2), "Max Energy", str(lowStat*2), "Current Health", str(highStat*2), "Current Energy", str(lowStat*2)] # Generates a new physical character with my pregen random stats
        currentPlayerCharacterInfo.extend(physList) # Adds info to the sheet
def skillRolling(): # When you need to roll skills you type out "roll [skillname]" and this chunk executes.
    if int(skillRollMultiplier) > int(currentPlayerCharacterInfo[20]): # this is for batch rolling, you type out "roll [skillname] [number of rolls]" to roll multiple times... this line checks if you have the energy to roll that many times in a row.
        os.system('cls') # Clears the screen to keep things clean.
        print("\nYou don't have enough energy for that.\n") # self explanatory.
    else: # if you have the energy, do the roll
        rollMultiSkill = int(skillRollMultiplier) # change to integer for use with following script.
        while rollMultiSkill > 0: # If a number was entered use that number for the number of rolls you are looking to do.
            if int(currentPlayerCharacterInfo[20]) > 0: # As long as the roll count is above 0 it'll roll
                rollMultiSkill -= 1 # As long as there is at least one energy and a roll is entered it will remove that roll counter by one
                os.system('cls') # Clears the screen to keep things clean.
                newSkillRoll = random.randint(1, 10) # Rollin, rollin, rollin...
                addSkillXPFromRoll = newSkillRoll/100 # divides by 100 for amount of skill xp gained from roll
                skillIndex = currentPlayerCharacterInfo.index(str.title(stripSpacesOfSkill)) + 1 # checks for the skill to increase and adds 1 to get the actual number instead of the skill name
                currentSkillXP = float(currentPlayerCharacterInfo.pop(skillIndex)) # removes the skill xp from the Character data list
                currentSkillXP += addSkillXPFromRoll # adds the old skill xp to the new skill xp gained from this roll
                currentPlayerCharacterInfo.insert(skillIndex, round(currentSkillXP, 2)) # inserts that number back into the list
                addPlayerXPFromRoll = math.floor((10 - newSkillRoll)/2) # Takes the remainder of the roll (out of 10) and adds half of it to the player XP
                currentPlayerXP = int(currentPlayerCharacterInfo.pop(6)) # removes the player xp from the Character data list
                currentPlayerXP += addPlayerXPFromRoll # adds the old player xp to the new player xp gained from this roll
                currentPlayerCharacterInfo.insert(6, currentPlayerXP) # inserts that number back into the list
                adjustCurrentEnergy = int(currentPlayerCharacterInfo.pop(20)) - 1 # removes one point of energy
                currentPlayerCharacterInfo.insert(20, str(adjustCurrentEnergy)) # inserts that number back into the list
                skillScore = (float(currentSkillXP) + float(currentPlayerCharacterInfo[4])) * (newSkillRoll/10) # Skill Score is the number that is presented after the roll. adds level and skill level, then takes the roll and creates a percentage of the total
                skillScore = math.floor(skillScore) # rounding down of course.
                print("\nYou rolled a " + str(newSkillRoll) + " in " + str.title(stripSpacesOfSkill) + " with a score of " + str(skillScore)+"\n") # Print the roll number you got and the Skill Score.
                Autosave() # Saving the character info directly to the TXT sheet.
def levelUp(): # Oh hey you leveled up! this chunk is used when the current player XP exceeds the current level*10
    print("┌───────────┐\n│ LEVEL UP! │\n└───────────┘\n") # The fancy pop up box that says you leveled up!
    currentLevel = int(currentPlayerCharacterInfo[4]) # get current level as integer
    removedXPforLevelUp = (int(currentPlayerCharacterInfo.pop(6)) - (currentLevel*10)) # remove the XP from the total required to level up
    currentPlayerCharacterInfo.insert(6, removedXPforLevelUp) # inserts that number back into the list
    currentLevel = int(currentPlayerCharacterInfo.pop(4)) + 1 # straight up removes the level and adds 1 for re-insertion
    currentPlayerCharacterInfo.insert(4, currentLevel) # inserts that number back into the list
    if int(currentPlayerCharacterInfo[4]) % 5 == 0: # If the level is a multiple of 5 it offers the option to increase your Int or Str
        StrIntLvl = input("Your Body and Mind are in sync...\nDo you focus on your Strength or Intelligence? ") # Does your input start with an "I"
        if StrIntLvl[0:1] == "i": # great! you did the thing!
            upgradeIntelligence = int(currentPlayerCharacterInfo.pop(12)) + 1 # pops the element and adds 1
            currentPlayerCharacterInfo.insert(16, str(upgradeIntelligence)) # inserts that number back into the list
            upgradeEnergy = int(currentPlayerCharacterInfo.pop(16)) + 2 # pops the element and adds 2
            currentPlayerCharacterInfo.insert(16, str(upgradeEnergy)) # inserts that number back into the list
            print("\nYou have chosen to Focus on your Mind.\n") # says what you just did...
        else: # thats not an "I" so im guessing you wanted str instead
            upgradeStrength = int(currentPlayerCharacterInfo.pop(10)) + 1 # pops the element and adds 1
            currentPlayerCharacterInfo.insert(14, str(upgradeStrength)) # inserts that number back into the list
            upgradeHealth = int(currentPlayerCharacterInfo.pop(14)) + 2 # pops the element and adds 2
            currentPlayerCharacterInfo.insert(14, str(upgradeHealth)) # inserts that number back into the list
            print("\nYou have chosen to Focus on your Body.\n") # says what you just did...
    levelUpToken = 1 # Adjustable token for allowing the amount of health and energy upgrade points allowed during a level up
    Autosave() # Saving the character info directly to the TXT sheet.
    while levelUpToken > 0: # as long a token is allowed you can level up your health and energy too
        chooseStatToUpgrade = str.lower(input("Would you like more Health or more Energy? ")) # asking nicely
        if chooseStatToUpgrade[:1] == "e": # does the entry start with an E? well you just got +1 energy!
            upgradeEnergy = int(currentPlayerCharacterInfo.pop(16)) + 1 # pops the element and adds 1
            currentPlayerCharacterInfo.insert(16, str(upgradeEnergy)) # inserts that number back into the list
            print("\nYou have chosen to increase your Energy Reserves.\n") # says what you just did...
            levelUpToken -= 1 # removes an upgrade token counter so you dont get stuck here.
        elif chooseStatToUpgrade[:1] == "h": # does the entry start with an H? well you just got +1 health!
            upgradeHealth = int(currentPlayerCharacterInfo.pop(14)) + 1 # pops the element and adds 1
            currentPlayerCharacterInfo.insert(14, str(upgradeHealth)) # inserts that number back into the list
            print("\nYou have chosen to increase your Health Reserves.\n") # says what you just did...
            levelUpToken -= 1 # removes an upgrade token counter so you dont get stuck here.
        else: # Answered completely wrong? That's not good, try again.
            print("That is not a valid entry.") # says what you just did...
    Autosave() # Saving the character info directly to the TXT sheet.
    os.system('cls') # Clears the screen to keep things clean.
    print("Level Up Complete!") # Oh hey you did the thing! Congrats!
    dailyReset() # reset health and energy to max
def dailyReset(): # Did you sleep or level up? this resets your health and energy to max
    finalRestoreHealth = currentPlayerCharacterInfo[14] # gets the max health stat
    currentPlayerCharacterInfo.pop(18) # straight up removes the current health
    currentPlayerCharacterInfo.insert(18, str(finalRestoreHealth)) # inserts that number back into the list
    finalRestoreEnergy = currentPlayerCharacterInfo[16] # gets the max energy stat
    currentPlayerCharacterInfo.pop(20) # straight up removes the current energy
    currentPlayerCharacterInfo.insert(20, str(finalRestoreEnergy)) # inserts that number back into the list
    Autosave() # Saving the character info directly to the TXT sheet.
    print("\nHealth and Energy Restored!\n") # now you can use more skills!
#### SCRIPT ACTUALLY STARTS HERE!
os.system('cls') # Clears the screen to keep things clean.
if path.exists(saveFile) != True: # Is there a sheet already made...
    PlayerCharacterDatabase = open(saveFile, "w+") # No? make one!
else: # yes, the sheet exists?
    PlayerCharacterDatabase = open(saveFile, "r") # just read from it and dont overwrite it
for PlayerCharacterData in PlayerCharacterDatabase.readlines(): # take the information from the sheet
    currentPlayerCharacterInfo.append(PlayerCharacterData.rstrip("\n")) # place it into the list at the top called "currentPlayerCharacterInfo"
PlayerCharacterDatabase.close() # Close the TXT file, you dont need to keep it open.
if not currentPlayerCharacterInfo: # If there is nothing in the list called "currentPlayerCharacterInfo" even after the import of the sheet we start making a new character for you.
    enterNewPlayerCharacterName = str.title(input("What is your character's name? ")) # New Name, who dis?
    enterNewPlayerCharacterRace = str.title(input("What is the race of "+enterNewPlayerCharacterName+"? ")) # New Race, who dis?
    enterNewPlayerCharacterDamageStyle = str.lower(input("Are you Physical or Magical? ")) # Are you a brute or will you spell magical correctly?
    newCharList = [enterNewPlayerCharacterName, "Race", enterNewPlayerCharacterRace, "Level", 1, "XP", 0] # make a list of things that need to be at the top of the sheet
    currentPlayerCharacterInfo.extend(newCharList) # add it to the list at the top
    newCharacterStats() # make new char stats
    Skillz = startingCharSkills.copy() # Get the list of skills from the top
    while len(Skillz) > 0: # check if the copied list isnt empty
        currentPlayerCharacterInfo.append(Skillz.pop(0)) # add the skill in line
        currentPlayerCharacterInfo.append("0") # add the level of a new skill which is 0
    Autosave() # Saving the character info directly to the TXT sheet.
os.system('cls') # Clears the screen to keep things clean.
print("\n\nWelcome to your Super Basic RPG Character Sheet!\n\n") # WELCOME TO AUTOMATICALY MATHING YOUR STATS
Playing = True # mainly here for making sure when you save and quit there is an actual exit condition
while Playing == True: # obv if you're playing its going to be true lul
    Autosave() # Saving the character info directly to the TXT sheet.
    while int(currentPlayerCharacterInfo[6]) >= int(currentPlayerCharacterInfo[4])*10: # checking if the XP is higher than the level*10
        levelUp() # do the levelup dance!
    startScreenSelection = "" # clears the start screen selector so you can do stuff
    lastThing = "" # lastThing really isnt a last item or object, it just makes the bottom dashes equidistant to the top dashes when the name is inserted.
    for _ in range(len(currentPlayerCharacterInfo[0])): lastThing += "-" # easy to watch in action, hard to explain. checks how long the name is and makes the bottom dashes equal to the top ones.
    print("------------ "+currentPlayerCharacterInfo[0]+" ------------\n\nLevel "+str(currentPlayerCharacterInfo[4])+" - "+str(currentPlayerCharacterInfo[6])+"/"+str(int(currentPlayerCharacterInfo[4])*10)+" XP\nRace: "+str(currentPlayerCharacterInfo[2])+"\n"+str(currentPlayerCharacterInfo[7]) + " - "+str(currentPlayerCharacterInfo[8])+"\n"+str(currentPlayerCharacterInfo[18])+"/"+str(currentPlayerCharacterInfo[14])+" Health"+"\n"+str(currentPlayerCharacterInfo[20])+"/"+str(currentPlayerCharacterInfo[16])+" Energy"+"\n"+"\nUse \"roll [skill]\" to use a skill"+"\n1. View Skills"+"\n2. Long Rest"+"\n3. Inventory Manager"+"\n4. Save and Quit"+"\n-------------"+lastThing+"-------------") # ALL THE MAIN MENU INFO
    startScreenSelection = str.lower(input("\nPlease make a selection or roll a skill: ")) # time to put this thing to work! pick your poison below
    if startScreenSelection == "1" or startScreenSelection == "view skills": # if you want to see your current skills and level stats for them
        os.system('cls') # Clears the screen to keep things clean.
        print("Skills List:") # you gotta know what you are looking at
        unsplitter = currentPlayerCharacterInfo[21:] # get the skills and values
        skillListFix = [] # Empty list for appending things in the next loop
        for i in range(0, len(unsplitter), 2): # get every other items index
            skillListFix.append(str(unsplitter[i]) +": "+ str(unsplitter[i+1])) # append the 1st and 2nd item to a new list, at the index of the previous list, together with a colon seperating them
        splitter = int(len(skillListFix)/2) # makes a int that is half the total length of the list.
        SL1 = skillListFix[0:splitter] # first half of the list.
        SL2 = skillListFix[splitter:] # second half of the list.
        for key, value in zip(SL1,SL2): # I have no idea how this works yet, I found it in an online thread asking for what I wanted to do.
            print("{0:<25s}{1}".format(key, value)) # I need to learn this so i can figure out 2d lists and integrate them into the skill section.
        print() # empty space just cause it looks better
    elif startScreenSelection == "2" or startScreenSelection == "rest": # gotta reset those energy points
        os.system('cls') # Clears the screen to keep things clean.
        dailyReset() # resets health and energy to max
    elif startScreenSelection == "3": # inventory incomplete, dont ask because I dont know how im doing this yet.
        os.system('cls') # Clears the screen to keep things clean.
        print("\nView/Edit Inventory options are incomplete. Please try again later.\n") # if you read this and still need a comment please see a psychiatrist
    elif startScreenSelection == "4" or startScreenSelection == "quit" or startScreenSelection == "exit": # simple save and quit option
        Autosave() # Saving the character info directly to the TXT sheet.
        Playing = False # quiting the game like every other RPG out there.
        print(currentPlayerCharacterInfo[0]+"'s Info Saved! Thanks for playing!") # buh-bye! terminate program.
    elif startScreenSelection[0:1] == "r": # ROLLS! the most important part of a dice and math game!
        skillRollMultiplier = ''.join(numberCheck for numberCheck in startScreenSelection if numberCheck.isnumeric()) # strips everything in the input away to just numbers
        skillChosen = ''.join(numberCheck for numberCheck in startScreenSelection if numberCheck.isalpha() or numberCheck.isspace()) # gets everything that is a plan letter and space only
        splitFromFirstWord = (skillChosen.split(' ', 1)) # splits off the first word which is usually roll and turns them into a list
        stripSpacesOfSkill = str.strip(splitFromFirstWord[1]) # choose the second item in the list which is the skill and removes excess spaces at the begining and end
        if skillRollMultiplier == "": # if no number was provided after the skill
            skillRollMultiplier = 1 # if no number was provided it defaults to 1
        if str.title(stripSpacesOfSkill) in startingCharSkills: # if the skill you put in is actually on the list.
            skillRolling() # does the rolls that you input
        else: # if you didnt put in a skill correctly you didnt roll anything
            os.system('cls') # Clears the screen to keep things clean.
            print("\nThats not a Skill, Try harder.\n") # roll an actual skill please, there is a list for reference.
    else: # nothing matches so you get accosted
        os.system('cls') # Clears the screen to keep things clean.
        wrongList = ["\nEven electronic brain pancake crystal elderly.\n", "\nDo you even read, Bro?\n", "\nAre you even trying?\n", "\nThat wasn't useful, Try again.\n", "\nGG EZ Noob!\n", "\nMaybe you could use your fingers?\n", "\nDidn't see that coming... But it did.\n", "\nNext time roll for intelligence, you might need it.\n", "\nRead first, then type.\n", "\nHold on, let me just NOT do that...\n", "\nHappens to the best of us, but clearly you're not one of us.\n", "\nCan you at least use the last 2 brain cells you have?\n", "\nNo...\n", "\nI know, the first 30 years of childhood are the hardest.\n", "\nAnd this is why batman works alone.\n", "\nHow do I put this? You need to be \"not dumb.\"\n", "\nYou disgust me...\n", "\nI'm gunna smack you!\n", "\nUser faulty; please replace.\n", "\nI'm smarter than you and I dont even have a brain.\n", "\nError lies between keyboard and chair.\n", "\nID-10T report will be available shortly.\n", "\n\n"] # What? you cant read basic instructions!
        print(wrongList[random.randint(0,len(wrongList)-1)]) # chooses one of the previous lines
# End of the line...