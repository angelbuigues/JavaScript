import subprocess  # Import the subprocess module to execute system commands

def googleXD(txt):
    url = "https://www.google.com/search?q=" + txt
    try:
        subprocess.run(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", url])  # Try to run Notepad.exe from a specific path
        
    
    except subprocess.CalledProcessError as e:  # Catch any CalledProcessError exceptions
        print(e.output)  # Print the error output


buscarTxt = input("Escribe que quieres buscar en google XD: ")
googleXD(buscarTxt)