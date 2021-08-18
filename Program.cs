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
            string userInputName, userInputRace, userInputDesc;
            Character currentChar = new Character();
            Display.OpeningBanner();
            do
            {
                Display.InitialNameInputRequest();
                userInputName = Console.ReadLine();
            } while (!currentChar.updateName(userInputName));
            
            // I know this IF statement goes somewhere else but I cant be bothered to move it RN cause I dont know where to put it yet...
            if (true/* IF The name doesnt exist... */)
            {
                Display.InitialRaceInputRequest();
                userInputRace = Console.ReadLine();
                Display.InitialDescInputRequest();
                userInputDesc = Console.ReadLine();
            }
            Display.ChosenOne(currentChar.GetName());
            Display.MainMenu();
        }
    }
}