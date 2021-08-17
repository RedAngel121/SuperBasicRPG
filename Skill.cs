namespace SuperBasicRPG
{
    enum CharacterSkill
    {
        Acrobatics, Animal_Handling, Arcana, Athletics, Barter, Bluff, Climb, Crafting, Diplomacy, Disguise, Engineering, Fabrication, Flora, History, Insight, Intimidate, Investigation, Medicine, Mining, Perception, Perform, Persuasion, Religion, Sleight_Of_Hand, Stealth, Survival, Swim
    }
    enum AdditionalSkills
    {
        Admin, Advocate, Animals_Handling, Animals_Training, Animals_Veterinary, Art_Performer, Art_Holography, Art_Instrument, Art_Visual_Media, Art_Write, Astrogation, Athletics_Dexterity, Athletics_Endurance, Athletics_Strength, Broker, Carouse, Deception, Diplomat, Drive_Hovercraft, Drive_Mole, Drive_Track, Drive_Walker, Drive_Wheel, Electronics_Comms, Electronics_Computers, Electronics_Remote_Ops, Electronics_Sensors, Engineer_J_Drive, Engineer_Life_Support, Engineer_M_Drive, Engineer_Mech, Engineer_Power, Explosives, Flyer_Airship, Flyer_Grav, Flyer_Ornithopter, Flyer_Rotor, Flyer_Wing, Gambler, Gunner_Mech, Gunner_Capital, Gunner_Ortillery, Gunner_Screen, Gunner_Turret, Gun_Combat_Archaic, Gun_Combat_Energy, Gun_Combat_Slug, Heavy_Weapons_Artillery, Heavy_Weapons_Man_Portable, Heavy_Weapons_Vehicle, Investigate, Language_Spoken, Language_Written, Leadership, Mechanic, Medic, Melee_Blade, Melee_Bludgeon, Melee_Natural, Melee_Unarmed, Navigation, Persuade, Pilot_Mech, Pilot_Capital_Ships, Pilot_Small_Craft, Pilot_Spacecraft, Recon, Science_Archaeology, Science_Astronomy, Science_Biology, Science_Chemistry, Science_Cosmology, Science_Cybernetics, Science_Economics, Science_Genetics, Science_History, Science_Linguistics, Science_Philosophy, Science_Physics, Science_Planetology, Science_Psionicology, Science_Psychology, Science_Robotics, Science_Sophontology, Science_Xenology, Seafarer_Ocean_Ship, Seafarer_Personal, Seafarer_Sail, Seafarer_Submarine, Stealth, Steward, Streetwise, Survival, Tactics_Guerrilla, Tactics_Military, Tactics_Naval, Vacc_Suit
    }
    class Skill
    {
        decimal skillLevel { get; set; }
        string skillName { get; set; }
        string skillDescription { get; set; }
    }
}