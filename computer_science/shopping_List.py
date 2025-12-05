import os
from statistics import mean
from colorama import Fore, Back, Style, init


os.system('cls' if os.name == 'nt' else 'clear')

add_item_choice = "1"

shopping_list = []

def making_shopping_list():
    init(autoreset=True)
    print()
    adding = input(Fore.GREEN + "New thing: ")
    shopping_list.append(adding)
    print(f'"{adding}" added to your shopping list.')
    print()

def menu():

    print("choose 1,2,3 or q")
    print("------------------")
    print(f'{add_item_choice}: add item to list')
    print("2: remove item from list")
    print("3: view shopping list") 
    print("q: To quit")

def view_shopping_list():
    print()
    if shopping_list:
        print(Fore.YELLOW + "Your shopping list:")
        for item in shopping_list:
            print(Fore.BLUE + f"- {item}")
    else:
        print(Fore.YELLOW + "Your shopping list is empty.")
    print()

def remove_item_from_list():
    view_shopping_list()
    print()
    if shopping_list:
        item = input(Fore.RED + "Enter the thing you want to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(Fore.RED + f"-{item} remove from the list")
        else:
            print("item not in list")
    else:
        print(Fore.YELLOW + "Your shopping list is empty.")
    print()
    
def main():
    ans = "choice needed"
    while ans in [add_item_choice,"2","3","choice needed"]:
        menu()
        print("")
        ans = input("Your choice: ")    
        if ans == add_item_choice: making_shopping_list()
        elif ans == "q": print("bye bye")
        elif ans == '3': view_shopping_list()
        elif ans == '2': remove_item_from_list()
        else: 
            print("Not in the choosable thing")
            ans = "choice needed"
main()

