import json

studentsJSON = "students.json"


def saveFile(file):
    try:
        with open(studentsJSON, "w", encoding="utf-8")as f:
            json.dump(file, f, indent=4)

            print("Data successfuly saved.\n")


    except Exception as e:
        print("Error Found; ", e)

def loadFile():
    try:
        with open(studentsJSON, "r", encoding="utf-8")as f:
            return json.load(f)
        
    except Exception as e:
        print("Error Found; ", e)

    return []