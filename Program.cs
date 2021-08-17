using System;

namespace SuperBasicRPG
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Console.WriteLine("┌─────────────────────────────┐\n│ Welcome to Super Basic RPG! │\n└─────────────────────────────┘\n\nPlease enter the name of your Character: ");
                string userInputName = Console.ReadLine();
                Console.WriteLine("You have chosen " + userInputName);
                if (userInputName == "existing char name")
                {
                    string openExistingChar = "Done";
                    Console.WriteLine("You have chosen " + openExistingChar);
                }
                else
                {
                    Console.WriteLine("Please enter the race of your Character: ");
                    string userInputRace = Console.ReadLine();
                    Console.WriteLine("Describe your character: ");
                    string userInputDesc = Console.ReadLine();
                    Character char1 = new Character(userInputName, userInputRace, userInputDesc);
                }
                // I have no idea where to start here...
            }
            catch (System.Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

    }

}