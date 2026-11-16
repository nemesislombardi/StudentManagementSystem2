from storage import *
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
6. Manuel Save Students to CSV / JSON
7. Exit & Save
    
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