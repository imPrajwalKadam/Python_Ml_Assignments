"""
Write a program which accepts one number and prints its binary equivalent.
"""

def displayBinary(no):

    if no == 0:
        print(0)
        return

    binary = ""

    while no > 0:
        binary = chr((no % 2) + 48) + binary
        no //= 2

    print(binary)


def main():
    no = int(input("Enter a number: "))
    displayBinary(no)


if __name__ == "__main__":
    main()