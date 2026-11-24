"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""


def read_menu():
    # Reads menu information from the file
    menus = {}

    try:
        with open("menu_config.txt", "r") as file:
            for line in file:
                parts_of_line = line.strip().split(":")

                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()

                menus[category] = detail

        return menus

    except FileNotFoundError:
        print("Please make sure menu_config.txt exists.")
        return {}


def split_into_variables(menu_items):
    # Breaks the dictionary into variables
    tacos = menu_items.get("TACOS")
    toppings = menu_items.get("TOPPINGS")
    drinks = menu_items.get("DRINKS")
    desserts = menu_items.get("DESSERTS")

    return tacos, toppings, drinks, desserts


def print_menu(tacos, toppings, drinks, desserts):
    # Displays the menu

    print("TACOS")
    for item in tacos.split(","):
        print(f"\t{item.strip()}")

    print("\nTOPPINGS")
    for item in toppings.split(","):
        print(f"\t{item.strip()}")

    print("\nDRINKS")
    for item in drinks.split(","):
        print(f"\t{item.strip()}")

    print("\nDESSERTS")
    for item in desserts.split(","):
        print(f"\t{item.strip()}")


def main():
    # Controls the program flow
    menu_items = read_menu()

    tacos, toppings, drinks, desserts = split_into_variables(menu_items)

    print_menu(tacos, toppings, drinks, desserts)


main()