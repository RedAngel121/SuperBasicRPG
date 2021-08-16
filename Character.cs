namespace SuperBasicRPG
{
    enum characterClass
    {
        Physical, Magical
    }

    class Character
    {
        public string characterBasicInfo;
        
        int strength { get; set; }
        int intelligence { get; set; }
        characterClass characterClass { get; set; }
        // Character class is set by the initial dice rolls, if you assign higher STR then you get a physical class.
        // You are not allowed to roll the same number for each stat.
        // I may end up letting the player decide on a class but thats not going to be anytime soon.
        int maxHealth { get; set; }
        int currentHealth { get; set; }
        int maxMana { get; set; }
        int currentMana { get; set; }
        int level { get; set; }
        int currentExperience { get; set; }
        string name { get; set; }
        string race { get; set; }
        string description { get; set; }
        int currency { get; set; }

        Item[] inventory { get; set; }
        Skill[] skillsList { get; set; }

    }

}

// eventuially I want to add the ability to do hit/miss, and have other skills factor into a roll