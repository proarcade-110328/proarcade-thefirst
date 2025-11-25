import random
number = random.randrange(100,1000)
numberh = str(number)[0]
numbert = str(number)[1]
numbero = str(number)[2]
def strike():
    strikecount = 0
    if userh == numberh:
        strikecount += 1
    if usert == numbert:
        strikecount += 1
    if usero == numbero:
        strikecount += 1
    print(f"{strikecount} Strike(s).")
    return strikecount
def ball():
    ballcount = 0
    if userh == numbert or userh == numbero:
        ballcount += 1
    if usert == numberh or usert == numbero:
        ballcount += 1
    if usero == numberh or usero == numbert:
        ballcount += 1
    print(f"{ballcount} Ball(s).")
    return ballcount
def out(strikecount, ballcount):
    outcount = 3 - strikecount - ballcount
    print(f"{outcount} Out(s).")
    return outcount
while True:
    userinput = input("Input 3 digit number: ")
    if not userinput.isdigit():
        print("Please input a number.")
        continue
    if not (100<=int(userinput)<=999):
        print("Not an appropriate number for Number Baseball.")
        continue
    userh = userinput[0]
    usert = userinput[1]
    usero = userinput[2]
    s = strike()
    b = ball()
    o = out(s,b)
    if s == 3:
        print("You won.")
        again = input("Do you want to play again? (y/n)").lower()
        if again != "y":
            print("Goodbye!")
            break
        else:
            print("Starting a new game....\n")
            number = random.randrange(100,1000)
            numberh = str(number)[0]
            numbert = str(number)[1]
            numbero = str(number)[2]