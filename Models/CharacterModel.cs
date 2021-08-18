namespace SuperBasicRPG
{
    enum CharacterClass
    {
        Physical, Magical
    }
    class CharacterModel
    {
        protected string name { get; set; }
        protected int strength { get; set; }
        protected int intelligence { get; set; }
        protected int maxHealth { get; set; }
        protected int currentHealth { get; set; }
        protected int maxMana { get; set; }
        protected int currentMana { get; set; }
        protected int level { get; set; }
        protected int baseDamage { get; set; }
        protected int currentExperience { get; set; }
        protected string race { get; set; }
        protected string description { get; set; }
        protected decimal currency { get; set; }
        CharacterClass characterClass { get; set; }
        Item[] inventory { get; set; }
        Skill[] skillsList { get; set; }
        /*
        int dexterity { get; set; }
        int constitution { get; set; }
        int vitality { get; set; }
        int perception { get; set; }
        int endurance { get; set; }
        int charisma { get; set; }
        int agility { get; set; }
        int wisdom { get; set; }
        int luck { get; set; }
        int education { get; set; }
        int socialStanding { get; set; }
        int morale { get; set; }
        int psionics { get; set; }
        int maxEnergy { get; set; }
        int currentEnergy { get; set; }
        int maxStamina { get; set; }
        int currentStamina { get; set; }
        int maxSpeed { get; set; }
        int currentSpeed { get; set; }
        int maxWeight { get; set; }
        decimal currentWeight { get; set; }
        */

    }
}
