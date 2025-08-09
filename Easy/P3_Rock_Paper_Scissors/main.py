import random

user = comp = 0
options =["r","p","s","q"]# To check for valid inputs
options_dict = {"r":"Rock","p":"Paper","s":"Scissors"}
while True:
    user_input = input("Enter Rock, Paper, Scissor or Quit (R,P,S,Q)? ").lower()
    if user_input not in options:
        continue
    if user_input == "q":# Printing the results when quiting 
        print(f"\n----RESULTS----\nUser Won : {user}\nMachine Won: {comp}\nGoodbye")
        quit()
    machine_input =random.choice(options[:3]) 
    print(f"I chose {options_dict.get(machine_input,"")} ")
    #Checking wining conditions
    if user_input =="r" and machine_input=="s":
        user+=1
        print("You won\n")
    elif user_input =="s" and machine_input=="p":
        user+=1
        print("You won\n")
    elif user_input =="p" and machine_input=="r":
        user+=1
        print("You won\n")
    elif user_input ==machine_input:
        print("Draw\n")
    else:
        comp+=1
        print("I won\n")



    