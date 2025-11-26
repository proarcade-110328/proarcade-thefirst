import random
cpu = ['rock', 'paper', 'scissors']
computer = random.choice(cpu)
print("Let's play a Rock, Paper Scissors.")
usergame = input("Enter among rock, paper, scissors: ").lower()
if usergame not in cpu:
    print("Invalid input.")
    quit()
if (usergame == 'rock' and computer == 'scissors') or \
    (usergame == 'paper' and computer == 'rock') or \
    (usergame == 'scissors' and computer == 'paper'):
    print("YOU'RE A WINNER!")
elif usergame == computer:
    print("NOBODY WINS.")
else:
    print("YOU LOSE!")