import threading  # Import the threading module to create and manage threads

# Define a function that will be run by each thread
def thread_Surname(name):
    print(name + " Kane")  # Print the name followed by "Kane"

# List of names to be used by the threads
names = ["Harry", "David", "William", "Henry", "James"]

threads = list()  # Create an empty list to hold the thread objects

# Loop through each name in the list
for n in names:
    # Create a new thread for each name, passing the name as an argument
    t = threading.Thread(target=thread_Surname, args=(n,))
    threads.append(t)  # Add the thread to the list
    t.start()  # Start the thread

# Wait for user input to exit the program
input("Press Enter to exit...")
