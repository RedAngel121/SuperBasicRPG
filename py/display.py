# move all the main menu stuff here so it can be called and not part of the main.py
from character import Character
class display:
    def opening_banner():
        print("┌─────────────────────────────┐\n│ Welcome to Super Basic RPG! │\n└─────────────────────────────┘\n")

    def initial_name_input_request():
        print("Please enter the name of your character: ")

    def initial_race_input_request():
        print("Please enter the race of your character: ")

    def initial_desc_input_request():
        print("Describe your character: ")

    def chosen_one(name):
        print(f"You have chosen {name}...")

    def choose_class():
        print("Physical or Magical?")

    def main_menu():
        PC_Char = Character()
        print(f"------------ {PC_Char.get_name()} ------------\n\nLevel {PC_Char.get_level()} - {PC_Char.get_current_xp()}/{PC_Char.get_level() * 10} XP\nRace: {PC_Char.get_race()}\n{PC_Char.get_character_class()}? - {PC_Char.get_weapon()}\n{PC_Char.get_health_current()}/{PC_Char.get_health_max()} Health\n{PC_Char.get_mana_current()}/{PC_Char.get_mana_max()} Mana\n\nUse \"roll [skill name]\" to use a skill\n1. View Skills\n2. Long Rest\n3. Inventory Manager\n4. Save and Quit\n-------------{PC_Char.get_name_dashes()}-------------")
        # I am not sure it's going to work like this... but it'll work for now to stop some of the errors.
