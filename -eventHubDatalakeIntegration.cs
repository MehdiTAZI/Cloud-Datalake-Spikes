using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using Microsoft.ServiceBus.Messaging;

namespace ConsoleApp1
{
    class Program
    {
        static string eventHubName = "iot";
        static string connectionString = "Endpoint=sb://itieventhub.servicebus.windows.net/;SharedAccessKeyName=IoTProducer;SharedAccessKey=xxxxxxxxxxxxxxxxxxxxxxxxxxx";

        static void Main(string[] args)
        {
            Console.WriteLine("Press Ctrl-C to exit");
            SendingRandomMessages();
        }

        static void SendingRandomMessages()
        {
            var eventHubClient = EventHubClient.CreateFromConnectionString(connectionString, eventHubName);
            while (true)
            {
                try
                {
                    var random = new Random().Next();
                    var message = DateTime.Now.ToShortTimeString().ToString() + ";" + "my IoT Object" + ";" + random.ToString();
                    eventHubClient.Send(new EventData(Encoding.UTF8.GetBytes(message)));
                }
                catch (Exception exception)
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("{0} > Exception: {1}", DateTime.Now, exception.Message);
                    Console.ResetColor();
                }

                Thread.Sleep(200);
            }
        }
    }
}
