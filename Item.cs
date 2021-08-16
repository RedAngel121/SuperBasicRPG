namespace SuperBasicRPG
{
    enum material
    {
        Copper,
        Tin,
        Brass,
        Aluminum,
        Lead,
        Silver,
        Corundum,
        Iron,
        ColdIron,
        Electrum,
        Steel,
        Malachite,
        Gold,
        Tungsten,
        Platinum,
        Orichalcum,
        Moonstone,
        DwarvenSteel,
        Titanium,
        Mithril,
        Palladium,
        DragonSteel,
        Uranium238,
        Irridium,
        Uranium235,
        Inconel,
        Osmium,
        Adamantine,
        AntiMatter,
        SolidHelium
    }
    enum physicalWeaponType
    {
        Axe,
        Boomerang,
        Bow,
        Cane,
        Club,
        Crossbow,
        Dagger,
        Daibo,
        Explosive,
        FistWeapon,
        Flail,
        Hammer,
        Javelin,
        Mace,
        MagicOrb,
        Pickaxe,
        Pistol,
        Polearm,
        Rifle,
        Scythe,
        Shotgun,
        Shovel,
        Spear,
        Stave,
        Sword,
        Unarmed,
        Wand,
        Whip
    }

    enum magicalWeaponType
    {
        None,
        Acid,
        Anti,
        Art,
        Card,
        Crystal,
        Death,
        Earth,
        Electric,
        Fire,
        Gravity,
        Hair,
        Holy,
        Ice,
        Lava,
        Life,
        Light,
        Magiscript,
        Metal,
        Mind,
        Music,
        Plant,
        Shadow,
        Shield,
        Sonic,
        Tech,
        Time,
        Water,
        Wind
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