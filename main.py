def inputString():
    currCode = None
    codeList = []
    locked = True
    unlockIndex = 0
    lockIndex = 0
    unlockCode = 850161
    lockCode = 850164

    unlockCodeList = [int(x) for x in str(unlockCode)]
    lockCodeList = [int(x) for x in str(lockCode)]

    print("Enter string of code 0-9")
    myInput = input()
    myInput = [x for x in myInput]
    for x in myInput:
        currCode = x
        if currCode.isdigit():
            currCode = int(currCode)
            codeList.append(currCode)
            if currCode == unlockCodeList[unlockIndex]: #code for tracking unlocking
                unlockIndex += 1
                if unlockIndex == len(unlockCodeList):
                    if locked:
                        print("NOW UNLOCKED!")
                        unlockIndex = 0
                        locked = False
                    else:
                        print("STILL UNLOCKED!")
                        unlockIndex = 0
            else:
                unlockIndex = 0
            if currCode == lockCodeList[lockIndex]: #code for tracking locking
                lockIndex += 1
                if lockIndex == len(lockCodeList):
                    if locked:
                        print("STILL LOCKED!")
                        lockIndex = 0
                    else:
                        print("NOW LOCKED!")
                        lockIndex = 0
                        locked = True
            else:
                lockIndex = 0
    # print(codeList)



def bufferedInput():
    currCode = None
    codeList = []
    locked = True
    unlockIndex = 0
    lockIndex = 0
    unlockCode = 850161
    lockCode = 850164

    unlockCodeList = [int(x) for x in str(unlockCode)]
    lockCodeList = [int(x) for x in str(lockCode)]

    print("Start buffering your code line by line. Enter Q to quit")
    while currCode != "Q":
        currCode = input()
        if currCode.isdigit():
            currCode = int(currCode)
            codeList.append(currCode)
            if currCode == unlockCodeList[unlockIndex]: #code for tracking unlocking
                unlockIndex += 1
                if unlockIndex == len(unlockCodeList):
                    if locked:
                        print("NOW UNLOCKED!")
                        unlockIndex = 0
                        locked = False
                    else:
                        print("STILL UNLOCKED!")
                        unlockIndex = 0
            else:
                unlockIndex = 0
            if currCode == lockCodeList[lockIndex]: #code for tracking locking
                lockIndex += 1
                if lockIndex == len(lockCodeList):
                    if locked:
                        print("STILL LOCKED!")
                        lockIndex = 0
                    else:
                        print("NOW LOCKED!")
                        lockIndex = 0
                        locked = True
            else:
                lockIndex = 0
    # print(codeList)

needRepeat = True
while needRepeat:
    print("Would you like to buffer code input [1] or input code all as one string [2]?")
    if int(input()) == 1:
        bufferedInput()
        needRepeat = False
    if int(input()) == 2:
        inputString()
        needRepeat = False
    else:
        print("Would you like to buffer code input [1] or input code all as one string [2]?")
