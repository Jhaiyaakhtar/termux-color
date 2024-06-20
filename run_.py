
import subprocess
import sys

# Function to install a package if it is not already installed
def install_package(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install required package
install_package('colorama')

# Import colorama after installation
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to print colored text
def print_colored(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

# Example usage with different colors
print_colored("This is red text", Fore.RED)
print_colored("This is green text", Fore.GREEN)
print_colored("This is yellow text", Fore.YELLOW)
print_colored("This is blue text", Fore.BLUE)
print_colored("This is magenta text", Fore.MAGENTA)
print_colored("This is cyan text", Fore.CYAN)
print_colored("This is white text", Fore.WHITE)
print_colored("This is black text", Fore.BLACK)
print_colored("This is light black text", Fore.LIGHTBLACK_EX)
print_colored("This is light red text", Fore.LIGHTRED_EX)
print_colored("This is light green text", Fore.LIGHTGREEN_EX)
print_colored("This is light yellow text", Fore.LIGHTYELLOW_EX)
print_colored("This is light blue text", Fore.LIGHTBLUE_EX)
print_colored("This is light magenta text", Fore.LIGHTMAGENTA_EX)
print_colored("This is light cyan text", Fore.LIGHTCYAN_EX)
print_colored("This is light white text", Fore.LIGHTWHITE_EX)