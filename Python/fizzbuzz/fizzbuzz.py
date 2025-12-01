def FizzBuzz():  
    if int(x) >= 1:
        for i in range(1,x+1):
            if i % 15 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
            i += 1
    else:
        print("Your number is so small.")
while True:
    x = input("Enter any integer.")
    try:
        x = int(x)
        FizzBuzz()
    except ValueError:
        print("Invaild input.")