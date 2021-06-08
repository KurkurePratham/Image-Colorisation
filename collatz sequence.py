import sys


def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    print(number)
    return number


while True:
    try:
        num = int(input("Enter an integer no."))
        while True:
            num = collatz(num)
            if num == 1:
                sys.exit()
    except ValueError:
        print("This is not an integer")
