#codeorbit-internship
#task 3- guessing game

import random

#this shall generate a random number between 1-100
secrect_number=random.randint(1,100)

#it shall keep a track of the number of attemps made to guess the secrect number
attempts=0

#it shall keep loopiing until the user guesses the secrect number
while True:
    try:
        guess=int(input("guess a number between 1-100: ")) #takes the input from the user

        if guess<1 or guess>100: #if the user geusses a invalid number
            print("please geuss a numebr between 1-100")
            attempts+=1
            continue

        elif guess<secrect_number: #if the user geusses a number less than the secrect number
            print("too low! try again")
            attempts+=1

        elif guess>secrect_number: #if the user geusses a number greater than the secrect number
            print("too high! try again")
            attempts+=1

        else: #if the user geusses the secrect number
            attempts+=1
            print(f"congratulations! you guessed the secrect number {secrect_number} in {attempts} attempts.")
            break

    except ValueError: #handeles a invalid input
        print("Invalid input. Please enter a valid number.")
        attempts+=1