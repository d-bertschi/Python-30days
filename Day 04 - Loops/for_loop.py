# Basic for loop
for i in range(5):
    print(i)

# List iteration
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I love {fruit}s")

fruits.append("orange")
print(fruits)

fruits[1] = "mango"
print(fruits)

fruits.insert(1, "orange")
print(fruits)

fruits.extend(["grape", "kiwi"])
print(fruits)

for fruit in fruits:
    print(f"I love {fruit}s")

'''
fruits.append("orange")
print(fruits)

fruits[1] = "mango"
print(fruits)

fruits.insert(1, "orange")
print(fruits)

fruits.extend(["grape", "kiwi"])
print(fruits)

fruits1 = ["apple", "banana", "cherry"]
fruits2 = ["banana", "orange", "cherry", "kiwi"]

union = set(fruits1) | set(fruits2)
print(union)

union = set(fruits1).union(fruits2)

intersection = set(fruits1) & set(fruits2)
print(intersection)

intersection = set(fruits1).intersection(fruits2)
print(intersection)
'''

fruits1 = ["apple", "banana", "cherry"]
fruits2 = ["banana", "orange", "cherry", "kiwi"]

union = set(fruits1) | set(fruits2)
print(union)

union = set(fruits1).union(fruits2)
print(union)

intersection = set(fruits1) & set(fruits2)
print(intersection)

intersection = set(fruits1).intersection(fruits2)
print(intersection)