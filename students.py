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

def removeStudent():

    if not students:
        print("Students empty try add students")
        return
    
    try:
        getID = getInt("Enter ID: ")
        found = False

        for x in students:
            if x["id"] == getID:
                found = True
                students.remove(x)

                print(f"{x['name']} Named student successfuly removed.")
                return

        if not found:
            print("Student Not Found..")

    except Exception as e:
        print("Error found; ", e)

def updateStudent():

    if not students:
        print("Students empty try add students")
        return

    try:
        getID = getInt("Enter Student ID: ")
        found = False

        for x in students:
            if x["id"] == getID:
                found = True
            
                while True:
                    print("""
                        ----- UPDATE STUDENTS -----

                        1. Update Name
                        2. Update Surname
                        3. Update Age
                        4. Exit & Save
                    """)

                    choice = getInt("Enter Choice: ")

                    if choice == 1:
                        newName = getText("Enter New Name; ")
                        if newName == x["name"]:
                            print("New name same with old name try again.")
                            continue
                        else:
                            x["name"] = newName

                    elif choice == 2:
                        newSurname = getText("Enter New Surname; ")
                        if newSurname == x["surname"]:
                            print("New surname same with old surname try again.")
                            continue
                        else:
                            x["surname"] = newSurname

                    elif choice == 3:
                        newAge = getInt("Enter New Age; ")
                        if newAge == x["age"]:
                            print("New age same with old age try again.")
                            continue
                        elif newAge < 16:
                            print("Age not compitable atleast must be 16 try again.")
                            continue
                        else:
                            x["age"] = newAge

                    elif choice == 4:
                        print("Closing & Saving...")
                        return

                    else:
                        print("Invalid choice! Try again..")

        if not found:
            print("Student Not Found..")
                           

    except Exception as e:
        print("Error Found; ", e)              

def findStudent():

    if not students:
        print("Students empty try add students")
        return

    try:
        getID = getInt("Enter ID: ")
        found = False


        for x in students:
            if x["id"] == getID:
                found = True

                print("-" * 30)
                print(f"ID: {x['id']}")
                print(f"Name: {x['name']}")
                print(f"Surname: {x['surname']}")
                print(f"Age: {x['age']}")
                print("-" * 30)
                break
        
        if not found:
            print("Student Not Found..")

    except Exception as e:
        print("Error found; ", e)

def showAllStudent():

    if not students:
        print("Students empty try add students")
        return

    for x in students:
        print("-" * 30)

        print(f"ID: {x['id']}")
        print(f"Name: {x['name']}")
        print(f"Surname: {x['surname']}")
        print(f"Age: {x['age']}")

        print("-" * 30)

def filterByAge():

    if not students:
        print("Students empty try add students")
        return
    try:
        while True:
            print("""

            ----- Filter by Age -----
            
            1. Ascending
            2. Decreasing
            3. Exit
            
            
            """)

            choice = getInt("Enter Choice; ")

            if choice == 1:
                students.sort(key=lambda student: student["age"])

                print("Filtered by Ascending.")

            elif choice == 2:
                students.sort(key=lambda student: student["age"], reverse=True)

                print("Filtered by Decreasing.")

            elif choice == 3:
                print("Closing..")
                return

            else:
                print("Invalid choice! Try again..")
    except Exception as e:
        print("Error Found;", e)

    

        