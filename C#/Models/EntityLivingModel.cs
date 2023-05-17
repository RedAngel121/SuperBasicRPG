// This file is to hold basic information that all living items have in common. Mainly Stats.
namespace SuperBasicRPG
{
    enum CharacterClass
    {
        Physical, Magical
    }
    class EntityLivingModel
    {
        // Item[] inventory { get; set; }
        // Skill[] skillsList { get; set; }
        // CharacterClass characterClass { get; set; }
        // Stats Start here...
        protected string name { get; set; }
        protected string race { get; set; }
        protected string description { get; set; }
        protected decimal currency { get; set; }
        protected int level { get; set; }
        protected int experience { get; set; }
        protected int strength { get; set; }
        protected int intelligence { get; set; }
        // Stats above determine Stats below
        protected int health_Max { get; set; }
        protected int health_Current { get; set; }
        protected int mana_Max { get; set; }
        protected int mana_Current { get; set; }
        protected int baseDamage { get; set; }
        protected int damage_Max { get; set; }
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
        protected int energy_Max { get; set; }
        protected int energy_Current { get; set; }
        protected int stamina_Max { get; set; }
        protected int stamina_Current { get; set; }
        protected int speed_Max { get; set; }
        protected decimal speed_Current { get; set; }
        protected int weight_Max { get; set; }
        protected decimal weight_Current { get; set; }
        protected int armor_Natural { get; set; }
        protected int armor_Fabricated { get; set; }
        protected int armor_Magic { get; set; }
        protected int armor_Base { get; set; }
        
        */

    }
}