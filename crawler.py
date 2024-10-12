import subprocess
import os
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def print_title():
    # Create a star pattern for the title "CRAWLER"
    star_title = [
        "  *************   ***********          ****    **              ****              **   **              *************   *********** ",
        "  *************   ***********         **  **    **            ******            **    **              *************   *********** ",
        "  **              **       **        **    **    **          **    **          **     **              **              **       ** ",
        "  **              ** * * * **       **      **    **        **      **        **      **              *********       ** * * * ** ",
        "  **              ** **            ************    **      **        **      **       **              *********       ** **       ",
        "  **              **   **         **          **    **    **          **    **        **              **              **   **     ",
        "  *************   **     **      **            **    ******            ******         *************   *************   **     **   ",
        "  *************   **       **   **              **    ****              ****          *************   *************   **       ** ",
    ]
    
    # Print the star title
    for line in star_title:
        print(Fore.GREEN + line)
    
    print(Fore.CYAN + "Made by: Harsh Dev\n")

def main_menu():
    print(Fore.GREEN + "Please choose an option:")
    print(Fore.LIGHTBLUE_EX + "1. Run Simply")
    print(Fore.LIGHTBLUE_EX + "2. Run while saving the output")
    
    choice = input(Fore.LIGHTMAGENTA_EX + "Enter your choice (1/2): ")
    return choice

def run_scrapy(command):
    try:
        # Change to the specified directory
        os.chdir('stealth_crawler/spiders/')
        
        # Run the Scrapy command
        subprocess.run(command, shell=True)
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

if __name__ == "__main__":
    print_title()
    choice = main_menu()

    if choice == "1":
        print(Fore.GREEN + "Running Scrapy without saving output...")
        run_scrapy("scrapy crawl all_sites")
    elif choice == "2":
        print(Fore.GREEN + "Running Scrapy and saving output to output.json...")
        run_scrapy("scrapy crawl all_sites -o output.json")
    else:
        print(Fore.RED + "Invalid choice. Please select 1 or 2.")
