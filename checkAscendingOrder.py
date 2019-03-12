'''
Corrie Stewart
Program checks if user-entered numbers are in ascedning order
Date: 11/11/18
'''

def main():
    stringOfNumbers = input("Enter numbers seperated by blank space: ")
    stringSplit = stringOfNumbers.split()
    numbersInList = [eval(x) for x in stringSplit]

    if ordered(numbersInList):
        print("The numbers ARE in ascending order.")
    else:
        print("The numbers are NOT in ascending order.")


def ordered(numbersInList, ord = "ascending"):
    if ord == "ascending":
        for i in range(len(numbersInList) - 1):
            if numbersInList[i] >= numbersInList[i + 1]:
                return False

        return True
    else:
        for i in range(len(numbersInList) - 1):
            if numbersInList[i] <= numbersInList[i + 1]:
                return False

        return True


main()
