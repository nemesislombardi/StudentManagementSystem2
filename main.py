from storage import *
from csvoperations import *
from students import *
from utlis import *

while True:
    print('''
    
----- Student Management System -----

1. Add Student
2. Remove Student
3. Update Student
4. Find Student by ID
5. Show All Students
6. Show CSV Data
7. Manuel Save Students to CSV / JSON
8. Exit & Save
    
    ''')

    choice = getInt("Enter Choice: ")

    if choice == 1:
        addStudent()
        input("\nPress ENTER to continue...")

    elif choice == 2:
        removeStudent()
        input("\nPress ENTER to continue...")

    elif choice == 3:
        updateStudent()
        input("\nPress ENTER to continue...")

    elif choice == 4:
        findStudent()
        input("\nPress ENTER to continue...")

    elif choice == 5:
        showAllStudent()
        input("\nPress ENTER to continue...")

    elif choice == 6:
        showCSV()
        print("Data successfully loaded from CSV.")
        input("\nPress ENTER to continue...")

    elif choice == 7:
        while True:
            print("""
            
            --- Manuel Save to CSV or JSON ---

            1. Save to CSV
            2. Save to JSON
            3. Save both
            4. Exit
            
            """)

            choice0 = getInt("Enter Choice: ")

            if choice0 == 1:
                saveCSV(students)
                print("Data successfuly saved to CSV")


            elif choice0 == 2:
                saveFile(students)
                print("Data successfuly saved to JSON")
                

            elif choice0 == 3:
                saveFile(students)
                saveCSV(students)
                print("Data successfuly saved to JSON and CSV")
                

            elif choice0 == 4:
                print("Closing..")
                break


            else:
                print("Something went wrong")

        input("\nPress ENTER to continue...")

    elif choice == 8:
        saveFile(students)
        saveCSV(students)
        print("Saving..")
        print("Closing..")
        break


    else:
        print("Something went wrong")
