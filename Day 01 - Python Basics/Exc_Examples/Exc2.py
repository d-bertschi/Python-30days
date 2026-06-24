# Hardcoded exchange rate
USD_TO_EUR = 0.92

usd = float(input("Enter amount in USD: "))

eur = usd * USD_TO_EUR

print(f"{usd} USD is equal to {eur:.2f} EUR")