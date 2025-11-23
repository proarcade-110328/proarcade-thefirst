def xinput():
    while True:
        x = input("Enter any number: ")
        try:
            x = int(x)
            return x
        except ValueError:
            print("Invalid input.")
while True:
    x = xinput()
    lengths = []
    for n in range(x):
        size = float(input(f"Enter the size of Variable {n+1}: "))
        lengths.append(size)
    variables1 = []
    for size in lengths:
        variables1.append(size)
    print(variables1)
    print("Now enter the calculations among +, -, *, /, %, //, **.\n")
    variables2 = []
    for k in range(x-1):
        calc = input(f"Enter calculation {k+1}: ")
        variables2.append(calc)
    print(variables2)
    answers = []
    answer = variables1[0]
    for i in range(len(variables2)):
        operation = variables2[i]
        nextnum = variables1[i+1]
        if operation == "+":
            answer += nextnum
        elif operation == "-":
            answer -= nextnum
        elif operation == "*":
            answer *= nextnum
        elif operation == "/":
            answer /= nextnum
        elif operation == "%":
            answer %= nextnum
        elif operation == "//":
            answer //= nextnum
        elif operation == "**":
            answer **= nextnum
        else:
            print(f"Invalid operation.")
            break
        answers.append(answer)
    print(f"{answer} is your result.")
    print(answers, " is your result history.")
    again = input("Do you want to do another calculation? (y/n)").lower()
    if again != "y":
        print("This ends the calculation program.")
        break
    else:
        print("Starting a new calculation.\n")