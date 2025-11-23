def helloworld():
    print("Hello, World!")
def ninetynine():
    for i in range(99,0,-1):
        if i >= 3:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.\n")
        elif i == 2:
            print("2 bottles of beer on the wall, 2 bottles of beer.")
            print("Take one down and pass it around, 1 bottle of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
            print("No bottles of beer on the wall, no more bottles of beer.")
            print("Go to the store and buy some more, 99 bottles of beer on the wall.")
def adder():
    x = 0
    x = x + 1
while True:
    answer = input("Enter a H9+ command. ").upper()
    if answer == "H":
        helloworld()
    elif answer == "9":
        ninetynine()
    elif answer == "+":
        adder()
    else:
        print("Invalid command.")
        break
    again = input("Do you want to enter another?(y/n)").lower()
    if again != "y":
        print("This ends the H9+ interpreter.")
        break