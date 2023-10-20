students = {"Hermione": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin",
            }
            
print(students["Hermione"])

for _ in students:
    print(_, students[_], sep=", ")
