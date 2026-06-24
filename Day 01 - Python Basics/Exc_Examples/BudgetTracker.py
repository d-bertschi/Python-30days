income = float(input("Enter your monthly income: "))
rent = float(input("Enter your rent: "))
food = float(input("Enter your food expenses: "))
transport = float(input("Enter transport costs: "))
savings_goal = float(input("Enter your savings goal: "))

total_expenses = rent + food + transport
remaining_money = income - total_expenses
savings_progress = (remaining_money / savings_goal) * 100

print("\n--- Budget Summary ---")
print(f"Total expenses: {total_expenses:.2f} CHF")
print(f"Money left: {remaining_money:.2f} CHF")
print(f"Savings goal progress: {savings_progress:.1f}%")