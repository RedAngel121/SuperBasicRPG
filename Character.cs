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
        int dexterity { get; set; }
        int constitution { get; set; }
        int vitality { get; set; }
        int perception { get; set; }
        int endurance { get; set; }
        int charisma { get; set; }
        int intelligence { get; set; }
        int agility { get; set; }
        int wisdom { get; set; }
        int luck { get; set; }
        characterClass characterClass { get; set; }
        // Character class is set by the initial dice rolls, if you assign higher STR then you get a physical class.
        // You are not allowed to roll the same number for each stat.
        // I may end up letting the player decide on a class but thats not going to be anytime soon.
        int maxHealth { get; set; }
        int currentHealth { get; set; }
        int maxStamina { get; set; }
        int currentStamina { get; set; }
        int maxMana { get; set; }
        int currentMana { get; set; }
        int maxEnergy { get; set; }
        int currentEnergy { get; set; }
        int maxSpeed { get; set; }
        int currentSpeed { get; set; }
        int maxWeight { get; set; }
        int currentWeight { get; set; }
        int level { get; set; }
        int baseDamage { get; set; }
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