import csv

StudentCSV = "students.csv"
FieldsName = ["id", "name", "surname", "age"]

def saveCSV(students):
    try:
        with open(StudentCSV, "w", newline="", encoding="utf-8") as file:
            saveCSV = csv.DictWriter(file, fieldnames=FieldsName, delimiter="\t")
            saveCSV.writeheader()
            saveCSV.writerows(students)

    except Exception as e:
        print("Error Found: ", e)

def loadCSV():
    students = []

    try:
        with open(StudentCSV, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter="\t")

            for x in reader:
                students.append({
                    "id": int(x["id"]),
                    "name": str(x["name"]),
                    "surname": str(x["surname"]),
                    "age": int(x["age"])
                })

    except Exception as e:
        print("Error Found: ", e)

    return students


def showCSV():
    students = loadCSV()

    if not students:
        print("There is not a product here")
        return

    for x in students:
        print("-" * 30)
        print(f"ID: {x['id']}")
        print(f"Name: {x['name']}")
        print(f"Surname: {x['surname']}")
        print(f"Age: {x['age']}")
        print("-" * 30)
