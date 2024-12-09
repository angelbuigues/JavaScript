"""
Define several task functions:

greet: prints a greeting and waits for the user to press Enter.

write_chars: Prints 'X' and 'Y' characters alternately, with pauses between each print.

print_names: Prints a list of names with a suffix.

random_task: Assigns and displays random values to a thread-local variable.

show_thread_info: Displays information about the current thread.

Then you must create and manage threads for each task in such a way that they can overlap but the main one does not end up leaving some of them incomplete.
"""

import threading
import random
from time import sleep

def greet():
    print("Hello! Press Enter to continue...")
    input()

def write_chars():
    for _ in range(10):
        print("X", end="")
        sleep(0.1)
        print("Y", end="")
        sleep(0.1)
    print()

def print_names():
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        print(f"{name} Smith")
        sleep(0.1)

def random_task():
    local_data = threading.local()
    local_data.value = random.randint(1, 100)
    print(f"{threading.current_thread().name}: {local_data.value}")

def show_thread_info():
    print(f"Thread Name: {threading.current_thread().name}")
    print(f"Thread ID: {threading.current_thread().ident}")

threads = [
    threading.Thread(target=greet),
    threading.Thread(target=write_chars),
    threading.Thread(target=print_names),
    threading.Thread(target=random_task),
    threading.Thread(target=show_thread_info)
]

for t in threads:
    t.start()

for t in threads:
    t.join()

