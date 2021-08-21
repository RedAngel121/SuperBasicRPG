using System;
namespace SuperBasicRPG
{
    public static class Display
    {
        public static void OpeningBanner()
        {
            Console.WriteLine("┌─────────────────────────────┐\n│ Welcome to Super Basic RPG! │\n└─────────────────────────────┘\n");
        }
        public static void InitialNameInputRequest()
        {
            Console.WriteLine("Please enter the name of your character: ");
        }
        public static void InitialRaceInputRequest()
        {
            Console.WriteLine("Please enter the race of your character: ");
        }
        public static void InitialDescInputRequest()
        {
            Console.WriteLine("Describe your character: ");
        }
        public static void ChosenOne(string name)
        {
            Console.WriteLine($"You have chosen {name}...");
        }
        public static void ChooseClass()
        {
            Console.WriteLine("Physical or Magical?");
        }
        public static void MainMenu()
        {
            Character PC_Char = new Character();
            // Console.WriteLine($"------------  {PC_Char.GetName()} +  ------------\n\nLevel  + {PC_Char.GetLevel()} +  -  + {PC_Char.GetCurrentXP()} + / + {PC_Char.GetLevel() * 10} +  XP\nRace:  + {PC_Char.GetRace()} + \n + {PC_Char.GetCharacterClass()}? +  -  + {PC_Char.GetWeapon()} + \n + {PC_Char.GetHealthCurrent()} + / + {PC_Char.GetHealthMax()} +  Health + \n + {PC_Char.GetManaCurrent()} + / + {PC_Char.GetManaMax()} +  Mana + \n + \nUse \"roll [skill name]\" to use a skill + \n1. View Skills + \n2. Long Rest + \n3. Inventory Manager + \n4. Save and Quit + \n------------- + {/*dashExtender FIX THIS */PC_Char.GetName()} + -------------");
            // I am not sure its going to work like this... but it'll work for now to stop some of the errors.
            // I know there is a better way to handle this, I'll have to talk to dev about it.

        }
    }
}