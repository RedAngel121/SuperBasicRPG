using System;
namespace SuperBasicRPG
{
    class Character : CharacterModel
    {
        public Character()
        {
            Console.WriteLine("Creating New Character...");
        }
        // Character class is set by the initial dice rolls, if you assign higher STR then you get a physical class.
        // You are not allowed to roll the same number for each stat.
        // I may end up letting the player decide on a class but thats not going to be anytime soon.
        public bool updateName(string enteredName)
        {
            bool updateNameSuccessCheck = false;
            // TODO: check list of existing names.
            // return bool on success/failure of new name.
            this.name = enteredName;
            return updateNameSuccessCheck;
        }

        internal string GetName()
        {
            return this.name;
        }
    }
}

// eventually I want to add the ability to do hit/miss, and have other skills factor into a roll.
// To start I want to have an automatic character creation system to get things rolling.