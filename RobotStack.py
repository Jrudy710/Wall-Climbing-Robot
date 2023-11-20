# Project 1 - Dynamic Programming

# This is a program that will read from a file, with the file having an unknown number
# of lines, and on each line there will be a b (a given number of bots), n (the given number of stacks),
# and k (the max number of robots that can go in each stack) value. 

# This program will create a 2d array of n by b size, with the constraint of k.
# The program will then pass the values of b, n, k, and the 2d array and by using dynamic programming
# and memoization the program will determine the possible combinations based off the b, n, and k values.

# This value will then be formatted so that the answer is printed out in the format of: (b, n, k) = combinations

# Jason Rudinsky - U23254229

# Run the program in the terminal. Command line should be like so: "python RobotStack.py input.txt"

import sys                                                                    # Imports the ability to take commands from the command line

def robot(n, b, k, bcs):                                                      # Function Block
        
   # base cases
   if  b == 0 or n * k == b:                                                  # If statement to see if the number of robots is 0 or if the max number of possible bots/per stack * boxes is reached
      bcs[n][b] = 1                                                           # Sets the value of bcs at the index of n and b to 1
      
   elif n * k < b:                                                            # Checking to see if the number of bots exceeds the maximum capacity we can place
      bcs[n][b] = 0                                                           # Sets the number of possible combinations to 0  
   
   elif k == b:                                                               # Checks to see if the number of bots equals the max number of possible bots in a single stack
     bcs[n][b] = robot(n - 1, b, k, bcs) + robot(n, b - 1, k, bcs)            # Sets the value at the index of n and b
   
   # Memoization  
   if bcs[n][b] != -1:                                                        # Checks to see if the value is already filled
      return bcs[n][b]                                                        # Returns the value to the user

   else:                                                                      # Else statement for if the value of bcs[n][b] is unknown

      if bcs[n][b] == -1:                                                     # If statement to make sure the value has once again not been calculated
         bcs[n][b] = 0                                                        # Sets the value of bcs[n][b] to 0 to be correctly calculated by the for loop below
      
      for i in range(0, min(b + 1, k + 1)):                                   # For Loop that will loop for at most k times
         bcs[n][b] += robot(n - 1, b - i, k, bcs)                             # Adds to the value at the index of bcs[n][b]
      
      return bcs[n][b]                                                        # Returns the final value of bcs[n][b] to the user

def main():
   text_file = sys.argv[1]                                                    # Takes the value of the name of the file
   
   if ".txt" not in text_file:                                                # Checks to see if the '.txt' was included in the file name
      text_file += ".txt"                                                     # Adds the '.txt' to the file name
      
   fileInfo = []                                                              # Creates an empty list
   
   fileData = open(text_file, "r")                                            # Opens the file to read the data
   
   fileInfo = fileData.readlines()                                            # Reads the lines of info from the file
   
   for data in fileInfo:                                                      # For Loop for all the lines of data in the file
   
      betterData = data.split()                                               # Getting just the numeric values on a specific line
      
      b = int(betterData[0])                                                  # Sets the value of b
      n = int(betterData[1])                                                  # Sets the value of n
      k = int(betterData[2])                                                  # Sets the value of k
      
      bcs = [[-1 for i in range(b + 1)] for j in range(n + 1)]                # Creates an array of (n + 1) * (b + 1) size
      
      print(f"({b}, {n}, {k}) = {robot(n, b, k, bcs)}")                       # Prints out the info to the console
      
main()                                                                        # Calls the main function