import random
class Fsm:
    # def __init__(self, currCode, codeList, locked, unlockIndex, lockIndex, unlockCode, lockCode, unlockCodeList, lockCodeList):
    #     self.currCode = None
    #     self.codeList = []
    #     self.locked = True
    #     self.unlockIndex = 0
    #     self.lockIndex = 0
    #     self.unlockCode = 850161
    #     self.lockCode = 850164
    #     self.unlockCodeList = [int(x) for x in str(unlockCode)]
    #     self.lockCodeList = [int(x) for x in str(lockCode)]

    currCode = None
    codeList = []
    locked = True

    unlockIndex = 0
    lockIndex = 0

    unlockCode = 850161
    lockCode = 850164

    unlockCodeList = [int(x) for x in str(unlockCode)]
    lockCodeList = [int(x) for x in str(lockCode)]



    def resetVars(self):
        self.currCode = None
        self.codeList = []
        self.locked = True
        self.unlockIndex = 0
        self.lockIndex = 0

    def inputString(self,userInput):
        self.resetVars()
        # print(userInput)
        userInput = [x for x in userInput]
        for x in userInput:
            self.currCode = x
            if self.currCode.isdigit():
                self.currCode = int(self.currCode)
                # self.codeList.append(self.currCode)
                if self.currCode == self.unlockCodeList[self.unlockIndex]: #code for tracking unlocking
                    self.unlockIndex += 1
                    if self.unlockIndex == len(self.unlockCodeList):
                        if self.locked:
                            print("NOW UNLOCKED!")
                            self.unlockIndex = 0
                            self.locked = False
                        else:
                            print("STILL UNLOCKED!")
                            self.unlockIndex = 0
                else:
                    self.unlockIndex = 0
                if self.currCode == self.lockCodeList[self.lockIndex]: #code for tracking locking
                    self.lockIndex += 1
                    if self.lockIndex == len(self.lockCodeList):
                        if self.locked:
                            print("STILL LOCKED!")
                            self.lockIndex = 0
                        else:
                            print("NOW LOCKED!")
                            self.lockIndex = 0
                            self.locked = True
                else:
                    self.lockIndex = 0
        # print(codeList)



    def bufferedInput():
        resetVars()
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


def main():
    fsm1 = Fsm()
    # needRepeat = True
    # while needRepeat:
    #     print("Would you like to buffer code input [1] or input code all as one string [2]?")
    #     answer = input()
    #     if int(answer) == 1:
    #         bufferedInput()
    #         needRepeat = False
    #     if int(answer) == 2:
    #         print("Enter string of code 0-9")
    #         myInput = input()
    #         fsm1.inputString(myInput)
    #         needRepeat = False
    #     else:
    #         print("Would you like to buffer code input [1] or input code all as one string [2]?")

    codeGuess = []
    while fsm1.locked:
        x = random.randint(0, 9)
        codeGuess.append(x)
        fsm1.inputString(str(codeGuess))
        testList = ["FAILED"]
        # print(testList + (codeGuess[-6:]))
        print(testList + (codeGuess))


if __name__ == "__main__":
    main()







