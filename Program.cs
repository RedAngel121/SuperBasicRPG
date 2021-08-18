using System;
namespace SuperBasicRPG
{

    class Program
    {
        static void Main(string[] args)
        {
            // Get list of '.char' files saved to the database.
            // If no '.char' files exist, start making a new char.
            // If old '.char' files exist, then find the name of the character and match it to the input.
            // When matched correctly, the character will load into the menu.
            string userInputName;
            Character currentChar = new Character();
            Display.OpeningBanner();
            do
            {
                Display.InitialNameInputRequest();
                userInputName = Console.ReadLine();
            } while (!currentChar.updateName(userInputName));
            Display.ChosenOne(currentChar.GetName());

            if (currentChar.updateName(userInputName))
            {
                Display.MainMenu();
            }

            /*
            else
            {
                Console.WriteLine("Please enter the race of your Character: ");
                string userInputRace = Console.ReadLine();
                Console.WriteLine("Describe your character: ");
                string userInputDesc = Console.ReadLine();
            }
            I have a vague idea where to start here...
            */
        }
    }
}