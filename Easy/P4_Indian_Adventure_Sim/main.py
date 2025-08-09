from time import sleep
import os

def clr():
    if os.name == 'nt':
        _ = os.system('cls')
    else:  
        _ = os.system('clear')


usr_name =input("Hi there, Please enter your name to start playing: ")
clr()
print(f"So {usr_name} Welcome to Indian Life Simulator!! ")
sleep(0.5)
print("Disclaimer: *All jokes*\n\n")
sleep(3.5)
clr()
print("There was child born in the great country of India!!!")
sleep(1)
clr()
choice = input("S")



