# 🧾 Dictionary → player profile
player = {
    "name": "Alex",
    "level": 5,
    "health": 100
}

# 📋 List → inventory (can change)
inventory = ["sword", "shield", "potion"]

# 📌 Tuple → fixed spawn location
spawn_point = (100, 250)

# ❄️ Frozenset → permanent abilities (cannot change)
abilities = frozenset(["run", "jump", "attack"])

# --- OPERATIONS ---

# Add items to inventory (list operation)
inventory.append("armor")
inventory.remove("potion")

# Update player stats (dictionary operations)
player["level"] += 1
player["health"] = 85

# Tuple access (read-only)
x, y = spawn_point

# Frozenset operations (returns new sets)
extra_abilities = abilities | frozenset(["defend"])
combat_abilities = abilities & frozenset(["attack", "block"])

# --- OUTPUT ---

print("🎮 Player Info:")
for key, value in player.items():
    print(key, value)

print("\n📋 Inventory:", inventory)
print(f"📌 Spawn point: {spawn_point}")

print("\n❄️ Abilities:", abilities)
print("➕ Extra abilities:", extra_abilities)
print("⚔️ Combat abilities:", combat_abilities)

print(f"\n📍 Player position starts at x={x}, y={y}")