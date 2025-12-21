print("A normal Math Quiz game.")

def start():
    while True:
        import random
        import time

        calclist = ["+", "-", "*", "/"]
        calculator = random.choice(calclist)
        fnum = random.randrange(1, 101)
        snum = random.randrange(1, 101)

        start = time.perf_counter()

        def calc(fnum, snum, calculator):
            if calculator == "+": return fnum + snum
            if calculator == "-": return fnum - snum
            if calculator == "*": return fnum * snum
            return fnum / snum
    
        try:
            userans = float(input(f"{fnum} {calculator} {snum} = ? "))
        except ValueError:
            print("Invalid Input.")
            continue

        if abs(userans - calc(fnum, snum, calculator)) < 0.0001:
            end = time.perf_counter()
            total = end - start

            print(f"Correct! Total Time: {total} Second(s).")
            with open("record.txt", "a", encoding="utf-8") as f:
                f.write(f"Correct | {total} Second(s).\n")
        else:
            end = time.perf_counter()
            total = end - start

            print(f"Wrong! Total Time: {total} Second(s).")
            with open("record.txt", "a", encoding="utf-8") as f:
                f.write(f"Wrong | {total} Second(s).\n")
        break

def records():
    with open("record.txt", "r", encoding = "UTF-8") as f:
        content = f.read()
        print(content)

while True:
    uiinput = input("Start, Records, End. ").lower()
    if uiinput == "start":
        start()
    elif uiinput == "records":
        records()
    elif uiinput == "end":
        print("This ends the Quiz game.")
        break
    else:
        print("Invalid Input.")