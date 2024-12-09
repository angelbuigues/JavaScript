""" Make a Python program that:
·       Get the current process with its name, ID, and priority using psutil.
·       Create a child process that performs a Google search for the word Python in the Google Chrome browser.
·       If the child process fails to open the browser, handle the exception and retry the search on the URL https://www.bing.com/search?q=Python and ping www.google.es.
·       Change the priority of the child process to the lowest value allowed on your operating system, handling any errors that occur.
·       Try to run a especific aplication from the computer in which you are doing the exam. Take a screenshot from it.

To upload this test compress the code and the screenshot of the execution of all the code in a zip file with the name: LastNameFirstNamePracticeTest.zip
To upload the screenshots you can do it with the method that you judge """

import psutil, os, multiprocessing, webbrowser, subprocess

# FIRST POINT

def currentProccess():
    proc = psutil.Process(os.getpid())
    processName = proc.name()
    processID = proc.pid
    processPrio = proc.nice()
    print("Name: ", processName, "--- ID: ", processID, "--- Priority: ", processPrio)


# SECOND POINT
def create_child():
    new_process = multiprocessing.Process(target=child)

    new_process.start()

    pids = (
        os.getpid(),
        new_process.pid,
    )

    print("Parent: %d, Child: %d\n" % pids)

# FOURTH POINT
def changePriority (pid):
    try:
        subprocess.check_output(
                [
                    "wmic",
                    "process",
                    "where",
                    f"processid={pid}",
                    "CALL",
                    "setpriority",
                    "below normal"
                ]
            )
    except subprocess.CalledProcessError as e:
        print(e.output)

def child():
    try:
        print("Child EXECUTED: %d\n" % os.getpid())
        # The next line raise an exception
        # os.nice()
        subprocess.run(
            [
                "C:\\Users\\servicpin2\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe",
                "http://www.google.com/search?q=Python"
            ]
        )
        # THIRD POINT
    except Exception as e:
        webbrowser.open("https://www.bing.com/search?q=Python")
        result = subprocess.run(
            ["ping", "www.google.es", "-n", "4"]
        )
        print(result.stdout)
    finally:
        print(psutil.Process(os.getpid()).nice())
        changePriority(os.getpid())
        print(psutil.Process(os.getpid()).nice())

# FIFTH POINT
def open_program():
    try:
        subprocess.run(["taskmgr.exe"])
    except subprocess.CalledProcessError as e:
        print(e.output)


if __name__ == "__main__":
    currentProccess()
    create_child()
    open_program()

