def xpload():
    try:
        with open("xp.txt", "r", encoding = "utf-8") as f:
            lines = f.readlines()
            if not lines:
                return 0
            
            lastline = lines[-1].strip()
            parts = lastline.split("|")
            return int(parts[-1])
    except FileNotFoundError:
        return 0

xp = xpload()
import time
import datetime as dt
import random
calclist = ["+", "-", "*", "/"]
with open("typelist.txt", "r", encoding = "UTF-8") as f:
    sentences = f.read().splitlines()

levels = {
    100: "Lv.1",
    300: "Lv.2",
    600: "Lv.3",
    1000: "Lv.4",
    1500: "Lv.5"
}

def calc(x, y, calcul):
    if calcul == "+": return x + y
    if calcul == "-": return x - y
    if calcul == "*": return x * y
    return x / y

def game():
    while True:
        global xp
        x = random.randrange(1,101)
        y = random.randrange(1,101)
        calcul = random.choice(calclist)
        calcstart = time.perf_counter()
        
        try:
            userans = float(input(f"{x} {calcul} {y} = ? "))
        except ValueError:
            print("Invalid Input.")
            continue
        
        if abs(userans - calc(x, y, calcul)) < 0.0001:
            calcend = time.perf_counter()
            calctime = calcend - calcstart
            print(f"Correct! Time: {calctime} Second(s).")
            calcnow = dt.datetime.now()

            if calctime < 3:
                xp += 15
            else:
                xp += 10

            with open("xp.txt", "a", encoding = "utf-8") as f:
                f.write(f"Game | Correct | {calcnow} | {xp}\n")

        else:
            print("Wrong!")
            calcnow = dt.datetime.now()
            with open("xp.txt", "a", encoding = "utf-8") as f:
                f.write(f"Game | Wrong | {calcnow} | {xp}\n")
        break

def typer():
    global xp
    ransen = random.choice(sentences)
    print(ransen)
    typestart = time.perf_counter()
    typeuser = input("Enter the sentence above. ")

    if ransen == typeuser:
        typeend = time.perf_counter()
        typetime = typeend - typestart
        print(f"Correct! Time: {typetime} Second(s).")

        if typetime < 10:
            xp += 15
        else:
            xp += 10
        typedate = dt.datetime.now()

        with open("xp.txt", "a", encoding = "utf-8") as f:
            f.write(f"Type | Correct | {typedate} | {xp}\n")

    else:
        print("Wrong!")
        typedate = dt.datetime.now()
        with open("xp.txt", "a", encoding = "utf-8") as f:
            f.write(f"Type | Wrong | {typedate} | {xp}\n")

def record():
    with open("xp.txt", "r", encoding = "utf-8") as f:
        xplist = f.read()
        print(xplist)

while True:
    ui = input("Game, Typing, Records, End. ").lower()
    if ui == "game":
        game()
    elif ui == "typing":
        typer()
    elif ui == "records":
        record()
    elif ui == "end":
        print("This ends the XP Game.")
        break
    else:
        print("Invalid Input.")
        continue

    if xp <= 100:
        level = levels[100]
    elif 100 < xp <= 300:
        level = levels[300]
    elif 300 < xp <= 600:
        level = levels[600]
    elif 600 < xp <= 1000:
        level = levels[1000]
    elif 1000 < xp <= 1500:
        level = levels[1500]
    else:
        level = "Lv.6"

    print(f"Your Level: {level}")