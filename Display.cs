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

    }
}