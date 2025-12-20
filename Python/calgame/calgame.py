import random
import time
diffic = ['Easy', 'Normal', 'Hard']
calclist = ['+', '-', '*', '/']

def calc(fnum, snum, calcdif):
    if calcdif == '+': return fnum + snum
    if calcdif == '-': return fnum - snum
    if calcdif == '*': return fnum * snum
    return fnum / snum

ranges = {
    'Easy': 10,
    'Normal': 100,
    'Hard': 1000
}

while True:
    print("Calculation Game.")
    calcdif = input("What calculation do you want to do? ")
    if calcdif in calclist:
        print(f"Your calculation: {calcdif}.")
    else:
        print("Your calculation will be random.")
        calcdif = random.choice(calclist)

    gamedif = input("What difficulty do you want to do? ")
    if gamedif in diffic:
        print(f"Your difficulty: {gamedif}.")
    else:
        print("Your difficulty will be random.")
        gamedif = random.choice(diffic)

    start = time.perf_counter()

    limit = ranges[gamedif]
    fnum = random.randrange(1, limit + 1)
    snum = random.randrange(1, limit + 1)
    try:
        userans = float(input(f"{fnum} {calcdif} {snum} = "))
    except ValueError:
        print("Unvalid answer, Please input again.")
        continue
    answer = calc(fnum, snum, calcdif)

    if abs(answer - userans) < 0.0001:
        end = time.perf_counter()
        print("You're correct!")
        totaltime = end - start
        print(f"Calculation Time: {totaltime} Second(s)")
    else:
        print("You're NOT correct.")

    again = input("Do you want to play again? (y/n) ").lower()
    if again != "y":
        print("This ends the calculation game.")
        break
    else:
        print("Restarting...")