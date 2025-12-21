print("Schedule Manager.")
import datetime as dt
import statistics
timelist = []
subjectlist = []

while True:
    start = input("Enter 'Start' when you want to start your work. ").lower()
    if start == "start":
        datestart = dt.datetime.now()
    else:
        print("Invalid Input.")
        continue

    end = input("Enter 'Done' when you finish your work. ").lower()
    if end == "done":
        dateend = dt.datetime.now()
    else:
        print("Invalid Input.")
        continue

    totaltime = dateend - datestart
    timelist.append(totaltime)
    subject = input("What did you do? ").lower()
    subjectlist.append(subject)

    with open("dateslist.txt", "a", encoding="utf-8") as f:
        f.write(f"{datestart} | {dateend} | {subject} | {totaltime}.\n")
    
    mode_value = statistics.mode(subjectlist)
    print(f"The most common subject: {mode_value}")
    maxtime = max(timelist)
    print(f"The longest time: {maxtime}")