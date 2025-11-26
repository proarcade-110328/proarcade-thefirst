# This starts the GUI version.
import random
cpu = ['rock', 'paper', 'scissors']
tienum = 0
winnum = 0
losenum = 0
def game(userchoice):
    global tienum, winnum, losenum
    cpuchoice = random.choice(cpu)
    if userchoice == cpuchoice:
        result_label.config(text= "TIE!")
        computer_label.config(text= "Computer: " + cpuchoice)
        tienum = tienum + 1
        tie_label.config(text = f"Tie(s): {tienum}")
    elif (userchoice == 'rock' and cpuchoice == 'scissors') or \
        (userchoice == 'paper' and cpuchoice == 'rock') or \
        (userchoice == 'scissors' and cpuchoice == 'paper'):
        result_label.config(text= "WIN!")
        computer_label.config(text= "Computer: " + cpuchoice)
        winnum = winnum + 1
        win_label.config(text = f"Win(s): {winnum}")
    else:
        result_label.config(text= "LOSE!")
        computer_label.config(text= "Computer: " + cpuchoice)
        losenum = losenum + 1
        lose_label.config(text = f"Lose(s): {losenum}")
def retry():
    global winnum, losenum, tienum
    computer_label.config(text= "Computer: -")
    result_label.config(text = "Result: -")
    winnum = 0
    losenum = 0
    tienum = 0
    win_label.config(text = "Win(s): 0")
    tie_label.config(text = "Tie(s): 0")
    lose_label.config(text = "Lose(s): 0")
# This starts the GUI Code.    
import tkinter as tk
window = tk.Tk()
window.title("RSP GUI Version")
window.geometry("300x250")
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
computer_label = tk.Label(window, text = "Computer: -", font=("Arial, 12"))
computer_label.pack()
retrybtn = tk.Button(window, text = "Retry", command = retry)
retrybtn.pack()
win_label = tk.Label(window, text = "Win(s): 0", font = ("Arial, 10"))
win_label.pack()
tie_label = tk.Label(window, text = "Tie(s): 0", font = ("Arial, 10"))
tie_label.pack()
lose_label = tk.Label(window, text = "Lose(s): 0", font = ("Arial, 10"))
lose_label.pack()
window.mainloop()