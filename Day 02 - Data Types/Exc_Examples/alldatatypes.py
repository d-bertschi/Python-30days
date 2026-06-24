# Dictionary → student profile (key-value data)
student = {
    "name": "Alex",
    "age": 20,
    "id": 101
}

# List → courses student is currently taking (can change)
courses = ["Math", "Physics", "History"]

# Tuple → fixed data (student location)
location = (47.3769, 8.5417)  # Zurich coordinates

# Set → track unique grades (no duplicates)
grades = {"A", "B", "A", "C"}

# Frozenset → fixed allowed actions (cannot be changed)
permissions = frozenset(["view_grades", "enroll", "view_schedule"])

# --- Operations ---
courses.append("Computer Science")   # modify list
grades.add("B")                      # set ignores duplicates

# --- Output ---
print("--- Student Profile ---")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"ID: {student['id']}")

print("\nCourses:", courses)
print("Location:", location)
print("Unique Grades:", grades)
print("Permissions:", permissions)