weight = float(input("Enter package weight (kg): "))
region = input("Enter region (local / europe / international): ").lower()

# Base cost by weight
if weight < 1:
    cost = 5
elif weight <= 5:
    cost = 10
else:
    cost = 20

# Regional surcharge
if region == "local":
    surcharge = 0
elif region == "europe":
    surcharge = 5
elif region == "international":
    surcharge = 15
else:
    surcharge = 0
    print("Unknown region, default surcharge applied (0).")

total = cost + surcharge

print("\n--- Shipping Summary ---")
print(f"Base cost: {cost:.2f} CHF")
print(f"Surcharge: {surcharge:.2f} CHF")
print(f"Total cost: {total:.2f} CHF")