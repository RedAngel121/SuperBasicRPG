namespace SuperBasicRPG
{
    enum Material
    {
        Wood, Stone, Copper, Tin, Brass, Aluminum, Lead, Glass, Silver, Corundum, Iron, Cold_Iron, Electrum, Steel, Malachite, Gold, Tungsten, Platinum, Orichalcum, Moonstone, Dwarven_Steel, Titanium, Mithril, Palladium, Dragon_Steel, Uranium_238, Irridium, Uranium_235, Inconel, Osmium, Adamantine, Anti_Matter, Solid_Helium
        // Add more types in order of exponent value.
    }
    enum PhysicalWeapon
    {
        Axe, Boomerang, Bow, Cane, Club, Crossbow, Dagger, Daibo, Explosive, Fist_Weapon, Flail, Hammer, Javelin, Mace, Magic_Orb, Pickaxe, Pistol, Polearm, Rifle, Scythe, Shotgun, Shovel, Spear, Stave, Sword, Unarmed, Wand, Whip
    }
    enum MagicalType
    {
        None, Acid, Anti, Art, Card, Crystal, Death, Earth, Electric, Fire, Gravity, Hair, Holy, Ice, Lava, Life, Light, Magiscript, Metal, Mind, Music, Plant, Shadow, Shield, Sonic, Tech, Time, Water, Wind
        // Organize these so they are listed in order of value... easier said than done. (not sure if this is required or optional)
    }
    enum BulkTrade
    {
        Tiny, Puny, Compact, Small, Unpleasant, Sleek, Subpar, Average, Adequate, Unique, Sizeable, Substantial, Significant, Enormous, Colossal, Extensive, Massive, Ridiculous, LargerThanLife, Galactic, TOOMUCH
        // These are listed in order of smallest to largest in exponent value.
    }
    class EntityInertModel
    {
        int price { get; set; }
        int weight { get; set; }
        int baseDMG { get; set; }
        string material { get; set; }
        string magic { get; set; }
        string toolType { get; set; } // Everything is a tool,
        bool weapon { get; set; } // But not everything is a weapon.
        string name { get; set; }
        string description { get; set; }
    }
}