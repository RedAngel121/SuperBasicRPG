namespace SuperBasicRPG
{
    enum characterSkill
    {
        Acrobatics, Animal Handling, Arcana, Athletics, Barter, Bluff, Climb, Crafting, Diplomacy, Disguise, Engineering, Fabrication, Flora, History, Insight, Intimidate, Investigation, Medicine, Mining, Perception, Perform, Persuasion, Religion, Sleight Of Hand, Stealth, Survival, Swim
    }

    class Skill
    {
        decimal skillLevel { get; set; }
        string skillName { get; set; }
        string skillDescription { get; set; }

    }

}