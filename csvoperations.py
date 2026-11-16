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
        print("Some error occured:", e)
        