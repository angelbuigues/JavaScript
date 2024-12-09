"""
Exercise: Creating and Managing Threads 
Objective: Practice creating and managing threads in Python to perform concurrent tasks.

Description:

In this exercise, you will create a program that uses multiple threads to print different messages to the console.
Each thread will print a specific message with a specified delay between each print.
The goal is to observe how threads can run concurrently and how their outputs can interleave.

Instructions:

Create a function called print_message that takes two arguments: a message (message) and a delay (delay).

The function should print the message 10 times, with the specified delay between each print.
In the main function (main):

Print “Program start”.
Create three threads:
The first thread should call print_message with the message “A” and a delay of 0.1 seconds.
The second thread should call print_message with the message “B” and a delay of 0.2 seconds.
The third thread should call print_message with the message “C” and a delay of 0.3 seconds.
Start all three threads.
Wait for all three threads to finish using the join method.
Print “Program end”.
Ensure that the main program runs only if the script is executed directly.

Add a pause at the end of the program to view the output before the console closes
"""
import threading
from time import sleep

def print_message(message, delay):
    for _ in range(10):
        print(message, end=",")
        sleep(delay)

def main():
    print("Program start")

    # Crear los hilos
    t1 = threading.Thread(target=print_message, args=("A", 0.1))
    t2 = threading.Thread(target=print_message, args=("B", 0.2))
    t3 = threading.Thread(target=print_message, args=("C", 0.3))

    # Iniciar los hilos
    t1.start()
    t2.start()
    t3.start()

    # Esperar que los hilos terminen
    t1.join()
    t2.join()
    t3.join()

    print("\nProgram end")
    input("Press Enter to close the console...")

if __name__ == "__main__":
    main()
