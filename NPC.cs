namespace SuperBasicRPG
{
    enum MaleNames
    {
        Adon, Agro, Arlo, Azamarr, Baashar, Barak, Barton, Baske, Baxar, Blaiz, Caelan, Cassian, Clawsen, Colborn, Dagfinn, Dagrod, Dimian, Domnhar, Ebraheim, Eldermar, Embre, Esdel, Eune, Fangar, Favroe, Feron, Feston, Fintis, Gatlen, Gatlin, Gentar, Gethrod, Graff, Gunnar, Hagalbar, Hawke, Hemm, Henndar, Hezra, Hodus, Ishmael, Jakrin, Jareth, Jaris, Jather, Jerrick, Jessop, Jinto, Joz, Kadric, Kagran, Kaz, Kent, Khron, Kontas, Krinn, Lassrin, Lenox, Lothe, Lustros, Lydan, Malyen, Mavrek, Moki, Nazim, Nesso, Ophni, Pakker, Paquin, Paskel, Pike, Ptorik, Quintis, Rankar, Renham, Revvyn, Riordan, Rivik, Rourke, Roux, Ryven, Sarkin, Straus, Syrin, Talon, Tekren, Tez, Turrek, Tyvrik, Vadim, Vale, Varog, Verssek, Weston, Whit, Wulfe, Yorjan, Zaden, Zagaroth, Zenner
    }

    enum FemaleNames
    {
        Aeris, Afia, Agama, Anika, Annihya, Antia, Asralyn, Baakshi, Basak, Beatha, Beela, Belen, Braithe, Ciscra, Desmina, Dessa, Drusila, Elysa, Esmee, Esther, Estyn, Everen, Fidess, Hagar, Harper, Hartie, Heron, Herra, Ibera, Indie, Jesi, Jonna, Kessa, Ketra, Kory, Krynna, Kye, Larke, Lassona, Leska, Liris, Lunex, Lyla, Lynorr, Lynx, Maarika, Maeve, Magaltie, Merula, Minha, Morwena, Naima, Naphtalia, Orett, Palra, Partha, Pekka, Phlox, Phressa, Pret, Ralia, Rasy, Razra, Rei, Renalee, Resha, Reslyn, Rhays, Rhiannon, Rydna, Sage, Semet, Shike, Silene, Soko, Sonali, Sparrow, Surane, Syrana, Taewen, Talis, Tamrin, Temy, Tessel, Tezani, Thesra, Tisette, Tiv, Turi, Varin, Vemery, Vita, Vixra, Wren, Xavia, Yarri, Yelina, Yuni, Zara, Zet
    }
    enum FamilyNames
    {
        Abrielle, Acalia, Adair, Adara, Adriel, Aiyana, Alaire, Alissa, Alixandra, Altair, Amara, Anatola, Anya, Arcadia, Ariadne, Arianwen, Aurelia, Aurelian, Aurelius, Auristela, Avalon, Bastian, Breena, Briallan, Brielle, Briseis, Cambria, Cara, Carys, Caspian, Cassia, Cassiel, Cassiopeia, Cassius, Chaniel, Cora, Corbin, Cyprian, Dagen, Daire, Darius, Destin, Devlin, Devlyn, Drake, Drystan, Eira, Eirian, Eliron, Elysia, Eoin, Evadne, Evanth, Fineas, Finian, Fyodor, Gaerwn, Gareth, Gavriel, Ginerva, Griffin, Guinevere, Hadriel, Hannelore, Hermione, Hesperos, Iagan, Ianthe, Ignacia, Ignatius, Iseult, Isolde, Jessalyn, Kara, Katriel, Kerensa, Korbin, Kyler, Kyra, Kyrielle, Leala, Leila, Leira, Lilith, Liora, Liriene, Liron, Lucien, Lyra, Maia, Marius, Mathieu, Maylea, Meira, Mireille, Mireya, Natania, Neirin, Nerys, Nuriel, Nyfain, Nyssa, Oisin, Oleisa, Oralie, Orinthea, Orion, Orpheus, Ozara, Peregrine, Persephone, Perseus, Petronela, Phelan, Pryderi, Pyralia, Pyralis, Qadira, Quinevere, Quintessa, Raisa, Remus, Renfrew, Rhyan, Rhydderch, Riona, Saira, Saoirse, Sarai, Sarielle, Sebastian, Seraphim, Seraphina, Serian, Séverin, Sirius, Sorcha, Tavish, Tearlach, Terra, Thalia, Thaniel, Theia, Torian, Torin, Tressa, Tristana, Ulyssia, Uriela, Urien, Vanora, Vasilis, Vespera, Xanthus, Xara, Xylia, Yadira, Yakira, Yeira, Yeriel, Yestin, Yseult, Zaira, Zaniel, Zarek, Zephyr, Zora, Zorion
    }
    class NPC
    {
        // This is going to be an automatic setup of NPC for the DM.
        // This needs to generate all stats, mats and abilities on demand.
        // This must also keep a permanent copy of the NPC.
        // Potential for player auto-character creation tool?
        int strength { get; set; }
        int dexterity { get; set; }
        int constitution { get; set; }
        int vitality { get; set; }
        int perception { get; set; }
        int endurance { get; set; }
        int charisma { get; set; }
        int intelligence { get; set; }
        int agility { get; set; }
        int wisdom { get; set; }
        int luck { get; set; }
        CharacterClass characterClass { get; set; }
        int maxHealth { get; set; }
        int currentHealth { get; set; }
        int maxStamina { get; set; }
        int currentStamina { get; set; }
        int maxMana { get; set; }
        int currentMana { get; set; }
        int maxSpeed { get; set; }
        int currentSpeed { get; set; }
        int maxWeight { get; set; }
        int currentWeight { get; set; }
        int level { get; set; }
        int baseDamage { get; set; }
        int currentExperience { get; set; }
        string name { get; set; }
        string race { get; set; }
        string description { get; set; }
        int currency { get; set; }

        Item[] inventory { get; set; }
        Skill[] skillsList { get; set; }

    }

}