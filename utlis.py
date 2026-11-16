def getInt(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Error, Pls enter int number")

def getFloat(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Error, Pls enter float number")

def getText(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Not be empty")