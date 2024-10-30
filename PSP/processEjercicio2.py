import subprocess  # Import the subprocess module to execute system commands

def open_programs():
    try:
        subprocess.run(["C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2408.12.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"])  # Try to run Notepad.exe from a specific path
        subprocess.run(["C:\\Program Files\\WindowsApps\\Microsoft.WindowsCalculator_11.2405.2.0_x64__8wekyb3d8bbwe\\CalculatorApp.exe"])  # Try to run Notepad.exe from a specific path
        print("bien echo")
    except subprocess.CalledProcessError as e:  # Catch any CalledProcessError exceptions
        print(e.output)  # Print the error output

open_programs()