using System;
namespace SuperBasicRPG
{
    class Character : CharacterModel
    {
        public Character()
        {
            Console.WriteLine("Checking Database...");
        }
        // Character class is set by the initial dice rolls, if you assign higher STR then you get a physical class.
        // You are not allowed to roll the same number for each stat.
        // I may end up letting the player decide on a class but thats not going to be anytime soon.
        public bool updateName(string enteredName)
        {
            bool updateNameSuccessCheck = false;
            // TODO: check list of existing names in the database.
            // If Existing Name is False, send to 'Create New Character'.
            // Double check with the user to make sure they want to create a new char IF chars already exist.
            this.name = enteredName;
            return updateNameSuccessCheck;
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
        internal string GetCharacterClass()
        {
            return this.characterClass;
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
        internal int GetWeapon()
        {
            return this.FIX_WeaponInfo;
        }
        
    }
}
/*
eventually I want to add the ability to do hit/miss, and have other skills factor into a roll.
To start I want to have an automatic character creation system to get things rolling.
*/