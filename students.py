from utlis import *
from storage import *

students = loadFile()

studentsID = max((x["id"] for x in students), default=0) + 1

def addStudent():
    try:
        global studentsID
        
        name = getText("Enter Name; ")
        surname = getText("Enter Surname; ")
        age = getInt("Enter Age; ")

        if age < 16:
            raise ValueError("Age not compitable")

        student = {
            "id": studentsID,
            "name": name,
            "surname": surname,
            "age": age
        }

        students.append(student)
        studentsID += 1

        print("Student successfuly added.")
        print(f"Student ID:", student["id"])

    except Exception as e:
        print("Error Found; ", e)