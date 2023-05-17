class Character: #EntityLivingModel
    def __init__(self):
        # WHERE/HOW DO I INITIALIZE THE DATABASE???
        # Separate file called database.py where all that information takes place.
        # Once I get the database initialization completed I won't have to worry about it, Set it and Forget it.
        print("Checking Database...")
    
    def update_name(self, entered_name):
        self.name = entered_name
        return True

    def update_race(self, entered_race):
        self.race = entered_race
        return self.get_race() == entered_race

    def update_class(self, entered_class):
        self.character_class = entered_class
        return True  # This section is obviously wrong but I don't know how to fix it yet.
    
    def get_character_class(self):
        return self.character_class  # I need to have the 'class choice option' functional in order to write to the DB

    def get_weapon(self):
        return self.weapon_info  # I need to have the weapon system semi-functional in order to write to the DB

    def get_tool(self):
        return self.tool_info  # I need to have the tool system semi-functional in order to write to the DB

    def get_name(self):
        return self.name

    def get_race(self):
        return self.race

    def get_level(self):
        return self.level

    def get_current_xp(self):
        return self.experience

    def get_health_current(self):
        return self.health_current

    def get_health_max(self):
        return self.health_max

    def get_mana_current(self):
        return self.mana_current

    def get_mana_max(self):
        return self.mana_max