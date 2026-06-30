for fruit in ["apple", "banana", "cherry"]:
    if fruit == "banana":
        break # will not print cherry
    print(fruit)

print("Done with the loop - break")

for fruit in ["apple", "banana", "cherry"]:
    if fruit == "banana":
        continue
    print(fruit)

print("Done with the loop - continue")

'''
The else block runs only if the loop completes without encountering a break.
'''

numbers = [1, 3, 5, 7]

for n in numbers:
    if n == 4:
        print("Found 4")
        break
else:
    print("4 not found")

numbers_1 = [1, 4]

number_union = set(numbers) | set(numbers_1)

print(f"Union of {numbers} and {numbers_1}: {number_union}")

for n in number_union:
    if n == 4:
        print("Found 4")
        break
else:
    print("4 not found")

'''
    | Statement  | Purpose                                                               |
| ---------- | --------------------------------------------------------------------- |
| `break`    | Exit the loop immediately.                                            |
| `continue` | Skip the current iteration and continue with the next.                |
| `else`     | Execute after the loop finishes normally (i.e., no `break` occurred). |
'''

''' 
how ro add in which index? or how much loops?
'''

numbers = [1, 3, 4, 7]

for i, n in enumerate(numbers):
    if n == 4:
        print(f"Found {n} at index {i}")
        break

numbers = [1, 3, 4, 7]

count = 0

for n in numbers:
    count += 1
    if n == 4:
        print(f"Found after {count} iterations")
        break

'''

for n in numbers:
count += 1
if n == 4:
print(f"Found after {count} iterations")
break

IndentationError: expected an indented block after 'for' statement
'''