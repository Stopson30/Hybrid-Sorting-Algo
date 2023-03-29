using System;

namespace AnthropocBiasUrn
{
    class Program
    {
        static void Main(string[] args)
        {
            const int numTrials = 100000;
            int headsCount = 0;
            int whiteCount = 0;
            int headsAndWhiteCount = 0;

            var rand = new Random();

            for (int i = 0; i < numTrials; i++)  // whoah so here we go with a C# loop finally lol 
            {
                bool coin = rand.Next(2) == 0; // 0 = heads, 1 = tails

                if (coin)
                {
                    headsCount++;
                    bool white = rand.Next(2) == 0; // 0 = white, 1 = black
                    if (white)
                    {
                        whiteCount++;
                        if (i == 0)
                        {
                            headsAndWhiteCount++; // First person drew a white ball
                        }
                    }
                }
                else
                {
                    bool black = rand.Next(2) == 0; // 0 = black, 1 = white
                    if (black && i == 0)
                    {
                        headsAndWhiteCount = 0; // First person drew a black ball, so no white balls
                    }
                }
            }

            double pHeadsGivenWhite = (double)headsAndWhiteCount / whiteCount;

            Console.WriteLine($"Probability of the coin landing heads given that a white ball was observed: {pHeadsGivenWhite:P2}");
        }
    }
}
