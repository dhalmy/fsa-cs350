import random
import time

class Fsm:
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
        self.resetVars() #resets all the variables to default state if the function were to be called again
        userInput = [x for x in userInput]
        for x in userInput:
            self.currCode = x
            if self.currCode.isdigit(): #check if input is a digit, disregard otherwise
                self.currCode = int(self.currCode)
                if self.currCode == self.unlockCodeList[self.unlockIndex]: #code for tracking the locking sequence from inputs
                    self.unlockIndex += 1
                    if self.unlockIndex == len(self.unlockCodeList): #if the unlock code matches, unlock
                        if self.locked:
                            print("NOW UNLOCKED!")
                            self.unlockIndex = 0
                            self.locked = False
                        else:
                            # print("STILL UNLOCKED!")
                            self.unlockIndex = 0
                else:
                    self.unlockIndex = 0
                if self.currCode == self.lockCodeList[self.lockIndex]: #code for tracking the unlocking sequence from inputs
                    self.lockIndex += 1
                    if self.lockIndex == len(self.lockCodeList): #if the lock code matches, lock
                        if self.locked:
                            # print("STILL LOCKED!")
                            self.lockIndex = 0
                        else:
                            print("NOW LOCKED!")
                            self.lockIndex = 0
                            self.locked = True
                else:
                    self.lockIndex = 0



    def bufferedInput(self):
        self.resetVars() #resets all the variables to default state if the function were to be called again
        print("Start entering codes one digit at a time, pressing enter after each input. Enter Q to quit")
        while self.currCode != "Q": #check if user wishes to stop anytime
            self.currCode = input()
            # print(self.currCode)
            if self.currCode.isdigit(): #check if input is a digit, disregard otherwise
                self.currCode = int(self.currCode) #string input to int
                if self.currCode == self.unlockCodeList[self.unlockIndex]: #code for tracking the unlock sequence from inputs
                    self.unlockIndex += 1
                    if self.unlockIndex == len(self.unlockCodeList): #if the unlock code matches, unlock
                        if self.locked:
                            print("NOW UNLOCKED!")
                            self.unlockIndex = 0
                            self.locked = False
                        else:
                            # print("STILL UNLOCKED!")
                            self.unlockIndex = 0
                else:
                    self.unlockIndex = 0
                if self.currCode == self.lockCodeList[self.lockIndex]: #code for tracking the locking sequence from inputs
                    self.lockIndex += 1
                    if self.lockIndex == len(self.lockCodeList): #if the lock code matches, lock
                        if self.locked:
                            # print("STILL LOCKED!")
                            self.lockIndex = 0
                        else:
                            print("NOW LOCKED!")
                            self.lockIndex = 0
                            self.locked = True
                else:
                    self.lockIndex = 0

    def crack(self,numTests):
        timeList = []
        symbolList = []
        trialNumber = 0
        for x in range(numTests):
            trialNumber += 1
            self.locked = True
            totalSymbols = 0
            codeGuess = []
            attempt = 1
            giveup = 25
            st = time.time()
            while self.locked:
                while attempt <= giveup and self.locked:
                    x = random.randint(0, 9)  # attempts
                    codeGuess.append(x)  # attempts
                    totalSymbols += 1
                    print('test iteration:', trialNumber, " : TRYING:", (codeGuess))
                    self.codeCrack(str(codeGuess))
                    attempt += 1  # attempts
                codeGuess = []
                attempt = 1  # attempts

            et = time.time()

            elapsed_time = et - st
            timeList.append(elapsed_time)
            symbolList.append(totalSymbols)
            print('Execution time:', elapsed_time, 'seconds')
            print("Total symbols generated: ", totalSymbols)

        print()
        print()
        print("Minimum time to compute code:", min(timeList), "seconds")
        print("Maximum time to compute code:", max(timeList), "seconds")
        print("Average time to compute code:", (sum(timeList)) / (len(timeList)), "seconds")

        print("Minimum number of symbols generated before unlock:", min(symbolList))
        print("Maximum number of symbols generated before unlock:", max(symbolList))
        print("Average number of symbols generated before unlock:", (sum(symbolList)) / (len(symbolList)))




def main():
    fsm1 = Fsm()
    fsm1.bufferedInput()
    print("How many times would you like to run the code cracking algorithm? Each solve takes 36 seconds on average")
    numTimes = input()
    fsm1.crack(int(numTimes))



if __name__ == "__main__":
    main()
    print()
    print("enter anything to quit")
    input()