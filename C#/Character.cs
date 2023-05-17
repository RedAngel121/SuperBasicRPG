using System;
namespace SuperBasicRPG
{
    class Character : EntityLivingModel
    {
        public Character()
        {
            // WHERE/HOW DO I INITIALIZE THE DATABASE???
            // Seperate file called database.cs where all that information takes place.
            // Once I get the database initialization completed I wont have to worry about it, Set it and Forget it.
            Console.WriteLine("Checking Database...");
        }
        public bool UpdateName(string enteredName)
        {
            bool updateNameSuccessCheck = false;
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
            else  // LET ME KNOW IF THIS IS COMPLETELY UNNECESSARY... or if I did it correctly (which is doubtful)
            {
                updateRaceSuccessCheck = false;
            }
            return updateRaceSuccessCheck;
        }/*
        public bool UpdateClass(string enteredClass)
        {
            this.characterClass = enteredClass;
            bool updateClassSuccessCheck = true;   // This section is obviously wrong but I dont know how to fix it yet. 
            return updateClassSuccessCheck;
        }

        internal string GetCharacterClass()
        {
            return this.characterClass; // I need to have the 'class choice option' functional in order to write to the DB
        }
        internal int GetWeapon()
        {
            return this.weaponInfo; // I need to have the weapon system semi-functional in order to write to the DB
        }
        internal int GetTool()
        {
            return this.toolInfo; // I need to have the tool system semi-functional in order to write to the DB
        }
        */
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
            return this.experience;
        }
        internal int GetHealthCurrent()
        {
            return this.health_Current;
        }
        internal int GetHealthMax()
        {
            return this.health_Max;
        }
        internal int GetManaCurrent()
        {
            return this.mana_Current;
        }
        internal int GetManaMax()
        {
            return this.mana_Max;
        }

    }
}