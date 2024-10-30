import multiprocessing  # Import the multiprocessing module to handle processes in Windows
import os  # Import the os module to get the current process ID

def padre():
    while True:  # Start an infinite loop
        new_process = multiprocessing.Process(target=hijo)  # Create a new process that will run the hijo function
        new_process.start()  # Start the new process
        pids = (os.getpid(), new_process.pid)  # Get the parent process ID and the new child process ID
        print("Parent: %d, Child: %d\n" % pids)  # Print the IDs of the parent and child processes
        reply = input("Press 's' if you want to create a new process: ")  # Ask the user to press 's' to create a new process
        if reply != 's':  # If the user does not press 's', break the loop
            break
            
def hijo():
    print('\n>>>>>>>>>>>>>>>> New child created with pid %d about to exit <<<<<<<<<<<<' % os.getpid())  # Print a message indicating a new child process has been created with its ID
        
if __name__ == '__main__':  # Check if the script is being run directly (not imported as a module)
    padre()  # Call the padre function to start the process