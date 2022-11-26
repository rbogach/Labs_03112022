import math


def makeMatrix():
    size = input("Enter a number")
    if size.isnumeric():
        size = int(size)
        for row in range(0, size):
            for col in range(0, size):
                if row == col:
                    print("1 ", end="  ")
                else:
                    print("0 ", end="   ")
    else:
        print("It is NaN NOT A NUMBER!!!")


makeMatrix()
