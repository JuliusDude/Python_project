#Formula 1 Quiz

import random
print("----Welcome to Formula 1 quiz----")
playing = input("Do you want to play(yes/no)? ")
if playing != "yes":
    quit()
print("Lets Start!!!")
points = 0

#List containing 1)Question 2)Options 3)Answers
f1_quiz_mcq = [
    [
        "Who holds the record for the most Formula 1 World Drivers’ Championships?",
        [ "A) Lewis Hamilton", "B) Juan Manuel Fangio", "C) Sebastian Vettel"],
        "A"
    ],
    [
        "In F1, the term 'DRS' stands for:",
        ["A) Dynamic Racing System", "B) Drag Reduction System", "C) Downforce Reduction Setup", "D) Driver Reaction Speed"],
        "B"
    ],
    [
        "Monaco Grand Prix is the shortest race in the F1 calendar by distance. (True/False)",
        ["A)True", "B)False"],
        "A)"
    ],
    [
        "Which team introduced the 'double diffuser' in the 2009 season?",
        ["A) Ferrari", "B) Red Bull Racing", "C) Brawn GP", "D) McLaren"],
        "C"
    ],
    [
        "The pit lane speed limit during a race is usually ______ km/h.",
        ["A) 60", "B) 80", "C) 100", "D) 120"],
        "B"
    ],
    [
        "What is the maximum number of points a driver can score in a single race weekend under the current rules (2025)?",
        ["A) 25", "B) 26", "C) 27", "D) 28"],
        "C"
    ],
    [
        "Which tyre compound is the fastest but wears out the quickest?",
        ["A) Hard", "B) Medium", "C) Soft", "D) Super Soft"],
        "C"
    ],
    [
        "Who won the first ever Formula 1 World Championship race in 1950?",
        ["A) Giuseppe Farina", "B) Juan Manuel Fangio", "C) Stirling Moss", "D) Alberto Ascari"],
        "A"
    ],
    [
        "In wet races, F1 cars use slick tyres for maximum grip. (True/False)",
        ["A)True", "B)False"],
        "B"
    ],
    [
        "Which team did Fernando Alonso drive for when he won his first World Championship?",
        ["A) Ferrari", "B) McLaren", "C) Renault", "D) Minardi"],
        "C"
    ]
]

#The Quiz loop
while playing=="yes":
    random.shuffle(x=f1_quiz_mcq)
    for i in f1_quiz_mcq:
        print(i[0])
        for j in i[1]:
            print(j)
        answer = input("Enter your Answer(A,B,C,D): ").strip()
        if answer.upper() == i[2]:
            points+=1
            print("You got the Right Answer!!!")
        else:
            print(f"Wrong Answer, The correct answer:{i[2]}")
    print(f"You Got {points} out of 10!!!!")
    playing = input("Do you want to play again(yes/no)? ").lower()


