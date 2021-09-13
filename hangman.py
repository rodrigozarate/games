#!/usr/bin/python3
#INIT	
import random
import sys
from os import system, name
from time import sleep

print("Welcome to Hangman.")
print("A game created by:")
print("Laura Callejas")
print("Oscar")
print("Paola")
print("Juan Camilo")
print("Stefania")
print("Rodrigo Zárate")

sleep(2)

#PARAMS
def main():
  # number of attempts by player
  global count
  # the words being guessed
  global showguessed
  # the chosen word
  global word
  # unmodified word
  global compareword
  # array of used letters
  global guessed
  # the lenght of the word
  global length

  dictionary = ["alfa","beta","gamma","delta","epsilon","zeta","omega","sigma"]
  word = random.choice(dictionary)
  compareword = word
  length = len(word)
  count = 0
  showguessed = "_" * length
  guessed = []
  clear()

# 2.0 LOOP
def play_again():
    global count
    global word
    print("Do you want to play again?")
    response = input("y for yes or n for no\n")
    if response == 'y':
        main()
        hangman()
    else:
        exit()

#PRINT
def print_hangman():
    global count

    if count == 1:
      print(" ")
      print(" ")
      print(" ")
      print(" ")
      print(" ")
      print(" ")
      print("======")
      print("You have 6 attempts left")

    if count == 2:
      print(" ")
      print("     |")
      print("     |")
      print("     |")
      print("     |")
      print("     |")
      print("======")
      print("You have 5 attempts left")

    if count == 3:
      print(" +---+")
      print("     |")
      print("     |")
      print("     |")
      print("     |")
      print("     |")
      print("======")
      print("You have 4 attempts left")

    if count == 4:
      print(" +---+")
      print(" |   |")
      print("     |")
      print("     |")
      print("     |")
      print("     |")
      print("======")
      print("You have 3 attempts left")

    if count == 5:
      print(" +---+")
      print(" |   |")
      print(" O   |")
      print("     |")
      print("     |")
      print("     |")
      print("======")
      print("You have 2 attempts left")

    if count == 6:
      print(" +---+")
      print(" |   |")
      print(" O   |")
      print("/|\  |")
      print("     |")
      print("     |")
      print("     =")
      print("You have 1 attempts left")

    if count == 7:
      print(" +---+")
      print(" |   |")
      print(" O   |")
      print("/|\  |")
      print("/ \  |")
      print("     |")
      print("======")
      print("You have 0 attempts left")
      print("Sorry, you lose")
      play_again()

#CLEAR SCREEN
def clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

#GAME
def hangman():
  global count
  global showguessed
  global word
  global guessed
  limit = 7
  # validate right input
  guess = input("The word consist of "+showguessed+" letters, enter your letter to guess\n")

  # just press enter error
  if len(guess.strip()) == 0:
    clear()
    print("Please write a single letter")
    hangman()
  
  elif len(guess.strip()) > 1:
    clear()
    # use a complete word
    print("Guessing the whole word")
    print(guess)
    if guess == compareword:
      print("------------------------------")
      print("| You win using this letters |")
      print("------------------------------")
      print(guessed)
      print("Your word was: " + compareword)
      play_again()
    else:
      count += 1
      print_hangman()
      print("Wrong guess")
      print("You have wasted 1 attempt")
      print(guessed)

  # the letter is found
  elif guess in word:
    clear()
    print_hangman()
    guessed.extend([guess])
    index = word.find(guess)
    word = word[:index] + "_" + word [index + 1:]
    showguessed = showguessed[:index] + guess + showguessed [index + 1:]
    print("You've found the first ocurrence of " + guess
         + " in " + showguessed +"\n")
    print("")

  # used letter
  elif guess in guessed:
    clear()
    print_hangman()
    print("You already found all - " +guess+ " - letters")
    print("Give another try")

  # wrong guess print hangman
  else:
    clear()
    count += 1
    print_hangman()


  # end program 
  if word == "_" * length:
    clear()
    print("-----------")
    print("| You win |")
    print("-----------")
    play_again()

  #go to the program again
  elif count != limit:
    hangman()


main()

hangman()
