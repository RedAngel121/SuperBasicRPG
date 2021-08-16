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





        // Bulk Trade Goods
        int bulkTradeTiny = 1;
        int bulkTradePuny = 2;
        int bulkTradeCompact = 4;
        int bulkTradeSmall = 8;
        int bulkTradeUnpleasant = 16;
        int bulkTradeSleek = 32;
        int bulkTradeSubpar = 64;
        int bulkTradeAverage = 128;
        int bulkTradeAdequate = 256;
        int bulkTradeUnique = 512;
        int bulkTradeSizeable = 1024;
        int bulkTradeSubstantial = 2048;
        int bulkTradeSignificant = 4096;
        int bulkTradeEnormous = 8192;
        int bulkTradeColossal = 16384;
        int bulkTradeExtensive = 32768;
        int bulkTradeMassive = 65536;
        int bulkTradeRidiculous = 131072;
        int bulkTradeLargerThanLife = 262144;
        int bulkTradeGalactic = 524288;
        int bulkTradeTOOMUCH = 1048576;
    }

}