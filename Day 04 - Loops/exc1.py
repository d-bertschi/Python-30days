'''
import random

# Generate a secret number between 1 and 20
secret_number = random.randint(1, 20)

# print(secret_number)  # Uncomment this line for testing purposes

attempts = 0

while attempts < 5:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1

    if guess == secret_number:
        print(f"Good job! You guessed the number in {attempts} attempt(s).")
        break
    else:
        print("Incorrect. Try again.")

else:
    print(f"Game over! The secret number was {secret_number}.")
'''

import random
import tkinter as tk
from tkinter import simpledialog, messagebox

# Hide the main window
root = tk.Tk()
root.withdraw()

secret_number = random.randint(1, 10)

attempts = 0

while attempts < 5:
    guess = simpledialog.askinteger(
        "Guessing Game",
        "Guess a number between 1 and 10:"
    )

    attempts += 1

    if guess == secret_number:
        messagebox.showinfo(
            "Congratulations!",
            f"You guessed the number in {attempts} attempt(s)."
        )
        break
    else:
        messagebox.showinfo("Try Again", "Incorrect guess!")

else:
    messagebox.showinfo(
        "Game Over",
        f"The secret number was {secret_number}."
    )