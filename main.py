import random
import time
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

    def codeCrack(self,userInput):
        self.resetVars()
        # print(userInput)
        userInput = [x for x in userInput]
        for x in userInput:
            self.currCode = x
            if self.currCode.isdigit():
                self.currCode = int(self.currCode)
                if self.currCode == self.unlockCodeList[self.unlockIndex]: #code for tracking unlocking
                    self.unlockIndex += 1
                    if self.unlockIndex == len(self.unlockCodeList):
                        if self.locked:
                            print("NOW UNLOCKED!")
                            self.unlockIndex = 0
                            self.locked = False
                        else:
                            # print("STILL UNLOCKED!")
                            self.unlockIndex = 0
                else:
                    self.unlockIndex = 0
                if self.currCode == self.lockCodeList[self.lockIndex]: #code for tracking locking
                    self.lockIndex += 1
                    if self.lockIndex == len(self.lockCodeList):
                        if self.locked:
                            # print("STILL LOCKED!")
                            self.lockIndex = 0
                        else:
                            print("NOW LOCKED!")
                            self.lockIndex = 0
                            self.locked = True
                else:
                    self.lockIndex = 0
        # print(codeList)



    def bufferedInput(self):
        self.resetVars() #resets all the variables to default state if the function were to be called again
        print("Start entering codes one digit at a time, pressing enter after each input. Enter Q to quit")
        while self.currCode != "Q": #check if user wishes to stop anytime
            self.currCode = input()
            # print(self.currCode)
            if self.currCode.isdigit(): #check if input is a digit, disregard otherwise
                self.currCode = int(self.currCode) #string input to int
                if self.currCode == self.unlockCodeList[self.unlockIndex]: #code for tracking unlocking
                    self.unlockIndex += 1
                    if self.unlockIndex == len(self.unlockCodeList):
                        if self.locked:
                            print("NOW UNLOCKED!")
                            self.unlockIndex = 0
                            self.locked = False
                        else:
                            # print("STILL UNLOCKED!")
                            self.unlockIndex = 0
                else:
                    self.unlockIndex = 0
                if self.currCode == self.lockCodeList[self.lockIndex]: #code for tracking locking
                    self.lockIndex += 1
                    if self.lockIndex == len(self.lockCodeList):
                        if self.locked:
                            # print("STILL LOCKED!")
                            self.lockIndex = 0
                        else:
                            print("NOW LOCKED!")
                            self.lockIndex = 0
                            self.locked = True
                else:
                    self.lockIndex = 0
        # print(codeList)


def main():
    fsm1 = Fsm()
    fsm1.bufferedInput()

    # needRepeat = True
    # while needRepeat:
    #     print("Would you like to buffer code input [1] or input code all as one string [2]?")
    #     answer = input()
    #     if int(answer) == 1:
    #         fsm1.bufferedInput()
    #         needRepeat = False
    #     if int(answer) == 2:
    #         print("Enter string of code 0-9")
    #         myInput = input()
    #         fsm1.inputString(myInput)
    #         needRepeat = False
    #     else:
    #         print("Would you like to buffer code input [1] or input code all as one string [2]?")



    timeList = []
    symbolList = []
    trialNumber = 0
    for x in range(10):
        trialNumber += 1
        fsm1.locked = True
        totalSymbols = 0
        codeGuess = []
        attempt = 1
        giveup = 25
        st = time.time()
        while fsm1.locked:
            while attempt <= giveup and fsm1.locked:

                # x = random.randint(0, 9999999999999999999999999) #25 random string everytime
                x = random.randint(0,9) #attempts
                # codeGuess = x #random string everytime
                codeGuess.append(x) #attempts
                totalSymbols += 1
                print('test iteration:', trialNumber, " : TRYING:", (codeGuess))
                fsm1.codeCrack(str(codeGuess))
                attempt += 1 #attempts
            codeGuess = []
            attempt = 1 #attempts
                # print("FAILED: ", (codeGuess[-6:]))
                # print("TRYING: ", (codeGuess))

        et = time.time()

        elapsed_time = et - st
        timeList.append(elapsed_time)
        symbolList.append(totalSymbols)
        print('Execution time:', elapsed_time, 'seconds')
        print("Total symbols generated: ", totalSymbols)


    print("Minimum time to compute code:", min(timeList), "seconds")
    print("Maximum time to compute code:", max(timeList), "seconds")
    print("Average time to compute code:", (sum(timeList)) / (len(timeList)), "seconds")

    print("Minimum number of symbols generated before unlock:", min(symbolList))
    print("Maximum number of symbols generated before unlock:", max(symbolList))
    print("Average number of symbols generated before unlock:", (sum(symbolList)) / (len(symbolList)))

if __name__ == "__main__":
    main()







