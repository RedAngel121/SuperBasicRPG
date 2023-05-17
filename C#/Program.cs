using System;
namespace SuperBasicRPG
{
    class Program
    {
        static void Main(string[] args)
        {
            Database.CreateDataBase();
            string userInputName, userInputRace, userInputDesc, userInputClass;
            Character currentChar = new Character();
            Display.OpeningBanner();

            // 1st search database for existing character names, if none exist then default to creating a new character.

            void CreateNewChar()
            {
                Display.InitialRaceInputRequest();
                userInputRace = Console.ReadLine();
                Display.InitialDescInputRequest();
                userInputDesc = Console.ReadLine();
                // Description should be optional.
                Display.ChooseClass();
                userInputClass = Console.ReadLine();
                /* 
                Generate STR/INT Stats, double for health/mana.
                Match health/mana max and current.
                Lvl 1, Exp 0, Base dmg based on level and STR
                Add Wooden Sword or Wooden Wand based on class.
                Finally, Write to character sheet.
                */
            }

            void OpenExistingChar()
            {
                // Access Database and retireve info.
            }

            do
            {
                Display.InitialNameInputRequest();
                userInputName = Console.ReadLine();
            } while (!currentChar.UpdateName(userInputName));

            if (currentChar.GetName() == "Existing Database Name")
            {
                OpenExistingChar();
                Display.ChosenOne(currentChar.GetName());
            }
            else
            {
                CreateNewChar();
            }
            OpenExistingChar(); // Complete This Function so it will open a newly created character as well.
            Display.MainMenu();
        }
    }
}