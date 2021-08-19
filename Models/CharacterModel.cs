namespace SuperBasicRPG
{
    enum CharacterClass
    {
        Physical, Magical
    }
    class CharacterModel
    {
        Item[] inventory { get; set; }
        Skill[] skillsList { get; set; }
        CharacterClass characterClass { get; set; } // Chosen during character creation.
        // Stats Start here...
        protected string name { get; set; }
        protected string race { get; set; }
        protected string description { get; set; }
        protected decimal currency { get; set; }
        protected int level { get; set; }
        protected int currentExperience { get; set; }
        protected int strength { get; set; }
        protected int intelligence { get; set; }
        // Stats above determine Stats below
        protected int maxHealth { get; set; }
        protected int currentHealth { get; set; }
        protected int maxMana { get; set; }
        protected int currentMana { get; set; }
        protected int baseDamage { get; set; }
        /*
        protected int dexterity { get; set; }
        protected int constitution { get; set; }
        protected int vitality { get; set; }
        protected int perception { get; set; }
        protected int endurance { get; set; }
        protected int charisma { get; set; }
        protected int agility { get; set; }
        protected int wisdom { get; set; }
        protected int luck { get; set; }
        protected int education { get; set; }
        protected int socialStanding { get; set; }
        protected int morale { get; set; }
        protected int psionics { get; set; }
        // Stats above determine Stats below
        protected int maxEnergy { get; set; }
        protected int currentEnergy { get; set; }
        protected int maxStamina { get; set; }
        protected int currentStamina { get; set; }
        protected int maxSpeed { get; set; }
        protected int currentSpeed { get; set; }
        protected int maxWeight { get; set; }
        protected decimal currentWeight { get; set; }
        */

    }
}
