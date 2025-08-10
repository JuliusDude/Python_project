import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value,max_value)

while True:
    players = input("Enter the number of players(2-5): ")
    if players.isdigit():
        players = int(players)
        if 2<=players<=5:
            break
        else:
            print("Must be between 2 - 5 players.")
    else:
        print("Invalid, try again.")

max_score = 40
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    for player in range(players):
        current_score =0
        print(f"\nPlayer {player+1}'s turn has started!!")
        while True:
            should_roll = input("Would you like to roll (y)? ").lower()
            if should_roll !="y":
                break
            value = roll()

            if value == 1:
                print("You rolled a 1! You lost..")
                current_score = 0
                break
            else:
                current_score +=value
                print("You rolled ->",value)
            print("Your Score is:",current_score)
        player_score[player] = current_score
    
    top_score = max(player_score)
    print("\n\nWinners:")
    for i in range(len(player_score)):
        if player_score[i] == top_score:
            print(f"Player {i+1}")
    break



