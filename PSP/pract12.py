import subprocess  # Import the subprocess module to execute system commands

try:
    subprocess.run(['Notepad.exe'])  # Try to run the Notepad.exe program
    int(input("subprocess 1"))
    subprocess.run(["C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2407.9.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"])  # Try to run Notepad.exe from a specific path
    int(input("subprocess 2"))
    subprocess.run(['Notepad.exe', 'texto.txt'])  # Try to open the file texto.txt with Notepad.exe
    int(input("subprocess 3"))
    
except subprocess.CalledProcessError as e:  # Catch any CalledProcessError exceptions
    print(e.output)  # Print the error output