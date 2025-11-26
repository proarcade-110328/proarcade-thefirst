# This starts the GUI version.
import random
cpu = ['rock', 'paper', 'scissors']
def game(userchoice):
    cpuchoice = random.choice(cpu)
    if userchoice == cpuchoice:
        result_label.config(text= "TIE!")
    elif (userchoice == 'rock' and cpuchoice == 'scissors') or \
        (userchoice == 'paper' and cpuchoice == 'rock') or \
        (userchoice == 'scissors' and cpuchoice == 'paper'):
        result_label.config(text= "WIN!")
    else:
        result_label.config(text= "LOSE!")
# This starts the GUI Code.    
import tkinter as tk
window = tk.Tk()
window.title("RSP GUI Version")
window.geometry("300x200")
title_label = tk.Label(window, text="What will you choose?", font=("Arial, 14"))
title_label.pack()
rockbtn = tk.Button(window, text = "rock", command = lambda: game('rock'))
rockbtn.pack()
paperbtn = tk.Button(window, text = "paper", command = lambda: game('paper'))
paperbtn.pack()
scissorsbtn = tk.Button(window, text = "scissors", command = lambda: game('scissors'))
scissorsbtn.pack()
result_label = tk.Label(window, text = "Result: -", font=("Arial, 12"))
result_label.pack()
window.mainloop()
