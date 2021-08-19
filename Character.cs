using System;
namespace SuperBasicRPG
{
    class Character : CharacterModel
    {
        public Character()
        {
            // WHERE/HOW DO I INITIALIZE THE DATABASE?
            Console.WriteLine("Checking Database...");
        }
        public bool UpdateName(string enteredName)
        {
            bool updateNameSuccessCheck = false;
            // TODO: check list of existing names in the database.
            // If Existing Name is False, send to 'Create New Character'.
            // Double check with the user to make sure they want to create a new char IF chars already exist.
            this.name = enteredName;
            return updateNameSuccessCheck;
        }
        public bool UpdateRace(string enteredRace)
        {
            bool updateRaceSuccessCheck;
            this.race = enteredRace;
            if (GetRace() == enteredRace)
            {
                updateRaceSuccessCheck = true;
            }
            else  // LET ME KNOW IF THIS IS COMPLETELY UNNECESSARY... or if I did it correctly (doubtful)
            {
                updateRaceSuccessCheck = false;
            }
            return updateRaceSuccessCheck;
        }
        public bool UpdateClass(string enteredClass)
        {
            this.characterClass = enteredClass;
            bool updateClassSuccessCheck = true;   // This section is obviously wrong but I dont know how to fix it yet. 
            return updateClassSuccessCheck;
        }

        internal string GetCharacterClass()
        {
            return this.characterClass; // TODO: FINISH THIS! I need to have the 'class choice option' functional in order to write to the DB
        }
        internal int GetWeapon()
        {
            return this.weaponInfo; // TODO: FINISH THIS! I need to have the weapon system semi-functional in order to write to the DB
        }
        internal string GetName()
        {
            return this.name;
        }
        internal string GetRace()
        {
            return this.race;
        }
        internal int GetLevel()
        {
            return this.level;
        }
        internal int GetCurrentXP()
        {
            return this.currentExperience;
        }
        internal int GetHealthCurrent()
        {
            return this.currentHealth;
        }
        internal int GetHealthMax()
        {
            return this.maxHealth;
        }
        internal int GetManaCurrent()
        {
            return this.currentMana;
        }
        internal int GetManaMax()
        {
            return this.maxMana;
        }

    }
}