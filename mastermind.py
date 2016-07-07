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

def getRandomNumber():
  return [1,2,3,4]

def getUserInput():
  return [4,2,3,4]

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
    sys.exit()  # we should really pause and play a fanfare first but.... the clock is ticking! ;-)
  # else check number of correct digits and almost correct digits -> print progress message
  else:
    # check ... check ...
    correctDigit = 0           # right digit, right position
    possibleCorrectDigit = 0   # right digit, position unknown
    almostCorrectDigit = 0     # right digit, wrong position
    
    for digit in guess:
      if guess[digit] == answer[digit]:
        correctDigit = correctDigit + 1
      if digit in answer:
        possibleCorrectDigit = possibleCorrectDigit + 1
        
    almostCorrectDigit = possibleCorrectDigit - correctDigit 
    print "You have " + str(correctDigit) + "correct digits in the right place, and " + str(almostCorrectDigit) +  "correct digits in the wrong place. Keep trying." 
        

# ----- Main ----- #

if __name__ == "__main__":

  import sys

  # - generate random 4-digit number (as a 4-digit array/list)
  mysteryNumber = getRandomNumber()
  
  userGuess = []
  
  # - FOR(up to 10 times):
  for i in range(10):
    # - prompt user and get user input (as a 4-digit array/list)
    userGuess = getUserInput()
    
    # - validate user input
    if isValidInput(userGuess):
      # - evaluate user input
      evaluateGuess(userGuess, mysteryNumber)
  
  # - print failure message; EXIT
  print "Sorry, but you had your ten guesses. Better luck next time"
