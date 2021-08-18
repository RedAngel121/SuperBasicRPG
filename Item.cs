namespace SuperBasicRPG
{
    enum Material
    {
        Wood, Stone, Copper, Tin, Brass, Aluminum, Lead, Silver, Corundum, Iron, Cold_Iron, Electrum, Steel, Malachite, Gold, Tungsten, Platinum, Orichalcum, Moonstone, Dwarven_Steel, Titanium, Mithril, Palladium, Dragon_Steel, Uranium_238, Irridium, Uranium_235, Inconel, Osmium, Adamantine, Anti_Matter, Solid_Helium
    }
    enum PhysicalWeaponType
    {
        Axe, Boomerang, Bow, Cane, Club, Crossbow, Dagger, Daibo, Explosive, Fist_Weapon, Flail, Hammer, Javelin, Mace, Magic_Orb, Pickaxe, Pistol, Polearm, Rifle, Scythe, Shotgun, Shovel, Spear, Stave, Sword, Unarmed, Wand, Whip
    }
    enum MagicalWeaponType
    {
        None, Acid, Anti, Art, Card, Crystal, Death, Earth, Electric, Fire, Gravity, Hair, Holy, Ice, Lava, Life, Light, Magiscript, Metal, Mind, Music, Plant, Shadow, Shield, Sonic, Tech, Time, Water, Wind
    }
    enum BulkTrade
    {
        Tiny, Puny, Compact, Small, Unpleasant, Sleek, Subpar, Average, Adequate, Unique, Sizeable, Substantial, Significant, Enormous, Colossal, Extensive, Massive, Ridiculous, LargerThanLife, Galactic, TOOMUCH
        // These are listed in order of smallest to largest.
    }
    class Item
    {
        int price { get; set; }
        int weight { get; set; }
        string materialType { get; set; }
        string magicType { get; set; }
        string weaponType { get; set; }
        string name { get; set; }
        string description { get; set; }
    }
}