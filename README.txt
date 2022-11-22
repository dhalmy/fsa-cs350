To run this program, since it is written in python and uses base libraries, all you need to do is have python installed and then open the file to run it.
When this program is run, it initiates a loop that takes in user input line by line. The user can quit the loop and start the cracking by entering 'Q'.
This user input is meant to be individual numbers, from 0-9, however any other characters will be disregarded silently.
The 'lock' begins in a locked state, where it requires the right sequence of numbers to unlock. The unlock code is 850161.
Once unlocked, a sequence of numbers is required to lock it. The lock code is 850164.

Once the user has quit the loop using 'Q', the program asks the user how many times to run the cracking the code method.
This code cracking simulates a locked lock with a digital numberpad that requires the intruder to input digits one by one.
In this simulation, the intruder doesn't know when the password is incorrect, but knows the password can't be over 25 digits long.
Every time the code reaches 25 digits in length, the intruder starts with new digits.
This code cracking method averaged around 36 seconds per iteration on my computer (over 100 runs) which is running Windows 10 with a ryzen 3800x, however results will vary.
Once the test cases are run, the code will output the following information:


Minimum time to compute code:
Maximum time to compute code:
Average time to compute code:
Minimum number of symbols generated before unlock:
Maximum number of symbols generated before unlock:
Average number of symbols generated before unlock: