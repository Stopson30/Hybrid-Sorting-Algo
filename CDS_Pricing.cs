using System;
using System.Collections.Generic;
using System.IO;
using ExcelDataReader;

namespace CreditSwapCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            // Read the input file and extract the put option data
            string inputFile = "put_options.xlsx";
            List<double> strikes = new List<double>();
            List<double> premiums = new List<double>();
            using (var stream = File.Open(inputFile, FileMode.Open, FileAccess.Read))
            {
                using (var reader = ExcelReaderFactory.CreateReader(stream))
                {
                    reader.Read(); // Skip the header row
                    while (reader.Read())
                    {
                        double strike = reader.GetDouble(0);
                        double premium = reader.GetDouble(1);
                        strikes.Add(strike);
                        premiums.Add(premium);
                    }
                }
            }

            // Calculate the price of a credit default swap using the put option data
            double cdsSpread = 0.05; // the spread of the credit default swap
            double defaultProbability = 0.05; // the probability of default
            double cdsPrice = 0;
            for (int i = 0; i < strikes.Count; i++)
            {
                double putValue = strikes[i] - premiums[i];
                cdsPrice += putValue * defaultProbability / (1 - defaultProbability) * cdsSpread;
            }

            // Output the result to the console
            Console.WriteLine($"The price of the credit default swap is {cdsPrice:C2}");
        }
    }
}
