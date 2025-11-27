# This is the main code part.
second = 0
minute = 0
hour = 0
running = False
import time
def stopwatch():
    global hour, minute, second, running
    if running:
        second += 1
        if second == 60:
            second = 0
            minute += 1
        if minute == 60:
            minute = 0
            hour += 1
        watch_label.config(text = f"{hour}:{minute}:{second}")
        window.after(1000, stopwatch)
def start():
    global running
    running = True
    stopwatch()
def end():
    global second, hour, minute, running
    running = False
    second = 0
    hour = 0
    minute = 0
    watch_label.config(text = f"{hour}:{minute}:{second}")
# This is the GUI Part.
import tkinter as tk
window = tk.Tk()
window.title("StopWatch")
window.geometry("300x200")
title_label = tk.Label(window, text = "Stopwatch Program", font = ("Arial, 20"))
title_label.pack()
watch_label = tk.Label(window, text = f"{hour}:{minute}:{second}", font =("Arial, 18"))
watch_label.pack()
startbtn = tk.Button(window, text = "Start", command = start)
startbtn.pack()
endbtn = tk.Button(window, text = "End", command = end)
endbtn.pack()
window.mainloop()