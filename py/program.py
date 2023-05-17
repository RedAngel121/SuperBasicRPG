class Database:
    def CreateDataBase():
        # Implementation for creating the database
        pass


class Character:
    def __init__(self):
        self.name = ""

    def UpdateName(self, name):
        # Implementation for updating the character's name
        pass

    def GetName(self):
        return self.name


class Display:
    @staticmethod
    def OpeningBanner():
        # Implementation for displaying the opening banner
        pass

    @staticmethod
    def InitialRaceInputRequest():
        # Implementation for requesting initial race input
        pass

    @staticmethod
    def InitialDescInputRequest():
        # Implementation for requesting initial description input
        pass

    @staticmethod
    def ChooseClass():
        # Implementation for choosing a class
        pass

    @staticmethod
    def InitialNameInputRequest():
        # Implementation for requesting initial name input
        pass

    @staticmethod
    def ChosenOne(name):
        # Implementation for displaying the chosen character name
        pass

    @staticmethod
    def MainMenu():
        # Implementation for displaying the main menu
        pass


def CreateNewChar():
    Display.InitialRaceInputRequest()
    userInputRace = input()
    Display.InitialDescInputRequest()
    userInputDesc = input()
    # Description should be optional.
    Display.ChooseClass()
    userInputClass = input()
    """ 
    Generate STR/INT Stats, double for health/mana.
    Match health/mana max and current.
    Lvl 1, Exp 0, Base dmg based on level and STR
    Add Wooden Sword or Wooden Wand based on class.
    Finally, Write to character sheet.
    """


def OpenExistingChar():
    # Access Database and retrieve info
    pass


def Main():
    Database.CreateDataBase()
    userInputName, userInputRace, userInputDesc, userInputClass = "", "", "", ""
    currentChar = Character()
    Display.OpeningBanner()

    # 1st search database for existing character names, if none exist then default to creating a new character.

    while True:
        Display.InitialNameInputRequest()
        userInputName = input()
        if currentChar.UpdateName(userInputName):
            break

    if currentChar.GetName() == "Existing Database Name":
        OpenExistingChar()
        Display.ChosenOne(currentChar.GetName())
    else:
        CreateNewChar()
        OpenExistingChar()  # Complete This Function so it will open a newly created character as well.
    Display.MainMenu()


if __name__ == "__main__":
    Main()