import sys


def printarg():
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])


if __name__ == "__main__":
    print("helllo")
    printarg()
