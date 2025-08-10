#Guess the number game
import random

print("Welcome to Guess the number :) ")
while (True):
    top_range=input("Enter the top range(eg. 6): ")
    if top_range.isdigit():
        if int(top_range)<=0:
            print("Enter a number lager than 0: ")
        else:
            mystery_number = random.randint(0,int(top_range)) #To set the mystery number
            break
    else:
        print("Enter a number!!!")

print("You have 5 Guesses to guess the number...\n")
count = 0
while (count<5): #Setting up the game for 5 tries 
    try:
        count+=1
        guess = int(input("Enter your Guess:"))
    except:
        print("you have entered an invalid value  :( )")
        print()
        continue
    if guess == mystery_number:
        print(f"You have got it!!!\nscore:{-count+6}/5\n")
        quit() #exiting the code when user gets the answer
    elif guess > mystery_number:
        print("The mystery number is 'Lower'\n")
    else:
        print("The mystery number is 'Higher'\n")
print(f"It was {mystery_number}\nBetter luck next time...")

