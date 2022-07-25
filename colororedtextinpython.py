# Print Colored Text with Python
# Traditionally, printing full-colour text to the terminal is accomplished by a series of escape characters on Linux or OS X systems. However, this will not work for Windows operating systems. Now let’s see how to print coloured text with Python using the Colorama module:
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE+Back.YELLOW+ "HI, My Name is Sharad Khare. " + Fore.YELLOW+ Back.BLUE + "I Am your Python Instructor")
print(Back.CYAN + "Hi, Again Myself Sharad Khare")
print(Fore.RED + Back.GREEN + "Hi, Sharad Khare is Your Programming instructor")