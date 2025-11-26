import random
cpu = ['rock', 'paper', 'scissors']
print("Let's play a Rock, Paper Scissors.")
while True:
    usergame = input("Enter among rock, paper, scissors: ").lower()
    if usergame in cpu:
        print(f"You chose {usergame}.")
        computer = random.choice(cpu)
        if (usergame == 'rock' and computer == 'scissors') or \
        (usergame == 'paper' and computer == 'rock') or \
        (usergame == 'scissors' and computer == 'paper'):
            print("YOU'RE A WINNER!")
        elif usergame == computer:
            print("NOBODY WINS.")
        else:
            print("YOU LOSE!")
        again = input("Do you want to do another game? (y/n)").lower()
        if again != "y":
            print("This ends the game.")
            break
        else:
            print("Starting a new game.\n")
    else:
        print("Invalid input.")
        continue