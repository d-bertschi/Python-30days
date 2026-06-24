'''

Here’s a single combined mini-project that uses everything you’ve learned so far:

variables
input
int / float
lists, tuples, sets, frozensets
dictionaries (nested)
loops (for / while)
conditionals (if / elif / else)
comparison + logical operators
string formatting (f"", :.2f)
basic operations + mini system logic

'''

from getpass import getpass

# ❄️ Frozenset → fixed permissions
permissions = frozenset(["play", "shop", "view_stats"])

# 📌 Tuple → fixed spawn location
spawn_point = (100, 250)

# 🔢 Set → unique items collected
collected_items = set()

# 🧾 Dictionary → user database (nested dict)
users = {}

# =========================
# 🧾 REGISTRATION
# =========================
print("=== REGISTER ===")

username = input("Create username: ")
password = getpass("Create password: ")

users[username] = {
    "password": password,
    "level": 1,
    "inventory": ["potion", "sword"]
}

print("\nAccount created!\n")

# =========================
# 🔐 LOGIN (3 attempts)
# =========================
attempts = 3
logged_in = False

while attempts > 0:
    print("=== LOGIN ===")

    user = input("Username: ")
    pw = getpass("Password: ")

    if user in users and users[user]["password"] == pw:
        print("Login successful!\n")
        logged_in = True
        break
    else:
        attempts -= 1
        print(f"Wrong credentials. Attempts left: {attempts}")

if not logged_in:
    print("Account locked.")
    exit()

# =========================
# 🎮 GAME + SHOP SYSTEM
# =========================

player = users[user]

print("Spawn point:", spawn_point)
print("Permissions:", permissions)

# 📋 List operations (inventory)
player["inventory"].append("shield")

# 🔁 Loop menu
while True:
    print("\n=== MENU ===")
    print("1. View Inventory")
    print("2. Collect Item")
    print("3. Shipping Calculator")
    print("4. Exit")

    choice = input("Choose: ")

    # -------------------------
    # 📦 Inventory (list)
    # -------------------------
    if choice == "1":
        print("\nInventory:")
        for item in player["inventory"]:
            print("-", item)

    # -------------------------
    # 🎒 Collect items (set)
    # -------------------------
    elif choice == "2":
        item = input("Enter item to collect: ")
        collected_items.add(item)
        print("Collected items:", collected_items)

    # -------------------------
    # 📦 Shipping calculator
    # -------------------------
    elif choice == "3":
        weight = float(input("Enter package weight (kg): "))
        region = input("Region (local/europe/international): ").lower()

        # weight tiers
        if weight < 1:
            cost = 5
        elif weight <= 5:
            cost = 10
        else:
            cost = 20

        # regional surcharge
        if region == "local":
            surcharge = 0
        elif region == "europe":
            surcharge = 5
        elif region == "international":
            surcharge = 15
        else:
            surcharge = 0
            print("Unknown region.")

        total = cost + surcharge

        print(f"\nShipping cost: {total:.2f} CHF")

    # -------------------------
    # 🚪 Exit
    # -------------------------
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")