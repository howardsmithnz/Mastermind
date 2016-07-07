#! /usr/bin/python2.7

# a Mastermind-style game
# Author: Howard Smith

# Pseudocode: - generate random 4-digit number (as a 4-digit array/list)
#             - FOR(up to 10 times):
#               - prompt user and get user input (as a 4-digit array/list)
#               - validate user input
#               - evaluate user input
#                  - IF success:
#                    - print success message; EXIT
#                  - ELSE:
#                    - print progress message
#             - print failure message; EXIT

# ----- functions ----- #

def printWelcome():
  print ''
  print "Welcome to Mastermind. Enter a list of 4 digits:  (e.g. [1,2,3,4])"
  print '================================================'
  print''

def getRandomNumber():
  return [1,2,3,4]

def getUserInput():
  userInput = input("Prompt> ")
  #print "Type of input is: " + str(type(userInput))
  return userInput

def isValidInput(input):
  # do some validation here
  # IF input is invalid, print message and return False 
  if type(input) != list: # we could test for many other kinds of invalid data (e.g. len(input)!= 4) but this is representative! :-)
    print "Ouch! Not a list! You just used up one guess."
    return False
  # ELSE return True
  else:
    return True
  
def evaluateGuess(guess, answer):
  # check if guess is correct -> print success message and exit
  if guess == answer:
    print "Well done. That's right!"
    print "The right answer WAS " + str(answer) + "!"
    sys.exit()
  # else check number of correct digits and almost correct digits -> print progress message
  else:
    # check ... check ...
    correctDigit = 0           # right digit, right position
    possibleCorrectDigit = 0   # right digit, position unknown
    almostCorrectDigit = 0     # right digit, wrong position
    
    # traverse through the guess list and compare to each corresponding digit in the answer list
    #for digit in guess:
    for i in range(len(guess)):
      #print "i is : " + str(i)
      #print "Digit is : "+ str(guess[i])
      if guess[i] == answer[i]:
        correctDigit = correctDigit + 1
      if guess[i] in answer:
        possibleCorrectDigit = possibleCorrectDigit + 1
        
    almostCorrectDigit = possibleCorrectDigit - correctDigit 
    print "You have " + str(correctDigit) + " correct digits in the right place, and " + str(almostCorrectDigit) +  " correct digits in the wrong place. Keep trying." 
        

# ----- Main ----- #

if __name__ == "__main__":

  import sys

  # - generate random 4-digit number (as a 4-digit array/list)
  mysteryNumber = getRandomNumber()
  
  userGuess = []
  limit = 1
  seq = range(1)

  printWelcome()
  
  # - FOR(up to limit):
  for i in seq:
    # - prompt user and get user input (as a 4-digit array/list)
    userGuess = getUserInput()
    
    # - validate user input
    if isValidInput(userGuess):
      # - evaluate user input
      evaluateGuess(userGuess, mysteryNumber)
  
  # - print failure message; EXIT
  print "Sorry, but you had your " + str(limit) + " guesses. Better luck next time"
  print "The answer was " + str(mysteryNumber) + "."
