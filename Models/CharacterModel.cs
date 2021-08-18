namespace SuperBasicRPG
{
    enum CharacterClass
    {
        Physical, Magical
    }
    class CharacterModel
    {
        protected string name { get; set; }
        int strength { get; set; }
        int intelligence { get; set; }
        CharacterClass characterClass { get; set; }
        int maxHealth { get; set; }
        int currentHealth { get; set; }
        int maxMana { get; set; }
        int currentMana { get; set; }
        int level { get; set; }
        int baseDamage { get; set; }
        int currentExperience { get; set; }
        string race { get; set; }
        string description { get; set; }
        decimal currency { get; set; }
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
