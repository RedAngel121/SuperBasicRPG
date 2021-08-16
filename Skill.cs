namespace SuperBasicRPG
{
    enum characterSkill
    {
        Acrobatics, AnimalHandling, Arcana, Athletics, Barter, Bluff, Climb, Crafting, Diplomacy, Disguise, Engineering, Fabrication, Flora, History, Insight, Intimidate, Investigation, Medicine, Mining, Perception, Perform, Persuasion, Religion, SleightOfHand, Stealth, Survival, Swim
    }

    class Skill
    {
        decimal skillLevel { get; set; }
        string skillName { get; set; }
        string skillDescription { get; set; }

    }

}